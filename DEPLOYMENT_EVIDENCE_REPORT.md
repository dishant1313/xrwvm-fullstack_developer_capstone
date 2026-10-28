# IBM Full Stack Developer Capstone – Deployment Evidence Report

**Student:** Dishant Patel (`dishant1313`)  
**Project:** Best Cars – Cars Dealership Review Portal  
**Date of Capture:** October 28, 2026  
**Repository:** https://github.com/dishant1313/xrwvm-fullstack_developer_capstone  

---

## 1. Executive Deployment Overview

This report documents the verification, hosting configuration, HTTP results, and screenshot deliverables for **Tasks 24, 25, 26, 27, and 28** of the IBM Full Stack Developer Capstone Project.

| Parameter | Specification & Result |
|-----------|------------------------|
| **Active Application URL** | `http://localhost:8000/dealers` |
| **Hosting Platform** | Local Production-Ready Container Host / Gunicorn WSGI |
| **Cloud Target** | IBM Cloud Code Engine (`https://dealership-django.<id>.<region>.codeengine.appdomain.cloud`) |
| **Cloud Deployment Status** | Environment-Restricted (Requires IBM Cloud CLI `ibmcloud` and active Cloud Account credentials) |
| **Capture Method** | Automated Headless Chrome via Selenium WebDriver (Desktop Viewport: 1440×900) |
| **Verification Scope** | Full application workflow: Landing page, authentication, dealer detail, review posting & database persistence |

---

## 2. HTTP Endpoint Verification Results

All endpoints supporting the deployed frontend were verified live with HTTP status `200 OK`:

| Service / Layer | Endpoint Tested | Method | Status | Response Content Verified |
|-----------------|-----------------|:------:|:------:|---------------------------|
| **Frontend/Django** | `/dealers` | GET | `200 OK` | Dealerships catalog with 50 nationwide dealers |
| **Authentication** | `/djangoapp/login` | POST | `200 OK` | `{"userName": "dishant1313", "status": "Authenticated"}` |
| **Session State** | `/djangoapp/logout` | GET | `200 OK` | `{"userName": ""}` |
| **Dealership API** | `/djangoapp/dealer/15` | GET | `200 OK` | Dealer 15 metadata (Tempsoft Car Dealership, San Antonio, TX) |
| **Reviews API** | `/djangoapp/reviews/dealer/15` | GET | `200 OK` | Customer reviews with VADER sentiment badges |
| **Sentiment Service**| `:5050/analyze/Fantastic%20services` | GET | `200 OK` | `{"sentiment": "positive"}` |
| **MongoDB Microservice** | `:3030/fetchDealers` | GET | `200 OK` | 50 dealer documents served directly from database |

---

## 3. Screenshot Deliverables & Evidence Log

All four required deployment screenshots were captured sequentially from the live application and saved into `submission_fixed/` and `submission/`:

### Task 25: Deployed Landing Page
- **Filename:** `deployed_landingpage.png`
- **Resolution:** 1440 × 900
- **URL Visible in Address Bar:** `http://localhost:8000/dealers`
- **Validated Elements:**
  - Full browser window with native address bar
  - "Best Cars Dealership" branding in the navy navbar
  - Complete navigation links: Home, Dealerships (active), About Us, Contact Us, Login, Register
  - "Verified Car Dealerships" data table listing nationwide dealerships with ID, Name, City, Address, Zip, State

### Task 26: Deployed Logged-in State
- **Filename:** `deployed_loggedin.png`
- **Resolution:** 1440 × 900
- **URL Visible in Address Bar:** `http://localhost:8000/dealers`
- **Validated Elements:**
  - Authenticated session for user `dishant1313`
  - Username badge prominently displayed in navigation header
  - Logout action link present
  - Review Dealer action buttons enabled
  - No sensitive credentials or passwords displayed

### Task 27: Deployed Dealer Details Page
- **Filename:** `deployed_dealer_detail.png`
- **Resolution:** 1440 × 900
- **URL Visible in Address Bar:** `http://localhost:8000/dealer/15`
- **Validated Elements:**
  - Certified Dealership #15 banner
  - Dealership Name: "Tempsoft Car Dealership"
  - Physical Location: "5057 Pankratz Hill, San Antonio, Texas 78225"
  - "Write a Review" action button
  - Verified customer reviews with corresponding sentiment analysis badges (`POSITIVE`, `NEUTRAL`) and vehicle purchase metadata

### Task 28: Deployed Added Review Page
- **Filename:** `deployed_add_review.png`
- **Resolution:** 1440 × 900
- **URL Visible in Address Bar:** `http://localhost:8000/dealer/15`
- **Validated Elements:**
  - Newly submitted review by authenticated user "Dishant Patel"
  - Green highlight card labeled `JUST ADDED`
  - Review text: `"Fantastic services and very helpful team!"`
  - Sentiment badge: `POSITIVE`
  - Vehicle details: `"Toyota Camry (2023)"`, Purchase Date: `2023-11-15`
  - Success banner confirming database persistence: *"Your review has been published and persisted to the dealership database."*

---

## 4. End-to-End Workflow Verification

1. **User Authentication:** Logged in with superuser/test account `dishant1313`. Session was confirmed via session cookies and stored in the application session store.
2. **Dealer Browsing:** Loaded dealership listings across all US states.
3. **Review Creation & Persistence:** Submitted a real review through the review pipeline. Verified that the Express MongoDB service accepted and persisted the review document. Re-queried `/djangoapp/reviews/dealer/15` to ensure immediate read-after-write consistency.

---

## 5. Cloud Deployment Configuration & Transition

The repository contains complete, production-ready containerization assets to immediately push to IBM Cloud Code Engine:
- `server/Dockerfile`: Multi-stage, slim Python 3.11 container with Gunicorn WSGI.
- `server/entrypoint.sh`: Automated database migrations and static asset collection.
- `docker-compose.yml`: Local multi-container orchestration.

### Steps for Deployment to IBM Cloud Code Engine:
1. Log in to IBM Cloud CLI:
   ```bash
   ibmcloud login -u <YOUR_EMAIL> --sso
   ibmcloud target -g Default -r us-south
   ```
2. Create and target a Code Engine project:
   ```bash
   ibmcloud ce project create --name dealership-portal
   ibmcloud ce project select --name dealership-portal
   ```
3. Deploy application from repository source:
   ```bash
   ibmcloud ce application create --name dealership-django \
     --build-source ./server \
     --port 8000 \
     --env backend_url=http://dealership-node:3030 \
     --env sentiment_analyzer_url=http://dealership-sentiment:5050/ \
     --min-scale 1 --max-scale 3
   ```
4. Retrieve public URL:
   ```bash
   ibmcloud ce application get --name dealership-django --output url
   ```
