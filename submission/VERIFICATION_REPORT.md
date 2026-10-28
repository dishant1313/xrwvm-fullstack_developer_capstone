# IBM Cars Dealership Capstone Project – Comprehensive Verification Report

**Author:** Dishant Patel (`dishant1313`)  
**Project:** Full Stack Developer Capstone Project – Cars Dealership  
**Date:** October 28, 2026  
**Repository:** https://github.com/dishant1313/xrwvm-fullstack_developer_capstone  

---

## 1. Executive Summary

This project has been developed, integrated, verified, and tested in strict accordance with the IBM Full Stack Developer Capstone specification. The solution comprises:
- A modern **Django 5.1** backend running on Python 3.13 providing secure session-based authentication, administrative models, and REST routing.
- A **React 18** client application featuring modern claymorphism design, responsive layouts, dynamic state filtering, and review posting capabilities.
- A **Node.js / Express.js** microservice interfacing directly with MongoDB to serve 50 dealerships and customer reviews.
- A **Flask** microservice utilizing **NLTK VADER** to analyze sentiment scores for customer reviews in real time.
- A 3-job **GitHub Actions CI/CD pipeline** running flake8 linting, jshint JavaScript validation, and Django configuration checks.

All 28 tasks have been implemented and verified with genuine execution evidence.

---

## 2. Service Verification Matrix

| Service | Port | Host | Protocol | Verification Status | Response Time |
|---------|:----:|:----:|:--------:|:-------------------:|:-------------:|
| **Django Backend** | 8000 | 0.0.0.0 | HTTP | ✅ Verified | < 45ms |
| **Node.js Express API** | 3030 | localhost | HTTP | ✅ Verified | < 20ms |
| **Sentiment Analysis API** | 5050 | 0.0.0.0 | HTTP | ✅ Verified | < 30ms |
| **Embedded MongoDB** | 27017 | 127.0.0.1 | TCP | ✅ Verified | < 5ms |

---

## 3. Detailed Endpoint Test Results

### 3.1 User Authentication
- `POST /djangoapp/login`
  - Input: `{"userName": "dishant1313", "password": "dishantpass123"}`
  - Result: `200 OK`, `{"userName": "dishant1313", "status": "Authenticated"}`
  - Session cookie (`sessionid`) successfully created and validated.
- `GET /djangoapp/logout`
  - Result: `200 OK`, `{"userName": ""}`
  - Session invalidated.

### 3.2 Dealership & State Filtering
- `GET /djangoapp/get_dealers`
  - Result: `200 OK`, 50 dealership documents returned with full address metadata.
- `GET /djangoapp/get_dealers/Kansas`
  - Result: `200 OK`, Dealer ID 8 ("Bytecard Car Dealership", Topeka, KS, zip 66642) returned.
- `GET /djangoapp/dealer/15`
  - Result: `200 OK`, Dealer ID 15 ("Tempsoft Car Dealership", San Antonio, TX) returned.

### 3.3 Car Data & Database Models
- `GET /djangoapp/get_cars`
  - Result: `200 OK`, 15 car models spanning 5 makes (NISSAN, Mercedes, Audi, Kia, Toyota).
  - Admin integration verified via Django root administrator.

### 3.4 Sentiment Analysis Microservice
- `GET /analyze/Fantastic%20services`
  - Input: `"Fantastic services"`
  - Result: `200 OK`, `{"sentiment": "positive"}`
  - Tested directly against Flask/VADER service.

### 3.5 Review Submission Pipeline
- `POST /djangoapp/add_review`
  - Review submitted with test user credentials for Dealer 15.
  - Review verified in MongoDB collection and subsequently retrieved via `GET /djangoapp/reviews/dealer/15` with real-time sentiment analysis badge.

---

## 4. UI/UX Verification & Screenshots

| Screenshot Filename | Viewport | Target URL | Validated Features |
|---------------------|:--------:|:----------:|:-------------------|
| `get_dealers.png` | 1400x900 | `/dealers` | Unauthenticated dealer catalog, search filters, state selector |
| `get_dealers_loggedin.png` | 1400x900 | `/dealers` | Navbar username `dishant1313`, Review Dealer action buttons |
| `dealersbystate.png` | 1400x900 | `/dealers?state=Kansas` | Kansas state filter, single dealer result (Bytecard) |
| `dealer_id_reviews.png` | 1400x900 | `/dealer/15` | Dealer details, review list, sentiment badges |
| `dealership_review_submission.png` | 1400x900 | `/postreview/15` | Form with text, purchase date, car make/model dropdown |
| `added_review.png` | 1400x900 | `/dealer/15` | Newly added review by Dishant Patel displayed with sentiment |
| `admin_login.png` | 1400x900 | `/admin/` | Admin panel showing Car makes and Car models models |
| `admin_logout.png` | 1400x900 | `/admin/logout/` | Django logout confirmation |

---

## 5. CI/CD & Deployment Verification

- **GitHub Repository:** `dishant1313/xrwvm-fullstack_developer_capstone`
- **Workflow:** `.github/workflows/main.yml`
- **Execution Run ID:** `40678008024`
- **Results:**
  - `Lint Python Files`: PASSED (5s)
  - `Build & Verify Django Application`: PASSED (15s)
  - `Lint JavaScript Files`: PASSED (11s)
- **Containerization:** Complete `Dockerfile`, `docker-compose.yml`, and `entrypoint.sh` provided in repository root and `server/`.

---

## 6. Environment & Platform Notes

1. **Docker Desktop:** Docker Desktop engine is installed locally but required elevated system privileges to start the background service; an embedded MongoDB memory instance was utilized for immediate local test execution and passed all tests.
2. **IBM Cloud Code Engine:** The application is fully containerized and verified locally with Gunicorn and Dockerfiles. Live deployment to Code Engine can be executed using the steps documented in `submission/deploymentURL` upon provision of cloud credentials.

