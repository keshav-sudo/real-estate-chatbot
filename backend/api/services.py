import pandas as pd
import google.generativeai as genai
from django.conf import settings
from typing import Dict, List, Any
import os
from .mongodb_service import get_mongo_service

# Configure Gemini AI
if settings.GEMINI_API_KEY:
    genai.configure(api_key=settings.GEMINI_API_KEY)


class RealEstateAnalyzer:
    """Service class for analyzing real estate data"""
    
    def __init__(self, excel_path: str = None):
        """Initialize with Excel file path"""
        self.excel_path = excel_path or os.path.join(settings.BASE_DIR, 'data', 'real_estate_data.xlsx')
        self.df = None
        self.mongo_service = get_mongo_service()
        self.load_data()
    
    def load_data(self):
        """Load data from MongoDB first, fallback to Excel"""
        try:
            # Try loading from MongoDB first
            self.df = self.mongo_service.get_all_data()
            
            # If MongoDB is empty, load from Excel and upload to MongoDB
            if self.df.empty and os.path.exists(self.excel_path):
                self.df = pd.read_excel(self.excel_path)
                self.df.columns = self.df.columns.str.strip()
                
                # Upload to MongoDB
                if settings.MONGODB_URI:
                    self.mongo_service.upload_data_from_excel(self.excel_path)
                    print("Data uploaded to MongoDB")
            
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            # Fallback to Excel
            if os.path.exists(self.excel_path):
                self.df = pd.read_excel(self.excel_path)
                self.df.columns = self.df.columns.str.strip()
            else:
                self.df = pd.DataFrame()
    
    def filter_by_area(self, area: str) -> pd.DataFrame:
        """Filter data by area/locality"""
        if self.df.empty:
            return pd.DataFrame()
        
        # Case-insensitive search
        filtered = self.df[self.df['Area'].str.contains(area, case=False, na=False)]
        return filtered
    
    def get_price_trend(self, area: str) -> List[Dict[str, Any]]:
        """Get price trend data for charting"""
        filtered_data = self.filter_by_area(area)
        
        if filtered_data.empty:
            return []
        
        # Group by year and calculate average price
        trend_data = filtered_data.groupby('Year')['Price'].mean().reset_index()
        trend_data = trend_data.sort_values('Year')
        
        return [
            {'year': int(row['Year']), 'price': float(row['Price'])}
            for _, row in trend_data.iterrows()
        ]
    
    def get_demand_trend(self, area: str) -> List[Dict[str, Any]]:
        """Get demand trend data for charting"""
        filtered_data = self.filter_by_area(area)
        
        if filtered_data.empty:
            return []
        
        # Group by year and calculate average demand
        trend_data = filtered_data.groupby('Year')['Demand'].mean().reset_index()
        trend_data = trend_data.sort_values('Year')
        
        return [
            {'year': int(row['Year']), 'demand': float(row['Demand'])}
            for _, row in trend_data.iterrows()
        ]
    
    def compare_areas(self, areas: List[str]) -> Dict[str, Any]:
        """Compare multiple areas"""
        comparison_data = {
            'price_comparison': [],
            'demand_comparison': []
        }
        
        for area in areas:
            filtered_data = self.filter_by_area(area)
            
            if not filtered_data.empty:
                avg_price = filtered_data['Price'].mean()
                avg_demand = filtered_data['Demand'].mean()
                
                comparison_data['price_comparison'].append({
                    'area': area,
                    'avg_price': float(avg_price)
                })
                comparison_data['demand_comparison'].append({
                    'area': area,
                    'avg_demand': float(avg_demand)
                })
        
        return comparison_data
    
    def get_filtered_table(self, area: str, limit: int = 50) -> List[Dict[str, Any]]:
        """Get filtered table data"""
        filtered_data = self.filter_by_area(area)
        
        if filtered_data.empty:
            return []
        
        # Convert to list of dictionaries
        table_data = filtered_data.head(limit).to_dict('records')
        
        # Convert numpy types to Python types
        for record in table_data:
            for key, value in record.items():
                if pd.isna(value):
                    record[key] = None
                elif isinstance(value, (pd.Timestamp, pd.DatetimeTZDtype)):
                    record[key] = str(value)
                elif hasattr(value, 'item'):  # numpy types
                    record[key] = value.item()
        
        return table_data
    
    def generate_summary_with_gemini(self, area: str, data: pd.DataFrame) -> str:
        """Generate AI summary using Gemini"""
        if not settings.GEMINI_API_KEY:
            return self.generate_mock_summary(area, data)
        
        try:
            # Calculate statistics
            avg_price = data['Price'].mean()
            avg_demand = data['Demand'].mean()
            year_range = f"{data['Year'].min()} to {data['Year'].max()}"
            total_records = len(data)
            
            # Create prompt for Gemini
            prompt = f"""
            Analyze the real estate data for {area} and provide a concise summary (3-4 sentences):
            
            Statistics:
            - Average Price: ₹{avg_price:,.2f}
            - Average Demand: {avg_demand:.2f}
            - Data Period: {year_range}
            - Total Records: {total_records}
            
            Provide insights about the market trends, pricing, and investment potential.
            """
            
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            return response.text
            
        except Exception as e:
            print(f"Error generating Gemini summary: {str(e)}")
            return self.generate_mock_summary(area, data)
    
    def generate_mock_summary(self, area: str, data: pd.DataFrame) -> str:
        """Generate a mock summary when Gemini is not available"""
        if data.empty:
            return f"No data available for {area}."
        
        avg_price = data['Price'].mean()
        avg_demand = data['Demand'].mean()
        year_range = f"{data['Year'].min()} to {data['Year'].max()}"
        
        # Price trend analysis
        price_trend = "stable"
        if len(data) > 1:
            price_change = ((data['Price'].iloc[-1] - data['Price'].iloc[0]) / data['Price'].iloc[0]) * 100
            if price_change > 10:
                price_trend = "growing"
            elif price_change < -10:
                price_trend = "declining"
        
        summary = f"""Real Estate Analysis for {area}:

The average property price in {area} is ₹{avg_price:,.2f}, with demand levels averaging {avg_demand:.2f} during the period {year_range}. 
The market shows a {price_trend} trend, making it {"a promising investment opportunity" if price_trend == "growing" else "an area worth monitoring"}. 
With {len(data)} data points analyzed, this locality demonstrates {"strong" if avg_demand > 50 else "moderate"} demand patterns."""
        
        return summary
    
    def analyze_query(self, query: str) -> Dict[str, Any]:
        """Main method to analyze user query and return comprehensive response"""
        query_lower = query.lower()
        
        # Extract area names from query
        areas = self.extract_areas_from_query(query_lower)
        
        if not areas:
            return {
                'success': False,
                'message': 'Could not identify any area in your query. Please specify an area name.'
            }
        
        # Check if it's a comparison query
        if 'compare' in query_lower and len(areas) > 1:
            return self.handle_comparison_query(areas)
        
        # Single area analysis
        return self.handle_single_area_query(areas[0], query_lower)
    
    def extract_areas_from_query(self, query: str) -> List[str]:
        """Extract area names from user query"""
        # Get unique areas from dataset
        if self.df.empty:
            return []
        
        unique_areas = self.df['Area'].unique()
        found_areas = []
        
        for area in unique_areas:
            if area.lower() in query:
                found_areas.append(area)
        
        return found_areas
    
    def handle_comparison_query(self, areas: List[str]) -> Dict[str, Any]:
        """Handle comparison between multiple areas"""
        comparison_data = self.compare_areas(areas)
        
        # Generate comparison summary
        summary = f"Comparing {' and '.join(areas)}:\n\n"
        for item in comparison_data['price_comparison']:
            summary += f"{item['area']}: Average Price ₹{item['avg_price']:,.2f}\n"
        
        summary += "\n"
        for item in comparison_data['demand_comparison']:
            summary += f"{item['area']}: Average Demand {item['avg_demand']:.2f}\n"
        
        return {
            'success': True,
            'summary': summary,
            'chart_data': {
                'type': 'comparison',
                'price_data': comparison_data['price_comparison'],
                'demand_data': comparison_data['demand_comparison']
            },
            'table_data': []
        }
    
    def handle_single_area_query(self, area: str, query: str) -> Dict[str, Any]:
        """Handle single area analysis query"""
        filtered_data = self.filter_by_area(area)
        
        if filtered_data.empty:
            return {
                'success': False,
                'message': f'No data found for {area}.'
            }
        
        # Generate summary
        summary = self.generate_summary_with_gemini(area, filtered_data)
        
        # Determine chart type based on query
        chart_type = 'price'
        chart_data = []
        
        if 'demand' in query:
            chart_type = 'demand'
            chart_data = self.get_demand_trend(area)
        elif 'price' in query or 'growth' in query:
            chart_type = 'price'
            chart_data = self.get_price_trend(area)
        else:
            # Default to price trend
            chart_type = 'both'
            chart_data = {
                'price': self.get_price_trend(area),
                'demand': self.get_demand_trend(area)
            }
        
        # Get table data
        table_data = self.get_filtered_table(area)
        
        return {
            'success': True,
            'summary': summary,
            'chart_data': {
                'type': chart_type,
                'data': chart_data
            },
            'table_data': table_data,
            'area': area
        }
