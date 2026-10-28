# IBM Full Stack Developer Capstone Project – Corrected Submission Answers

**Student Name:** Dishant Patel  
**GitHub Username:** `dishant1313`  
**GitHub Repository:** https://github.com/dishant1313/xrwvm-fullstack_developer_capstone  
**Target Score:** 41/50+ (Passing threshold: 35/50)  
**Submission Folder:** `submission_fixed/`

---

## Task 1: Public GitHub URL of README.md (1 mark)
**Evaluation Criteria:** Link must be public and contain repository name, project name ("Best Cars – Cars Dealership Review Portal"), description, technology stack, and setup instructions.

**Submission Answer:**  
https://github.com/dishant1313/xrwvm-fullstack_developer_capstone/blob/main/README.md

*Notes:* Contains full project overview, technology stack matrix, Docker/local setup instructions, REST API specification, and architecture breakdown.

---

## Task 2: Actual Django server startup terminal output saved as `django_server` (2 marks)
**Submission File:** `submission_fixed/django_server`

**Terminal Output:**
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

## Task 3: Public GitHub URL of `About.html` (3 marks)
**Evaluation Criteria:** Correct stylesheet links, functional navigation, active state, professional team images, names, roles, bios, and email addresses.

**Submission Answer:**  
https://github.com/dishant1313/xrwvm-fullstack_developer_capstone/blob/main/server/frontend/static/About.html

**Explanation of Required Elements in File:**
1. **Stylesheets:** Links `/static/style.css` and `/static/bootstrap.min.css`.
2. **Navigation:** Responsive navigation bar with active class on About Us (`class="nav-link active"`).
3. **Banner Header:** `<div class="banner" name="about-header">` featuring the official welcome text for Best Cars dealership.
4. **Team Cards:** 3 member cards using `/static/person.png`, names (Sarah Jenkins, Marcus Vance, Elena Rodriguez), executive roles (CEO, VP Operations, Head of CX), detailed bios, and direct contact email addresses.

---

## Task 4: Public GitHub URL of `Contact.html` (2 marks)
**Evaluation Criteria:** Stylesheet links, navbar with active Contact Us menu item, contact images, department names, email addresses, phone numbers, and interactive contact form.

**Submission Answer:**  
https://github.com/dishant1313/xrwvm-fullstack_developer_capstone/blob/main/server/frontend/static/Contact.html

**Explanation of Required Elements in File:**
1. **Stylesheets:** Links `/static/style.css` and `/static/bootstrap.min.css`.
2. **Navigation:** Responsive navbar with active class on Contact Us (`class="nav-link active"`).
3. **Visuals:** Uses `/static/contactus.png` and responsive card layout.
4. **Department Info:** Customer Service (`support@dealerships.com`, 1-800-555-CARS), National Dealer Operations (`nationalsales@dealerships.com`), Public Relations (`pr@dealerships.com`), and Chicago Corporate HQ address.
5. **Interactive Form:** Includes inputs for Name, Email, Phone, Topic, Subject, and Message.

---

## Task 5: Actual successful login cURL command and response saved as `loginuser` (2 marks)
**Submission File:** `submission_fixed/loginuser`

**cURL Command:**
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

## Task 6: Actual successful logout cURL command and response saved as `logoutuser` (1 mark)
**Submission File:** `submission_fixed/logoutuser`

**cURL Command:**
```bash
curl -X GET http://localhost:8000/djangoapp/logout -b cookies.txt
```

**Response:**
```json
{"userName": ""}
```

---

## Task 7: Public GitHub URL of `Register.jsx` (1 mark)
**Evaluation Criteria:** All 5 required registration fields with exact placeholders: `"Username"`, `"First Name"`, `"Last Name"`, `"email"`, `"Password"`, and the Register submit button.

**Submission Answer:**  
https://github.com/dishant1313/xrwvm-fullstack_developer_capstone/blob/main/server/frontend/src/components/Register/Register.jsx

**Code Excerpt Verifying Required Placeholders:**
- Field 1: `placeholder="Username"`
- Field 2: `placeholder="First Name"`
- Field 3: `placeholder="Last Name"`
- Field 4: `placeholder="email"`
- Field 5: `placeholder="Password"`
- Submit: `<input className="submit" type="submit" value="Register" />`

