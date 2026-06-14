<div align="center">

# 🎯 InterviewIQ

### AI-Powered Interview Preparation Platform

**Practice smarter. Prepare faster. Get job-ready with AI-generated interview questions.**

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=for-the-badge)](https://interview-roan-five.vercel.app/)
[![Frontend](https://img.shields.io/badge/Frontend-React-blue?style=for-the-badge&logo=react)](https://react.dev/)
[![Backend](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Deployment](https://img.shields.io/badge/Deployed%20on-Vercel-black?style=for-the-badge&logo=vercel)](https://vercel.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](#-license)

</div>

---

## 🌐 Live Demo

🔗 **Live Application:** [https://interview-roan-five.vercel.app/](https://interview-roan-five.vercel.app/)

---

## 📌 About the Project

**InterviewIQ** is an AI-powered interview preparation web application designed to help students, developers, and job seekers prepare for interviews more effectively.

Instead of manually searching for interview questions, users can generate role-based, topic-based, and difficulty-based questions using AI. The platform provides a clean dashboard where users can practice, improve confidence, and prepare for real-world technical and HR interviews.

This project is especially useful for:

- 🎓 Students preparing for internships
- 👨‍💻 Developers preparing for software engineering interviews
- 🤖 AI/ML learners preparing for technical interviews
- 🧑‍💼 Job seekers preparing for HR and behavioral interviews
- 📚 Anyone who wants structured interview practice

---

## 🚀 Why InterviewIQ?

Preparing for interviews can be difficult because questions are spread across many websites, videos, PDFs, and notes. InterviewIQ solves this problem by giving users a single platform where they can generate and practice interview questions quickly.

### The main goal of this project is to make interview preparation:

- Faster
- Smarter
- More organized
- More personalized
- More practical for real interviews

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🔐 User Authentication | Users can register and log in securely |
| 📊 Dashboard | Clean dashboard to access interview preparation tools |
| 🤖 AI Question Generation | Generate interview questions using AI |
| 🎯 Role-Based Practice | Prepare for specific roles such as Software Engineer, AI/ML Engineer, Data Scientist, etc. |
| 📚 Topic-Based Questions | Generate questions for selected topics or skill areas |
| ⚙️ Difficulty Selection | Practice beginner, intermediate, and advanced level questions |
| 🧠 Technical Interview Practice | Prepare for coding, backend, frontend, AI/ML, database, and system design interviews |
| 💬 HR Interview Practice | Practice common HR and behavioral interview questions |
| 📱 Responsive UI | Works on desktop, tablet, and mobile screens |
| ⚡ Fast Performance | Frontend deployed with Vercel for quick loading |

---

## 🧠 Main Use Cases

InterviewIQ can be used to prepare for different interview categories:

### 💻 Software Engineering Interviews

- OOP concepts
- REST APIs
- Authentication
- Database queries
- Frontend fundamentals
- Backend development
- Git and GitHub
- Debugging questions

### 🤖 AI/ML Interviews

- Machine learning basics
- Model evaluation
- Feature engineering
- Data preprocessing
- Classification and regression
- Overfitting and underfitting
- Real-world ML problem solving

### 🧑‍💼 HR Interviews

- Tell me about yourself
- Strengths and weaknesses
- Teamwork questions
- Problem-solving questions
- Career goals
- Conflict handling
- Communication skills

---

## 🏗️ Project Architecture

```text
User
 │
 ▼
Frontend Application
React / Vite / Tailwind CSS
 │
 ▼
API Requests
Axios / Fetch
 │
 ▼
Backend Server
FastAPI / Python
 │
 ▼
AI Question Generation Service
Gemini API / OpenAI API / LLM Provider
 │
 ▼
Database
SQLite / PostgreSQL
```

---

## 🛠️ Tech Stack

### Frontend

- **React.js** - Frontend library
- **Vite** - Fast development build tool
- **Tailwind CSS** - Utility-first CSS framework
- **JavaScript** - Application logic
- **React Router** - Page navigation
- **Axios / Fetch API** - API communication

### Backend

- **FastAPI** - Python backend framework
- **Python** - Backend programming language
- **JWT Authentication** - Secure user authentication
- **SQLite / PostgreSQL** - Database
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

### AI Integration

- Gemini API / OpenAI API / any LLM API
- AI-based question generation
- Prompt-based interview question creation

### Deployment

- **Frontend:** Vercel
- **Backend:** Render / Railway / VPS / Cloud server
- **Version Control:** Git and GitHub

---

## 📸 Screenshots

> Add your project screenshots inside a `screenshots` folder and update the paths below.

```md
![Home Page](./screenshots/home.png)
![Dashboard](./screenshots/dashboard.png)
![Question Generator](./screenshots/question-generator.png)
![Login Page](./screenshots/login.png)
```

---

## 📂 Folder Structure

```bash
interview-iq/
│
├── frontend/
│   ├── public/
│   │   └── favicon.ico
│   │
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── .env
│   ├── package.json
│   ├── vite.config.js
│   └── README.md
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── routes/
│   │   ├── services/
│   │   └── utils/
│   │
│   ├── .env
│   ├── requirements.txt
│   └── README.md
│
├── screenshots/
├── README.md
└── .gitignore
```

> If your project folder structure is different, update this section according to your actual files.

---

## ⚙️ Installation and Setup

Follow the steps below to run the project locally.

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/interview-iq.git
cd interview-iq
```

---

## 2️⃣ Frontend Setup

Go to the frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Create a `.env` file:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

Start the frontend development server:

```bash
npm run dev
```

Frontend will run at:

```text
http://localhost:5173
```

---

## 3️⃣ Backend Setup

Open a new terminal and go to the backend folder:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Install backend dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file inside the backend folder:

```env
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
DATABASE_URL=sqlite:///./interviewiq.db
AI_API_KEY=your_ai_api_key_here
```

Run the backend server:

```bash
uvicorn app.main:app --reload
```

Backend will run at:

```text
http://127.0.0.1:8000
```

---

## 🔑 Environment Variables

### Frontend `.env`

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

### Backend `.env`

```env
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
DATABASE_URL=sqlite:///./interviewiq.db
AI_API_KEY=your_ai_api_key_here
```

---

## 📡 API Endpoints

Example API endpoints used in this project:

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/register` | Register a new user |
| POST | `/api/auth/login` | Login user |
| GET | `/api/dashboard` | Get dashboard data |
| POST | `/api/questions/generate` | Generate AI interview questions |
| GET | `/api/questions/history` | Get previous generated questions |
| GET | `/api/profile` | Get user profile |

---

## 🔄 How the Application Works

```text
1. User opens InterviewIQ
2. User registers or logs in
3. User enters the dashboard
4. User selects interview role, topic, or difficulty
5. Frontend sends request to backend API
6. Backend sends prompt to AI service
7. AI generates interview questions
8. Questions are returned to the frontend
9. User practices and improves interview preparation
```

---

## 🧪 Example AI Prompt Flow

```text
User selected:
Role: Software Engineer
Topic: REST API
Difficulty: Intermediate

AI prompt:
Generate 10 intermediate-level REST API interview questions for a software engineering interview.
Include practical and concept-based questions.

Output:
1. What is a REST API?
2. What is the difference between PUT and PATCH?
3. How does JWT authentication work?
...
```

---

## 🎯 Project Goals

The main goals of InterviewIQ are:

- Build a real-world AI-powered web application
- Help users prepare for interviews efficiently
- Practice full-stack development skills
- Integrate frontend, backend, database, and AI API
- Create a strong portfolio project for GitHub and LinkedIn
- Demonstrate practical AI application development

---

## 🌟 What Makes This Project Special?

InterviewIQ is not just a simple question list. It is a practical AI application that combines:

- Full-stack development
- Authentication
- Dashboard UI
- AI API integration
- Role-based question generation
- Real interview preparation use case
- Modern deployment workflow

This makes it a strong portfolio project for:

- Software Engineer roles
- AI Engineer roles
- Machine Learning Engineer roles
- Full Stack Developer roles
- Junior Data Scientist roles

---

## 🚀 Deployment

---

## Frontend Deployment with Vercel

Build the frontend:

```bash
npm run build
```

Then deploy using Vercel:

1. Push the project to GitHub
2. Open Vercel
3. Import the GitHub repository
4. Select the frontend folder
5. Add environment variables
6. Deploy the project

Production frontend URL:

```text
https://interview-roan-five.vercel.app/
```

---

## Backend Deployment Options

You can deploy the backend using:

- Render
- Railway
- Fly.io
- AWS EC2
- DigitalOcean
- VPS hosting

After deploying the backend, update the frontend environment variable:

```env
VITE_API_BASE_URL=https://your-backend-url.com
```

Then redeploy the frontend.

---

## ✅ Testing Checklist

Before final deployment, check the following:

- [ ] User registration works
- [ ] User login works
- [ ] JWT token is stored correctly
- [ ] Dashboard loads correctly
- [ ] AI question generation works
- [ ] API requests are connected correctly
- [ ] Environment variables are set
- [ ] Frontend URL is updated
- [ ] Backend URL is updated
- [ ] Mobile responsiveness is checked
- [ ] No console errors
- [ ] No backend server errors
- [ ] README file is updated

---

## 🧭 Roadmap

Future improvements planned for InterviewIQ:

- [ ] Add answer evaluation using AI
- [ ] Add resume-based question generation
- [ ] Add job-description-based question generation
- [ ] Add voice-based mock interview practice
- [ ] Add interview score calculation
- [ ] Add user progress tracking
- [ ] Add question history
- [ ] Add PDF report download
- [ ] Add admin dashboard
- [ ] Add dark mode
- [ ] Add email verification
- [ ] Add password reset
- [ ] Add multi-language support
- [ ] Add coding interview practice section
- [ ] Add system design interview section

---

## 💡 Future AI Enhancements

Possible AI features:

- AI answer feedback
- AI scoring system
- AI-generated model answers
- AI mock interviewer
- AI resume analysis
- AI job role recommendation
- AI weakness detection
- AI personalized study plan

---

## 🤝 Contributing

Contributions are welcome.

To contribute:

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to the branch

```bash
git push origin feature/new-feature
```

5. Open a pull request

---

## 🧑‍💻 Author

Developed by **Mithushan**

### Connect

- 🌐 Live App: [InterviewIQ](https://interview-roan-five.vercel.app/)
- 💻 GitHub: [https://github.com/your-username](https://github.com/your-username)
- 🔗 LinkedIn: [https://linkedin.com/in/your-linkedin](https://linkedin.com/in/your-linkedin)
- 📧 Email: your-email@example.com

---

## 🏷️ Recommended Repository Name

```text
interview-iq
```

Alternative names:

```text
interviewiq
ai-interview-coach
interview-prep-ai
mock-interview-ai
careerprep-ai
```

---

## 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project with proper attribution.

---

## ⭐ Support

If you like this project, please give the repository a star on GitHub.

<div align="center">

### Made with ❤️ for smarter interview preparation

**InterviewIQ — Prepare smarter. Perform better.**

</div>
