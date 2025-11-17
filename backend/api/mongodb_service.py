from pymongo import MongoClient
from django.conf import settings
import pandas as pd
from typing import List, Dict, Any
import os


class MongoDBService:
    """Service for MongoDB operations"""
    
    def __init__(self):
        self.client = None
        self.db = None
        self.collection = None
        self.connect()
    
    def connect(self):
        """Connect to MongoDB"""
        try:
            if settings.MONGODB_URI:
                self.client = MongoClient(settings.MONGODB_URI)
                self.db = self.client['real_estate_db']
                self.collection = self.db['properties']
                print("MongoDB connected successfully")
            else:
                print("MongoDB URI not configured, using local data only")
        except Exception as e:
            print(f"MongoDB connection failed: {str(e)}")
    
    def upload_data_from_excel(self, excel_path: str) -> Dict[str, Any]:
        """Upload data from Excel to MongoDB"""
        try:
            df = pd.read_excel(excel_path)
            df.columns = df.columns.str.strip()
            
            # Clear existing data
            if self.collection:
                self.collection.delete_many({})
            
            # Convert DataFrame to dict
            records = df.to_dict('records')
            
            # Insert into MongoDB
            if self.collection and records:
                result = self.collection.insert_many(records)
                return {
                    'success': True,
                    'count': len(result.inserted_ids),
                    'message': f'Successfully uploaded {len(result.inserted_ids)} records'
                }
            else:
                return {
                    'success': False,
                    'message': 'MongoDB not connected or no records to upload'
                }
        except Exception as e:
            return {
                'success': False,
                'message': f'Upload failed: {str(e)}'
            }
    
    def get_all_data(self) -> pd.DataFrame:
        """Get all data from MongoDB as DataFrame"""
        try:
            if self.collection:
                cursor = self.collection.find({}, {'_id': 0})
                data = list(cursor)
                if data:
                    return pd.DataFrame(data)
            return pd.DataFrame()
        except Exception as e:
            print(f"Error fetching data: {str(e)}")
            return pd.DataFrame()
    
    def get_data_by_area(self, area: str) -> pd.DataFrame:
        """Get data filtered by area"""
        try:
            if self.collection:
                query = {'Area': {'$regex': area, '$options': 'i'}}
                cursor = self.collection.find(query, {'_id': 0})
                data = list(cursor)
                if data:
                    return pd.DataFrame(data)
            return pd.DataFrame()
        except Exception as e:
            print(f"Error fetching data by area: {str(e)}")
            return pd.DataFrame()
    
    def get_unique_areas(self) -> List[str]:
        """Get list of unique areas"""
        try:
            if self.collection:
                areas = self.collection.distinct('Area')
                return sorted(areas)
            return []
        except Exception as e:
            print(f"Error fetching unique areas: {str(e)}")
            return []
    
    def save_query_log(self, query: str, response: Dict[str, Any]):
        """Save query logs to MongoDB"""
        try:
            if self.db:
                logs_collection = self.db['query_logs']
                log_entry = {
                    'query': query,
                    'success': response.get('success', False),
                    'timestamp': pd.Timestamp.now().isoformat()
                }
                logs_collection.insert_one(log_entry)
        except Exception as e:
            print(f"Error saving query log: {str(e)}")
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get database statistics"""
        try:
            if self.collection:
                total_records = self.collection.count_documents({})
                areas = self.get_unique_areas()
                
                # Get price range
                price_stats = list(self.collection.aggregate([
                    {
                        '$group': {
                            '_id': None,
                            'min_price': {'$min': '$Price'},
                            'max_price': {'$max': '$Price'},
                            'avg_price': {'$avg': '$Price'}
                        }
                    }
                ]))
                
                return {
                    'total_records': total_records,
                    'total_areas': len(areas),
                    'areas': areas,
                    'price_stats': price_stats[0] if price_stats else {}
                }
            return {}
        except Exception as e:
            print(f"Error getting statistics: {str(e)}")
            return {}
    
    def close(self):
        """Close MongoDB connection"""
        if self.client:
            self.client.close()


# Singleton instance
_mongo_service = None

def get_mongo_service():
    """Get MongoDB service instance"""
    global _mongo_service
    if _mongo_service is None:
        _mongo_service = MongoDBService()
    return _mongo_service
