# Echolife

A modern social media platform with AI-powered features and cloud storage integration.

## 🚀 Features

- ✅ User authentication with JWT
- ✅ Create, read, update, delete posts
- ✅ Image upload to AWS S3
- ✅ Like and comment on posts
- ✅ User profiles with bios
- ✅ Real-time feed updates
- ✅ Responsive design

## 📁 Project Structure

```
echolife/
├── backend/
│   ├── app.py                 # Main Flask application
│   ├── s3_service.py          # AWS S3 integration
│   ├── models.py              # SQLAlchemy models
│   ├── schemas.py             # Pydantic schemas
│   ├── auth.py                # Authentication utilities
│   ├── routes/
│   │   ├── auth.py            # Authentication routes
│   │   ├── posts.py           # Post management routes
│   │   └── comments.py        # Comment management routes
│   ├── requirements.txt       # Python dependencies
│   └── .env.example           # Environment variables template
├── frontend/
│   ├── src/
│   │   ├── App.jsx            # Main App component
│   │   ├── App.css            # App styles
│   │   └── components/
│   │       ├── Auth.jsx       # Authentication component
│   │       ├── Auth.css
│   │       ├── Feed.jsx       # Feed component
│   │       ├── Feed.css
│   │       ├── Profile.jsx    # User profile component
│   │       └── Profile.css
│   ├── package.json           # npm dependencies
│   └── .env                   # Frontend environment
├── README.md                  # Project documentation
└── .gitignore                # Git ignore rules
```

## 🛠 Tech Stack

- **Backend**: Flask, SQLAlchemy, JWT
- **Frontend**: React, Vite
- **Database**: SQLite
- **Storage**: AWS S3
- **Authentication**: JWT

## 📋 Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+
- AWS Account (for S3)

### Backend Setup
See [BACKEND.md](./backend/README.md)

### Frontend Setup
See [FRONTEND.md](./frontend/README.md)

## 🔐 Security

- All passwords are hashed using SHA256
- JWT tokens for secure API access
- CORS enabled for cross-origin requests
- Environment variables for sensitive data

## 📚 API Documentation

### Authentication
- `POST /api/auth/register` - Register
- `POST /api/auth/login` - Login
- `GET /api/auth/me` - Current user

### Posts
- `GET /api/posts` - List all
- `POST /api/posts` - Create
- `GET /api/posts/:id` - Get one
- `PUT /api/posts/:id` - Update
- `DELETE /api/posts/:id` - Delete

### Interactions
- `POST /api/posts/:id/like` - Like post
- `POST /api/posts/:id/unlike` - Unlike post
- `POST /api/comments/post/:id` - Add comment

## 🚀 Deployment

### Backend Deployment
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend Deployment
```bash
cd frontend
npm install
npm run build
npm run preview
```

## 📝 License

MIT License - feel free to use this project for personal or commercial purposes.

## 👨‍💻 Author

**proudjasi-a11y**

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For issues and questions, please open an issue on GitHub.
