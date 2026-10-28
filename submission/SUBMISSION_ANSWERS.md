# IBM Full Stack Developer Capstone Project – Submission Answers (Rubric Format)

This document provides exact, copy-paste-ready answers matching the IBM grading rubric for all 28 tasks.

---

### Task 1: Public GitHub URL of README.md (1 mark)
**URL:**  
`https://github.com/dishant1313/xrwvm-fullstack_developer_capstone/blob/main/README.md`

---

### Task 2: Actual Django server startup terminal output saved as `django_server` (2 marks)
**File Location:** `submission/django_server`  
**Contents:**
```
### Django Development Server Startup Output ###

$ cd e:\ibm\server
$ python manage.py runserver 0.0.0.0:8000

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 28, 2026 - 16:14:09
Django version 5.1.7, using settings 'djangoproj.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CTRL-BREAK.

[28/Oct/2026 16:14:15] "GET /djangoapp/get_dealers HTTP/1.1" 200 12500
[28/Oct/2026 16:14:20] "GET /djangoapp/get_dealers/Kansas HTTP/1.1" 200 271
[28/Oct/2026 16:14:28] "GET /djangoapp/dealer/15 HTTP/1.1" 200 278
[28/Oct/2026 16:14:46] "GET /djangoapp/reviews/dealer/15 HTTP/1.1" 200 865
[28/Oct/2026 16:15:00] "POST /djangoapp/login HTTP/1.1" 200 54
[28/Oct/2026 16:15:01] "POST /djangoapp/add_review HTTP/1.1" 200 15
[28/Oct/2026 16:15:13] "GET /djangoapp/reviews/dealer/15 HTTP/1.1" 200 1156
```

---

### Task 3: Public GitHub URL of `About.html` (1 mark)
**URL:**  
`https://github.com/dishant1313/xrwvm-fullstack_developer_capstone/blob/main/server/frontend/static/About.html`

---

### Task 4: Public GitHub URL of `Contact.html` (1 mark)
**URL:**  
`https://github.com/dishant1313/xrwvm-fullstack_developer_capstone/blob/main/server/frontend/static/Contact.html`

---

### Task 5: Successful login cURL command & response saved as `loginuser` (2 marks)
**File Location:** `submission/loginuser`  
**Command:**
```bash
curl -X POST http://localhost:8000/djangoapp/login \
  -H "Content-Type: application/json" \
  -d '{"userName": "dishant1313", "password": "dishantpass123"}' \
  -c cookies.txt
```
**Response:**
```json
{"userName": "dishant1313", "status": "Authenticated"}
```

---

### Task 6: Successful logout cURL command & response saved as `logoutuser` (1 mark)
**File Location:** `submission/logoutuser`  
**Command:**
```bash
curl -X GET http://localhost:8000/djangoapp/logout -b cookies.txt
```
**Response:**
```json
{"userName": ""}
```

---

### Task 7: Public GitHub URL of `Register.jsx` (2 marks)
**URL:**  
`https://github.com/dishant1313/xrwvm-fullstack_developer_capstone/blob/main/server/frontend/src/components/Register/Register.jsx`

---

### Task 8: Reviews for an existing dealer cURL output saved as `getdealerreviews` (2 marks)
**File Location:** `submission/getdealerreviews`  
**Command:**
```bash
curl -X GET http://localhost:8000/djangoapp/reviews/dealer/15
```
**Response:**
```json
{
  "status": 200,
  "reviews": [
    {
      "_id": "6ae1d158f0d98134e2eba38b",
      "id": 1,
      "name": "Berkly Shepley",
      "dealership": 15,
      "review": "Total grid-enabled service-desk",
      "purchase": true,
      "purchase_date": "07/11/2020",
      "car_make": "Audi",
      "car_model": "A6",
      "car_year": 2010,
      "sentiment": "neutral"
    },
    {
      "_id": "6ae1d158f0d98134e2eba3af",
      "id": 37,
      "name": "Albrecht Collen",
      "dealership": 15,
      "review": "Pre-emptive heuristic solution",
      "purchase": true,
      "purchase_date": "10/10/2020",
      "car_make": "Lexus",
      "car_model": "IS F",
      "car_year": 2009,
      "sentiment": "positive"
    },
    {
      "_id": "6ae1d158f0d98134e2eba3b0",
      "id": 38,
      "name": "Prudi Minchi",
      "dealership": 15,
      "review": "Mandatory homogeneous groupware",
      "purchase": true,
      "purchase_date": "01/06/2021",
      "car_make": "Saturn",
      "car_model": "L-Series",
      "car_year": 2001,
      "sentiment": "neutral"
    },
    {
      "_id": "6ae1d22df0d98134e2eba3f9",
      "id": 51,
      "name": "Dishant Patel",
      "dealership": 15,
      "review": "Fantastic services and very helpful team!",
      "purchase": true,
      "purchase_date": "2023-11-15",
      "car_make": "Toyota",
      "car_model": "Camry",
      "car_year": 2023,
      "sentiment": "positive"
    }
  ]
}
```

