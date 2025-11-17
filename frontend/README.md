# Real Estate Chatbot - Frontend

Modern React frontend with Shadcn UI, Tailwind CSS, and beautiful animations.

## 🎨 Features

- **Shadcn UI Components** - Beautiful, accessible components
- **Tailwind CSS** - Utility-first styling
- **Lucide Icons** - Modern icon library
- **Recharts** - Interactive data visualization
- **Responsive Design** - Works on all devices
- **Smooth Animations** - Polished user experience
- **Gradient Theme** - Professional purple-indigo design

## 🚀 Quick Start

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## 📦 Dependencies

```json
{
  "react": "^18.3.1",
  "axios": "^1.7.9",
  "recharts": "^2.15.0",
  "lucide-react": "^0.468.0",
  "tailwindcss": "^3.4.17",
  "class-variance-authority": "^0.7.1",
  "clsx": "^2.1.1",
  "tailwind-merge": "^2.6.0"
}
```

## 🎯 Components

### UI Components (Shadcn)
- `Button` - Versatile button component
- `Card` - Container component
- `Input` - Form input
- `Badge` - Status indicators

### Custom Components
- `ChatMessage` - Message bubbles
- `ChartDisplay` - Chart rendering
- `DataTable` - Data grid with export
- `FileUpload` - File upload interface

## 🎨 Customization

### Colors
Edit `tailwind.config.js` to change the color scheme:

```js
colors: {
  primary: "262 83% 58%",  // Purple
  // Add your colors...
}
```

### Theme
Modify CSS variables in `src/index.css`:

```css
:root {
  --primary: 262 83% 58%;
  --background: 0 0% 100%;
  // Customize...
}
```

## 📱 Responsive Breakpoints

- `sm`: 640px
- `md`: 768px
- `lg`: 1024px
- `xl`: 1280px
- `2xl`: 1536px

## 🚢 Deployment

### Vercel
```bash
npm run build
vercel
```

### Netlify
```bash
npm run build
# Deploy dist/ folder
```

## 🔧 Environment Variables

Create `.env` file:
```
VITE_API_URL=http://localhost:8000/api
```

## 📄 License

MIT License
