#!/bin/bash

echo "🚀 Starting Real Estate Chatbot..."
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Start Backend
echo -e "${BLUE}📦 Starting Backend (Django)...${NC}"
cd backend
source venv/bin/activate
python manage.py runserver &
BACKEND_PID=$!
echo -e "${GREEN}✓ Backend started at http://localhost:8000${NC}"
echo ""

# Wait a moment for backend to start
sleep 2

# Start Frontend
echo -e "${BLUE}🎨 Starting Frontend (React)...${NC}"
cd ../frontend
npm run dev &
FRONTEND_PID=$!
echo -e "${GREEN}✓ Frontend started at http://localhost:5173${NC}"
echo ""

echo -e "${GREEN}✨ Application is ready!${NC}"
echo ""
echo "Backend API: http://localhost:8000"
echo "Frontend: http://localhost:5173"
echo ""
echo "Press Ctrl+C to stop all services"

# Wait for Ctrl+C
trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait
