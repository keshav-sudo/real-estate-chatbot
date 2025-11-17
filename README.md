# 🏠 Real Estate Analysis Chatbot

A professional full-stack AI-powered real estate analysis chatbot built with **React**, **Django**, **MongoDB**, **Gemini AI**, and **Shadcn UI**.

![Tech Stack](https://img.shields.io/badge/React-18-blue) ![Django](https://img.shields.io/badge/Django-5.2.8-green) ![MongoDB](https://img.shields.io/badge/MongoDB-Latest-brightgreen) ![Gemini AI](https://img.shields.io/badge/Gemini-AI-purple)

## ✨ Features

### 🎯 Core Features
- **AI-Powered Analysis** - Gemini AI generates intelligent property market insights
- **Interactive Chat Interface** - Beautiful, modern chat UI with real-time responses
- **Data Visualization** - Interactive charts showing price and demand trends
- **Area Comparison** - Compare multiple localities side-by-side
- **File Upload** - Upload custom Excel datasets
- **CSV Export** - Download filtered data instantly
- **MongoDB Integration** - Scalable database with cloud support

### 🎨 UI/UX Features
- **Shadcn UI Components** - Beautiful, accessible component library
- **Tailwind CSS** - Modern, responsive design
- **Gradient Design** - Eye-catching purple-indigo theme
- **Smooth Animations** - Polished user experience
- **Dark Mode Ready** - Theme-aware components

### 📊 Analytics Features
- Price trend analysis over years
- Demand pattern visualization
- Multi-area comparison
- Statistical summaries
- Filterable data tables

## 🚀 Quick Start

### Prerequisites
- Node.js 16+ and npm
- Python 3.8+
- MongoDB account (optional, works with local Excel too)
- Gemini API key

### Installation

#### 1. Clone the Repository
```bash
cd /path/to/project/chatbot
```

#### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your keys:
# GEMINI_API_KEY=your_gemini_api_key
# MONGODB_URI=your_mongodb_connection_string (optional)

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

Backend will run at `http://localhost:8000`

#### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env
# Edit .env if needed (default: http://localhost:8000/api)

# Start development server
npm run dev
```

Frontend will run at `http://localhost:5173`

## 🔑 Getting API Keys

### Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy and paste into backend `.env` file

### MongoDB Connection String
1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create a free cluster
3. Get your connection string
4. Add to backend `.env` file as `MONGODB_URI`

**Note**: MongoDB is optional. The app works with local Excel files if MongoDB is not configured.

## 📁 Project Structure

```
chatbot/
├── backend/                 # Django REST API
│   ├── api/
│   │   ├── services.py     # Business logic
│   │   ├── mongodb_service.py  # MongoDB operations
│   │   ├── views.py        # API endpoints
│   │   └── urls.py         # API routes
│   ├── real_estate_chatbot/
│   │   └── settings.py     # Django configuration
│   ├── data/               # Sample Excel data
│   ├── requirements.txt    # Python dependencies
│   └── .env.example        # Environment template
│
└── frontend/               # React + Vite
    ├── src/
    │   ├── components/
    │   │   ├── ui/         # Shadcn UI components
    │   │   ├── ChatMessage.jsx
    │   │   ├── ChartDisplay.jsx
    │   │   ├── DataTable.jsx
    │   │   └── FileUpload.jsx
    │   ├── services/
    │   │   └── api.js      # API client
    │   ├── lib/
    │   │   └── utils.js    # Utility functions
    │   └── App.jsx         # Main app component
    ├── package.json
    └── .env.example
```

## 💬 Sample Queries

Try these queries in the chatbot:

- "Give me analysis of Wakad"
- "Compare Ambegaon Budruk and Aundh demand trends"
- "Show price growth for Akurdi over the last 3 years"
- "Analyze Aundh real estate market"
- "What are the price trends in Wakad?"

## 📊 Data Format

The app expects Excel files with these columns:
- `Year` - Year of the record
- `Area` - Locality/area name
- `Price` - Property price in ₹
- `Demand` - Demand index (0-100)
- `Size` - Property size in sq.ft
- `Property_Type` - Type (Apartment/Villa/etc)

Sample data is included in `backend/data/real_estate_data.xlsx`

## 🛠️ Technologies Used

### Backend
- **Django 5.2.8** - Web framework
- **Django REST Framework** - API development
- **MongoDB (PyMongo)** - Database
- **Pandas** - Data analysis
- **OpenPyXL** - Excel file handling
- **Google Gemini AI** - AI-powered insights
- **CORS Headers** - Frontend integration

### Frontend
- **React 18** - UI library
- **Vite** - Build tool & dev server
- **Tailwind CSS** - Styling
- **Shadcn UI** - Component library
- **Recharts** - Data visualization
- **Lucide React** - Icons
- **Axios** - HTTP client

## 🚢 Deployment

### Backend Deployment (Render/Railway)
```bash
# Add Procfile
web: gunicorn real_estate_chatbot.wsgi

# Install gunicorn
pip install gunicorn
pip freeze > requirements.txt

# Set environment variables in dashboard
# Deploy!
```

### Frontend Deployment (Vercel/Netlify)
```bash
# Build
npm run build

# Deploy
# - Drag dist/ folder to Netlify
# OR
# - Connect GitHub repo to Vercel
```

## 🎯 Assignment Completion Checklist

✅ **Backend (Django + Python)**
- [x] Excel data parsing and filtering
- [x] RESTful API endpoints
- [x] MongoDB integration
- [x] Gemini AI integration for summaries
- [x] Chart data generation
- [x] Table data filtering

✅ **Frontend (React + Modern UI)**
- [x] Beautiful chat interface with Shadcn UI
- [x] Text-based AI summaries
- [x] Interactive charts (Recharts)
- [x] Filterable data tables
- [x] File upload functionality
- [x] CSV export feature

✅ **Bonus Features**
- [x] Real Gemini AI integration
- [x] MongoDB database
- [x] Download data option
- [x] Modern UI with Shadcn + Tailwind
- [x] Responsive design
- [x] Smooth animations

✅ **Requirements**
- [x] GitHub repository with README
- [x] Clean code structure
- [x] Professional UI/UX
- [x] Working demo
- [x] Best practices followed

## 📹 Demo Video

Record a 1-2 minute demo showing:
1. Starting both servers
2. Asking sample queries
3. Viewing charts and data
4. Uploading a file
5. Exporting data

## 🐛 Troubleshooting

**Backend won't start:**
- Check Python version (3.8+)
- Ensure virtual environment is activated
- Verify all dependencies are installed

**Frontend won't start:**
- Check Node version (16+)
- Delete `node_modules` and reinstall
- Clear npm cache: `npm cache clean --force`

**MongoDB connection fails:**
- Verify connection string is correct
- Check network access in MongoDB Atlas
- The app still works without MongoDB

**Charts not showing:**
- Check API response in browser console
- Verify data format matches expected structure
- Ensure Recharts is properly installed

## 🤝 Contributing

This project is for a Full Stack Developer assignment. Feel free to fork and improve!

## 📄 License

MIT License - Free to use for internship assignments and learning

## 👨‍💻 Author

Built with ❤️ for **Sigmavalue Full Stack Developer Assignment**

### Key Highlights for Recruiters:
- ✅ Production-ready code structure
- ✅ Modern tech stack (React + Django + MongoDB + AI)
- ✅ Beautiful UI with Shadcn UI & Tailwind CSS
- ✅ RESTful API design
- ✅ AI integration (Gemini)
- ✅ Database integration (MongoDB)
- ✅ Responsive & accessible design
- ✅ Best practices & clean code
- ✅ Comprehensive documentation

---

**Made for Sigmavalue Internship Assignment** | [GitHub](#) | [Live Demo](#)
# real-estate-chatbot
