import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const sendChatQuery = async (query) => {
  try {
    const response = await api.post('/query/', { query });
    return response.data;
  } catch (error) {
    throw error.response?.data || { error: 'Failed to process query' };
  }
};

export const uploadFile = async (file) => {
  try {
    const formData = new FormData();
    formData.append('file', file);
    
    const response = await axios.post(`${API_BASE_URL}/upload/`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    
    return response.data;
  } catch (error) {
    throw error.response?.data || { error: 'Failed to upload file' };
  }
};

export const checkHealth = async () => {
  try {
    const response = await api.get('/health/');
    return response.data;
  } catch (error) {
    throw error.response?.data || { error: 'Health check failed' };
  }
};

export default api;
