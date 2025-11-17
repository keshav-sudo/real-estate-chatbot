# Real Estate Chatbot - Backend

Django REST API backend for real estate analysis chatbot powered by Gemini AI.

## 🚀 Features

- **RESTful API** for real estate data analysis
- **Gemini AI Integration** for intelligent summaries
- **Excel Data Processing** with pandas
- **CORS enabled** for frontend integration
- **File Upload Support** for custom datasets
- **Comprehensive Analytics** (price trends, demand analysis, area comparisons)

## 📋 Prerequisites

- Python 3.8+
- pip
- Virtual environment (recommended)

## 🛠️ Installation

1. **Create and activate virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables:**
```bash
cp .env.example .env
```

Edit `.env` and add your Gemini API key:
```
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

4. **Run migrations:**
```bash
python manage.py migrate
```

5. **Start development server:**
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000`

## 🔑 Getting Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key and add it to your `.env` file

## 📡 API Endpoints

### Health Check
```
GET /api/health/
```
Returns API status and configuration info.

### Chat Query
```
POST /api/query/
Content-Type: application/json

{
    "query": "Give me analysis of Wakad"
}
```

**Response:**
```json
{
    "success": true,
    "summary": "AI-generated analysis...",
    "chart_data": {
        "type": "price",
        "data": [...]
    },
    "table_data": [...],
    "area": "Wakad"
}
```

### File Upload
```
POST /api/upload/
Content-Type: multipart/form-data

file: <Excel file>
```

## 📊 Sample Queries

- "Give me analysis of Wakad"
- "Compare Ambegaon Budruk and Aundh demand trends"
- "Show price growth for Akurdi over the last 3 years"
- "Analyze Aundh real estate market"

## 🗂️ Project Structure

```
backend/
├── api/
│   ├── views.py          # API endpoints
│   ├── services.py       # Business logic & Gemini integration
│   ├── urls.py          # API routes
│   └── ...
├── real_estate_chatbot/
│   ├── settings.py      # Django settings
│   ├── urls.py         # Main URL configuration
│   └── ...
├── data/
│   └── real_estate_data.xlsx  # Sample dataset
├── requirements.txt     # Python dependencies
├── .env.example        # Environment variables template
└── manage.py          # Django management script
```

## 🔧 Technologies Used

- **Django 5.2.8** - Web framework
- **Django REST Framework** - API development
- **Pandas** - Data analysis
- **OpenPyXL** - Excel file handling
- **Google Generative AI** - Gemini integration
- **django-cors-headers** - CORS support

## 📝 Development

### Running Tests
```bash
python manage.py test
```

### Creating Superuser
```bash
python manage.py createsuperuser
```

### Admin Panel
Access at `http://localhost:8000/admin/`

## 🚢 Deployment

### For Production:

1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS`
3. Set up proper database (PostgreSQL recommended)
4. Use gunicorn or uwsgi
5. Configure static files serving

## 📄 License

MIT License - Feel free to use this project for your internship assignment!

## 👨‍💻 Author

Built with ❤️ for Sigmavalue Full Stack Developer Assignment
