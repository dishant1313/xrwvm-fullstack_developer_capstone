# IBM Cars Dealership Capstone Project - Full Stack Application

## Project Overview

A comprehensive, production-quality **Cars Dealership** web application developed as part of the **IBM Full Stack Developer Professional Certificate** Capstone Project. This project demonstrates integration of modern full-stack technologies including Django, React, Node.js, MongoDB, and Flask microservices.

## Live Demo

- **Local Application**: `http://localhost:8000`
- **Admin Panel**: `http://localhost:8000/admin` (credentials: admin / adminpass123)

## Technology Stack

| Layer | Technology |
|-------|------------|
| **Backend Framework** | Django 5.1 (Python 3.13) |
| **Frontend** | React 18 (JavaScript/JSX) |
| **Microservice** | Node.js + Express.js (Dealer/Review API) |
| **Sentiment Analysis** | Flask + NLTK VADER |
| **Primary Database** | SQLite (Car Makes, Models, Users) |
| **Document Database** | MongoDB (Dealerships, Reviews) |
| **Container Runtime** | Docker + Docker Compose |
| **CI/CD** | GitHub Actions |
| **Deployment Target** | IBM Cloud Code Engine |
| **CSS Framework** | Bootstrap 5 + Custom Claymorphism Design |

## Project Architecture

```
IBM Cars Dealership
├── server/                          # Django Backend
│   ├── djangoapp/                   # Main Django application
│   │   ├── models.py                # CarMake + CarModel models
│   │   ├── views.py                 # API views (login, dealers, reviews, cars)
│   │   ├── urls.py                  # URL routing
│   │   ├── admin.py                 # Django admin configuration
│   │   ├── populate.py              # Database seed data
│   │   ├── restapis.py              # HTTP client to microservices
│   │   └── microservices/
│   │       └── app.py               # Flask sentiment analysis service
│   ├── djangoproj/                  # Django project settings
│   ├── frontend/                    # React Frontend
│   │   ├── src/
│   │   │   ├── App.js               # React Router configuration
│   │   │   └── components/
│   │   │       ├── Header/          # Navigation component
│   │   │       ├── Dealers/         # Dealership list, detail, review components
│   │   │       └── Register/        # User registration
│   │   └── static/
│   │       ├── About.html           # About Us static page
│   │       ├── Contact.html         # Contact Us static page
│   │       └── Home.html            # Landing page
│   └── database/
│       └── app.js                   # Node.js/Express MongoDB microservice
└── .github/
    └── workflows/
        └── main.yml                 # GitHub Actions CI/CD workflow
```

## Features

### Authentication
- ✅ User registration with Username, First Name, Last Name, Email, Password
- ✅ Secure user login and logout
- ✅ Session-based authentication
- ✅ Username displayed after login in navigation bar
- ✅ Django admin panel with superuser access

### Dealership Management
- ✅ Display all 50 dealerships with city, state, and address
- ✅ Filter dealerships by US state (including Kansas)
- ✅ View individual dealership details
- ✅ Display customer reviews with sentiment analysis
- ✅ Authenticated users can post reviews
- ✅ Reviews persisted in MongoDB
- ✅ Newly posted reviews appear immediately

### Car Data
- ✅ 5 Car Makes: NISSAN, Mercedes, Audi, Kia, Toyota
- ✅ 15 Car Models across all makes
- ✅ Full Django admin integration
- ✅ REST API endpoint at `/djangoapp/get_cars`

### Sentiment Analysis
- ✅ Flask microservice using NLTK VADER
- ✅ REST endpoint: `GET /analyze/<text>`
- ✅ "Fantastic services" → `{"sentiment": "positive"}`
- ✅ Integrated into review display pipeline

### Static Pages
- ✅ About Us page with team profiles and contact info
- ✅ Contact Us page with department-specific contact form
- ✅ Professional claymorphism UI design
- ✅ Responsive Bootstrap 5 layout

## API Endpoints

### Django Backend (`http://localhost:8000`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/djangoapp/login` | User authentication |
| GET | `/djangoapp/logout` | User logout |
| POST | `/djangoapp/register` | User registration |
| GET | `/djangoapp/get_cars` | All car makes and models |
| GET | `/djangoapp/get_dealers` | All dealerships |
| GET | `/djangoapp/get_dealers/<state>` | Dealerships by state |
| GET | `/djangoapp/dealer/<id>` | Single dealership |
| GET | `/djangoapp/reviews/dealer/<id>` | Reviews for a dealership |
| POST | `/djangoapp/add_review` | Post a new review (auth required) |

### Node.js Microservice (`http://localhost:3030`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/fetchDealers` | All dealers from MongoDB |
| GET | `/fetchDealers/<state>` | Dealers by state |
| GET | `/fetchDealer/<id>` | Single dealer |
| GET | `/fetchReviews/dealer/<id>` | Reviews for dealer |
| POST | `/insert_review` | Insert new review into MongoDB |

### Sentiment Analysis Service (`http://localhost:5050`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/analyze/<text>` | Analyze text sentiment |

## Quick Start

### Prerequisites
- Python 3.10+
- Node.js 16+
- npm 8+

### 1. Clone the Repository
```bash
git clone https://github.com/dishant1313/xrwvm-fullstack_developer_capstone.git
cd xrwvm-fullstack_developer_capstone
```

### 2. Start the Node.js Microservice (MongoDB embedded)
```bash
cd server/database
npm install
node app.js
# Runs on http://localhost:3030
```

### 3. Start the Sentiment Analysis Service
```bash
cd server/djangoapp/microservices
pip install flask nltk
python app.py
# Runs on http://localhost:5050
```

### 4. Start the Django Backend
```bash
cd server
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
# Runs on http://localhost:8000
```

### 5. Access the Application
- **Home Page**: http://localhost:8000
- **Dealers**: http://localhost:8000/dealers
- **Admin Panel**: http://localhost:8000/admin
- **About Us**: http://localhost:8000/about
- **Contact Us**: http://localhost:8000/contact

### 6. Default Credentials
- **Admin**: username=`admin`, password=`adminpass123`
- **Test User**: username=`dishant1313`, password=`dishantpass123`

## Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up --build

# Services:
# - Django: http://localhost:8000
# - Node/MongoDB: http://localhost:3030
# - Sentiment: http://localhost:5050
```

## CI/CD Pipeline

GitHub Actions workflow (`.github/workflows/main.yml`) runs on every push to `main`:

1. **Python Linting** — flake8 code quality checks
2. **JavaScript Linting** — jshint code quality checks  
3. **Django Build & Test** — `python manage.py check` + migrations

View workflow runs: https://github.com/dishant1313/xrwvm-fullstack_developer_capstone/actions

## Project Author

**Dishant Patel**  
IBM Full Stack Developer Professional Certificate  
Capstone Project — 2026

## License

This project is part of the IBM Developer Skills Network curriculum.
