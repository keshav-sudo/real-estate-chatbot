# 🚀 Complete Setup Guide

## Step-by-Step Installation

### 1. Prerequisites Check

**Verify you have:**
```bash
# Check Python version (need 3.8+)
python3 --version

# Check Node.js version (need 16+)
node --version

# Check npm
npm --version
```

If missing, install:
- Python: https://www.python.org/downloads/
- Node.js: https://nodejs.org/

### 2. Backend Setup (5 minutes)

```bash
cd backend

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # Mac/Linux
# OR
venv\Scripts\activate  # Windows

# Install packages
pip install -r requirements.txt

# Configure environment
cp .env.example .env
nano .env  # or use any text editor
```

**Edit `.env` file:**
```env
GEMINI_API_KEY=YOUR_ACTUAL_KEY_HERE
MONGODB_URI=YOUR_MONGODB_CONNECTION_STRING  # Optional
```

**Get Gemini API Key (FREE):**
1. Visit: https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy and paste into .env

**Get MongoDB URI (Optional - FREE):**
1. Visit: https://www.mongodb.com/cloud/atlas
2. Create free account & cluster
3. Click "Connect" → "Connect your application"
4. Copy connection string
5. Replace `<password>` with your password

```bash
# Initialize database
python manage.py migrate

# Test the server
python manage.py runserver
```

**Expected output:**
```
Starting development server at http://127.0.0.1:8000/
```

✅ Backend is ready! Keep this terminal running.

### 3. Frontend Setup (3 minutes)

Open a **NEW terminal window**:

```bash
cd frontend

# Install packages
npm install

# Configure environment (optional)
cp .env.example .env
# Edit if your backend is NOT at localhost:8000

# Start development server
npm run dev
```

**Expected output:**
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

✅ Frontend is ready!

### 4. Test the Application

1. Open browser: http://localhost:5173
2. You should see the chatbot interface
3. Try asking: "Give me analysis of Wakad"
4. Check if charts and data appear

## 🎯 Quick Test Checklist

- [ ] Backend running (http://localhost:8000)
- [ ] Frontend running (http://localhost:5173)
- [ ] Chat interface loads
- [ ] Can send a message
- [ ] Bot responds with analysis
- [ ] Charts display correctly
- [ ] Data table shows
- [ ] File upload works
- [ ] CSV export works

## 🐛 Common Issues & Solutions

### Issue: "Module not found"
**Solution:**
```bash
cd backend
pip install -r requirements.txt

cd frontend
rm -rf node_modules
npm install
```

### Issue: "Port already in use"
**Backend:**
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9  # Mac/Linux
# OR
netstat -ano | findstr :8000  # Windows, then kill PID
```

**Frontend:**
```bash
# Kill process on port 5173
lsof -ti:5173 | xargs kill -9  # Mac/Linux
```

### Issue: "Gemini API not working"
**Check:**
1. API key is correct in `.env`
2. No quotes around the key
3. .env file is in backend folder
4. Restart backend after editing .env

### Issue: "MongoDB connection failed"
**Solution:**
- MongoDB is OPTIONAL
- App works fine without it
- Just leave `MONGODB_URI` empty
- Data will be stored in Excel files

### Issue: "CORS error"
**Solution:**
Already configured! But if you see it:
```python
# In backend/real_estate_chatbot/settings.py
CORS_ALLOW_ALL_ORIGINS = True  # Should be there
```

## 📦 Package Sizes (Approximate)

**Backend:**
- Virtual env size: ~100MB
- Dependencies: 50+ packages

**Frontend:**
- node_modules: ~200MB
- Dependencies: 100+ packages

## ⚡ Quick Start Script

Use the included script (Mac/Linux):
```bash
chmod +x start.sh
./start.sh
```

This starts both servers automatically!

## 🎬 Creating Demo Video

Record these steps:
1. Show code in VS Code/editor
2. Open terminal, start backend
3. Open another terminal, start frontend
4. Show browser at localhost:5173
5. Type query: "Give me analysis of Wakad"
6. Show the response, charts, and data
7. Upload a file
8. Export data to CSV
9. Try comparison: "Compare Wakad and Aundh"
10. Show GitHub repository

**Tools for recording:**
- OBS Studio (Free)
- Loom (Easy)
- QuickTime (Mac)
- Windows Game Bar (Windows)

## 📤 Uploading to GitHub

```bash
cd /path/to/chatbot

# Initialize git (if not already)
git init

# Add all files
git add .

# Commit
git commit -m "Real Estate AI Chatbot - Complete Project"

# Create repo on GitHub, then:
git remote add origin https://github.com/yourusername/real-estate-chatbot.git
git branch -M main
git push -u origin main
```

## 🚀 Deployment (Optional Bonus)

### Backend - Render
1. Go to render.com
2. New → Web Service
3. Connect GitHub repo
4. Build: `pip install -r requirements.txt`
5. Start: `gunicorn real_estate_chatbot.wsgi`
6. Add environment variables

### Frontend - Vercel
1. Go to vercel.com
2. Import project
3. Select frontend folder
4. Deploy!

## ✅ Pre-Submission Checklist

- [ ] All code pushed to GitHub
- [ ] README.md is comprehensive
- [ ] .env.example files included (no secrets!)
- [ ] Sample data included
- [ ] Both servers run without errors
- [ ] Demo video recorded (1-2 minutes)
- [ ] Screenshots taken
- [ ] Requirements.txt / package.json updated
- [ ] Code is clean and commented
- [ ] UI looks professional

## 📞 Need Help?

**Check:**
1. This guide first
2. README.md in root folder
3. Backend README
4. Frontend README
5. Error messages in console

**Good luck with your internship! 🎉**