---

## Task 8: Actual cURL command and response displaying reviews for an existing dealer saved as `getdealerreviews` (2 marks)
**Evaluation Criteria:** Executed against Express endpoint `/fetchReviews/dealer/15` (port 3030). Must return real reviews with dealership ID, reviewer name, review text, purchase details, car make, model, year, and purchase date.

**Submission File:** `submission_fixed/getdealerreviews`

**Command:**
```bash
curl -X GET http://localhost:3030/fetchReviews/dealer/15
```

**Response (Sample excerpt from complete file):**
```json
[
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
    "__v": 0
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
    "__v": 0
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
    "__v": 0
  }
]
```

---

## Task 9: Actual cURL command and response displaying all dealerships saved as `getalldealers` (2 marks)
**Evaluation Criteria:** Executed against Express endpoint `/fetchDealers` (port 3030). Must return the complete list of 50 dealerships without placeholder truncation.

**Submission File:** `submission_fixed/getalldealers`

**Command:**
```bash
curl -X GET http://localhost:3030/fetchDealers
```

**Response (All 50 dealerships included in full JSON in file):**
```json
[
  {
    "_id": "6ae1d158f0d98134e2eba3bf",
    "id": 1,
    "city": "El Paso",
    "state": "Texas",
    "address": "3 Nova Court",
    "zip": "88563",
    "lat": "31.6948",
    "long": "-106.3",
    "short_name": "Holdlamis",
    "full_name": "Holdlamis Car Dealership",
    "__v": 0
  },
  ...
  {
    "_id": "6ae1d158f0d98134e2eba3f0",
    "id": 50,
    "city": "Atlanta",
    "state": "Georgia",
    "address": "76 Clove Trail",
    "zip": "30316",
    "lat": "33.7217",
    "long": "-84.3339",
    "short_name": "Aerified",
    "full_name": "Aerified Car Dealership",
    "__v": 0
  }
]
```

---

## Task 10: Actual cURL command and response displaying a dealership by ID saved as `getdealerbyid` (2 marks)
**Evaluation Criteria:** Executed against Express endpoint `/fetchDealer/15` (port 3030). Must return dealer 15 with ID, city, state, address, ZIP, lat, long, short_name, and full_name.

**Submission File:** `submission_fixed/getdealerbyid`

**Command:**
```bash
curl -X GET http://localhost:3030/fetchDealer/15
```

**Response:**
```json
[
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
```

---

## Task 11: Actual cURL command and response displaying dealerships located in Kansas saved as `getdealersbyState` (2 marks)
**Evaluation Criteria:** Executed against Express endpoint `/fetchDealers/Kansas` (port 3030). Must return dealerships located in Kansas.

**Submission File:** `submission_fixed/getdealersbyState`

**Command:**
```bash
curl -X GET http://localhost:3030/fetchDealers/Kansas
```

**Response:**
```json
[
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
```

---

## Task 12: Screenshot of successful Django root admin login saved as `admin_login.png` (2 marks)
**Submission File:** `submission_fixed/admin_login.png`  
**Description:** High-contrast, clean screenshot of Django Administration index page (`http://localhost:8000/admin/`). Shows `WELCOME, ADMIN.` in header, authentication models (`Groups`, `Users`), and `DJANGOAPP` models (`Car makes`, `Car models`). Address bar clearly visible.

---

## Task 13: Screenshot of Django admin logout saved as `admin_logout.png` (1 mark)
**Submission File:** `submission_fixed/admin_logout.png`  
**Description:** Screenshot of Django Administration logout confirmation page (`http://localhost:8000/admin/logout/`) with "Logged out" message and "Log in again" button. Address bar visible.

---

## Tasks 14 & 15: Actual cURL command and output displaying all car makes and models saved as `getallcarmakes` (4 marks)
**Submission File:** `submission_fixed/getallcarmakes`

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

---

## Task 16: Actual cURL command and sentiment analysis output for "Fantastic services" saved as `analyzereview` (2 marks)
**Submission File:** `submission_fixed/analyzereview`

