from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.conf import settings
import os
from .services import RealEstateAnalyzer


class ChatQueryView(APIView):
    """Handle chat queries for real estate analysis"""
    
    parser_classes = [JSONParser]
    
    def post(self, request):
        """Process user query and return analysis"""
        query = request.data.get('query', '').strip()
        
        if not query:
            return Response(
                {'error': 'Query is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            # Initialize analyzer
            analyzer = RealEstateAnalyzer()
            
            # Analyze query
            result = analyzer.analyze_query(query)
            
            if not result.get('success', False):
                return Response(
                    {'error': result.get('message', 'Analysis failed')},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            return Response(result, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {'error': f'An error occurred: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class FileUploadView(APIView):
    """Handle Excel file uploads"""
    
    parser_classes = [MultiPartParser, FormParser]
    
    def post(self, request):
        """Upload and save Excel file"""
        file_obj = request.FILES.get('file')
        
        if not file_obj:
            return Response(
                {'error': 'No file provided'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Validate file type
        if not file_obj.name.endswith(('.xlsx', '.xls')):
            return Response(
                {'error': 'Only Excel files (.xlsx, .xls) are allowed'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            # Create data directory if it doesn't exist
            data_dir = os.path.join(settings.BASE_DIR, 'data')
            os.makedirs(data_dir, exist_ok=True)
            
            # Save file
            file_path = os.path.join(data_dir, 'real_estate_data.xlsx')
            with open(file_path, 'wb+') as destination:
                for chunk in file_obj.chunks():
                    destination.write(chunk)
            
            return Response(
                {'message': 'File uploaded successfully', 'filename': file_obj.name},
                status=status.HTTP_201_CREATED
            )
            
        except Exception as e:
            return Response(
                {'error': f'File upload failed: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class HealthCheckView(APIView):
    """Health check endpoint"""
    
    def get(self, request):
        """Return API health status"""
        analyzer = RealEstateAnalyzer()
        
        return Response({
            'status': 'healthy',
            'data_loaded': not analyzer.df.empty,
            'gemini_configured': bool(settings.GEMINI_API_KEY)
        }, status=status.HTTP_200_OK)