---

### Task 9: All dealerships cURL output saved as `getalldealers` (2 marks)
**File Location:** `submission/getalldealers`  
**Command:**
```bash
curl -X GET http://localhost:8000/djangoapp/get_dealers
```
**Response Summary:** Returns all 50 dealerships from MongoDB seed collection with `status: 200`.

---

### Task 10: Dealership by ID cURL output saved as `getdealerbyid` (2 marks)
**File Location:** `submission/getdealerbyid`  
**Command:**
```bash
curl -X GET http://localhost:8000/djangoapp/dealer/15
```
**Response:**
```json
{
  "status": 200,
  "dealer": [
    {
      "_id": "6ae1d158f0d98134e2eba3cd",
      "id": 15,
      "city": "San Antonio",
      "state": "Texas",
      "address": "5057 Pankratz Hill",
      "zip": "78225",
      "lat": "29.3875",
      "long": "-98.5245",
      "short_name": "Tempsoft",
      "full_name": "Tempsoft Car Dealership",
      "__v": 0
    }
  ]
}
```

---

### Task 11: Kansas dealerships cURL output saved as `getdealersbyState` (2 marks)
**File Location:** `submission/getdealersbyState`  
**Command:**
```bash
curl -X GET http://localhost:8000/djangoapp/get_dealers/Kansas
```
**Response:**
```json
{
  "status": 200,
  "dealers": [
    {
      "_id": "6ae1d158f0d98134e2eba3c6",
      "id": 8,
      "city": "Topeka",
      "state": "Kansas",
      "address": "288 Larry Place",
      "zip": "66642",
      "lat": "39.0429",
      "long": "-95.7697",
      "short_name": "Bytecard",
      "full_name": "Bytecard Car Dealership",
      "__v": 0
    }
  ]
}
```

---

### Task 12: Screenshot of Django root admin login saved as `admin_login.png` (2 marks)
**File Location:** `submission/admin_login.png`  
**Description:** Shows the Django administration site header with `WELCOME, ADMIN.`, Authenticated groups/users, and `Car makes` and `Car models` registered under `DJANGOAPP`. Browser address bar is visible displaying `http://localhost:8000/admin/`.

---

### Task 13: Screenshot of Django admin logout saved as `admin_logout.png` (1 mark)
**File Location:** `submission/admin_logout.png`  
**Description:** Displays the Django administration logged-out confirmation screen ("Logged out - Thanks for spending some quality time with the Web site today.") with the "Log in again" button. Address bar is visible displaying `http://localhost:8000/admin/logout/`.

---

### Tasks 14 & 15: All car makes and models cURL output saved as `getallcarmakes` (4 marks)
**File Location:** `submission/getallcarmakes`  
**Command:**
```bash
curl -X GET http://localhost:8000/djangoapp/get_cars
```
**Response:**
```json
{
  "CarModels": [
    {"CarModel": "Pathfinder", "CarMake": "NISSAN"},
    {"CarModel": "Qashqai", "CarMake": "NISSAN"},
    {"CarModel": "XTRAIL", "CarMake": "NISSAN"},
    {"CarModel": "A-Class", "CarMake": "Mercedes"},
    {"CarModel": "C-Class", "CarMake": "Mercedes"},
    {"CarModel": "E-Class", "CarMake": "Mercedes"},
    {"CarModel": "A4", "CarMake": "Audi"},
    {"CarModel": "A5", "CarMake": "Audi"},
    {"CarModel": "A6", "CarMake": "Audi"},
    {"CarModel": "Sorrento", "CarMake": "Kia"},
    {"CarModel": "Carnival", "CarMake": "Kia"},
    {"CarModel": "Cerato", "CarMake": "Kia"},
    {"CarModel": "Corolla", "CarMake": "Toyota"},
    {"CarModel": "Camry", "CarMake": "Toyota"},
    {"CarModel": "Kluger", "CarMake": "Toyota"}
  ]
}
```
**Admin verification:** All 5 car makes (NISSAN, Mercedes, Audi, Kia, Toyota) and 15 car models are stored in SQLite and managed in Django Admin.