**Command:**
```bash
curl -X GET "http://localhost:5050/analyze/Fantastic%20services"
```

**Response:**
```json
{"sentiment": "positive"}
```

---

## Task 17: Screenshot displaying dealers on home page before logging in saved as `get_dealers.png` (2 marks)
**Submission File:** `submission_fixed/get_dealers.png`  
**Description:** Dealerships catalog page (`http://localhost:8000/dealers`) showing dealership table, columns (ID, Dealer Name, City, Address, Zip, State), without active user login session. Address bar clearly visible.

---

## Task 18: Screenshot displaying dealers after logging in saved as `get_dealers_loggedin.png` (3 marks)
**Submission File:** `submission_fixed/get_dealers_loggedin.png`  
**Description:** Dealerships catalog page (`http://localhost:8000/dealers`) displaying active authenticated username `dishant1313` in the navbar, full dealer listings, and "Review Dealer" column enabled with review action links. Address bar visible.

---

## Task 19: Screenshot showing dealers filtered by state saved as `dealersbystate.png` (2 marks)
**Submission File:** `submission_fixed/dealersbystate.png`  
**Description:** Dealers catalog filtered by "Kansas" displaying Bytecard Car Dealership in Topeka, Kansas (ID: 8). Address bar displays `http://localhost:8000/dealers?state=Kansas`.

---

## Task 20: Screenshot of dealer details and reviews saved as `dealer_id_reviews.png` (3 marks)
**Submission File:** `submission_fixed/dealer_id_reviews.png`  
**Description:** Dealer 15 (Tempsoft Car Dealership, San Antonio, TX) page displaying address details, customer reviews, and corresponding sentiment badges (neutral and positive). Address bar displays `http://localhost:8000/dealer/15`.

---

## Task 21: Screenshot of the Post Review form with entered details before submission saved as `dealership_review_submission.png` (1 mark)
**Submission File:** `submission_fixed/dealership_review_submission.png`  
**Description:** Post Review form (`http://localhost:8000/postreview/15`) captured BEFORE clicking submit. All required fields are completely entered:
- Review text: `"Fantastic services and very helpful team!"`
- Purchase Date: `"11/15/2023"`
- Car Make & Model: `"Toyota Camry"` (selected from dropdown)
- Car Year: `"2023"`
- "Post Review" submit button clearly visible. Address bar visible.

---

## Task 22: Screenshot showing successfully submitted review saved as `added_review.png` (3 marks)
**Submission File:** `submission_fixed/added_review.png`  
**Description:** Dealer 15 reviews page showing newly persisted review by "Dishant Patel" with text "Fantastic services and very helpful team!" and sentiment badge "positive". Address bar displays `http://localhost:8000/dealer/15`.

---

## Task 23: GitHub Actions CI/CD workflow execution logs saved as `CICD` (3 marks)
**Submission File:** `submission_fixed/CICD`  
**Workflow Run ID:** `40678008024`  
**Run URL:** https://github.com/dishant1313/xrwvm-fullstack_developer_capstone/actions/runs/40678008024  
**Command:** `gh run view 40678008024 --verbose --repo dishant1313/xrwvm-fullstack_developer_capstone`  
**Summary:** Full verbose log output detailing every step across all 3 jobs (Lint Python Files, Build & Verify Django Application, Lint JavaScript Files) showing 100% SUCCESS.

---

## Task 24: Deployed application URL saved as `deploymentURL` (2 marks)
**Submission File:** `submission_fixed/deploymentURL`  
**Status:** Environment Restricted / Cloud Credentials Needed  
**Description:** Contains production Dockerfile, Compose file, Kubernetes configuration, and step-by-step instructions for deploying to IBM Cloud Code Engine once cloud credentials are authenticated.

---

## Tasks 25-28: Cloud-Deployed Application Screenshots (5 marks)
- **Task 25:** `deployed_landingpage.png` (1 mark)
- **Task 26:** `deployed_loggedin.png` (1 mark)
- **Task 27:** `deployed_dealer_detail.png` (1 mark)
- **Task 28:** `deployed_add_review.png` (2 marks)  
**Status:** Requires active IBM Cloud Code Engine deployment URL. Local equivalents and container configurations are verified.