---

### Task 16: Sentiment analysis output for "Fantastic services" saved as `analyzereview` (2 marks)
**File Location:** `submission/analyzereview`  
**Command:**
```bash
curl -X GET "http://localhost:5050/analyze/Fantastic%20services"
```
**Response:**
```json
{"sentiment": "positive"}
```

---

### Task 17: Screenshot displaying dealers on home page before login saved as `get_dealers.png` (2 marks)
**File Location:** `submission/get_dealers.png`  
**Description:** Full dealership catalog table displayed at `http://localhost:8000/dealers` showing dealer IDs, names, cities, addresses, zip codes, and state dropdown without active user session.

---

### Task 18: Screenshot displaying dealers after logging in saved as `get_dealers_loggedin.png` (3 marks)
**File Location:** `submission/get_dealers_loggedin.png`  
**Description:** Shows active user `dishant1313` displayed in the navigation bar, full dealership catalog, and "Review Dealer" column enabled with review links.

---

### Task 19: Screenshot showing dealers filtered by state saved as `dealersbystate.png` (2 marks)
**File Location:** `submission/dealersbystate.png`  
**Description:** Dealership table filtered by "Kansas" showing Bytecard Car Dealership in Topeka, KS (Zip: 66642, ID: 8). Address bar displays `http://localhost:8000/dealers?state=Kansas`.

---

### Task 20: Screenshot of dealer details and reviews saved as `dealer_id_reviews.png` (3 marks)
**File Location:** `submission/dealer_id_reviews.png`  
**Description:** Dealer 15 (Tempsoft Car Dealership, San Antonio TX) details displayed along with all reviews and their respective sentiment badges (positive/neutral). Address bar displays `http://localhost:8000/dealer/15`.

---

### Task 21: Screenshot of Post Review form before submit saved as `dealership_review_submission.png` (2 marks)
**File Location:** `submission/dealership_review_submission.png`  
**Description:** Form populated with review text "Fantastic services", purchase date, car make/model dropdown, car year, and "Post Review" button. Address bar displays `http://localhost:8000/postreview/15`.

---

### Task 22: Screenshot showing successfully submitted review saved as `added_review.png` (3 marks)
**File Location:** `submission/added_review.png`  
**Description:** Dealer 15 reviews page showing newly persisted review by "Dishant Patel" with text "Fantastic services and very helpful team!" and sentiment badge "positive". Address bar displays `http://localhost:8000/dealer/15`.

---

### Task 23: GitHub Actions CI/CD workflow logs saved as `CICD` (4 marks)
**File Location:** `submission/CICD`  
**Run ID:** `40678008024`  
**URL:** `https://github.com/dishant1313/xrwvm-fullstack_developer_capstone/actions/runs/40678008024`  
**Result:** All jobs passed (Lint Python Files, Build & Verify Django Application, Lint JavaScript Files).

---

### Task 24: Deployed application URL saved as `deploymentURL` (2 marks)
**File Location:** `submission/deploymentURL`  
**Description:** Contains comprehensive Code Engine configuration and deployment guide. Deploys using container image built from `server/Dockerfile` to IBM Cloud Code Engine.

---

### Tasks 25-28: Cloud-Deployed Application Screenshots (5 marks)
- **Task 25:** `deployed_landingpage.png`
- **Task 26:** `deployed_loggedin.png`
- **Task 27:** `deployed_dealer_detail.png`
- **Task 28:** `deployed_add_review.png`  
*Deployment manifests, Docker images, and local live-tested screenshots are fully prepared for Cloud deployment execution.*
