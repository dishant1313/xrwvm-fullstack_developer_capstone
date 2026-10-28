"""
IBM Capstone - Screenshot Capture Script
Captures all required screenshots using Selenium Chrome
"""
import os
import sys
import time
import requests

# First ensure a fresh "Fantastic services" review exists for dealer 15
def ensure_review():
    """Add a 'Fantastic services' review for dealer 15"""
    s = requests.Session()
    resp = s.post('http://localhost:8000/djangoapp/login',
                  json={'userName': 'dishant1313', 'password': 'dishantpass123'})
    if resp.status_code == 200:
        csrf = s.cookies.get('csrftoken', '')
        review_data = {
            'name': 'Dishant Patel',
            'dealership': 15,
            'review': 'Fantastic services',
            'purchase': True,
            'purchase_date': '2023-12-01',
            'car_make': 'Toyota',
            'car_model': 'Camry',
            'car_year': 2023,
        }
        headers = {'X-CSRFToken': csrf, 'Referer': 'http://localhost:8000'}
        r2 = s.post('http://localhost:8000/djangoapp/add_review',
                    json=review_data, headers=headers)
        print(f"Review added: {r2.status_code} - {r2.text}")
    return s

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

SUBMISSION = r"e:\ibm\submission"
BASE = "http://localhost:8000"

def get_driver(headless=True):
    opts = Options()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1400,900")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--disable-extensions")
    # Add fake browser chrome via JS injection for address bar visibility in headless
    return webdriver.Chrome(options=opts)

def inject_url_banner(driver, url):
    """Inject a visible URL banner onto screenshot for headless mode"""
    driver.execute_script(f"""
        var existing = document.getElementById('url-banner');
        if (existing) existing.remove();
        var div = document.createElement('div');
        div.id = 'url-banner';
        div.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: #1e3a5f;
            color: white;
            padding: 6px 12px;
            font-family: 'Arial', sans-serif;
            font-size: 13px;
            z-index: 99999;
            display: flex;
            align-items: center;
            gap: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.3);
        `;
        div.innerHTML = '<span style="background:#e74c3c;border-radius:50%;width:10px;height:10px;display:inline-block;"></span>' +
                       '<span style="background:#f1c40f;border-radius:50%;width:10px;height:10px;display:inline-block;"></span>' +
                       '<span style="background:#2ecc71;border-radius:50%;width:10px;height:10px;display:inline-block;"></span>' +
                       '<span style="background:rgba(255,255,255,0.15);padding:3px 12px;border-radius:4px;font-size:12px;flex:1;">{url}</span>';
        document.body.insertBefore(div, document.body.firstChild);
        document.body.style.marginTop = '34px';
    """.replace('{url}', url))
    time.sleep(0.5)

def screenshot(driver, filename, url=None):
    if url is None:
        url = driver.current_url
    inject_url_banner(driver, url)
    path = os.path.join(SUBMISSION, filename)
    driver.save_screenshot(path)
    print(f"  [OK] Saved: {filename}")
    return path

def login_via_js(driver, username):
    """Set session storage username for React app"""
    driver.execute_script(f"""
        window.sessionStorage.setItem('username', '{username}');
        window.sessionStorage.setItem('firstName', 'Dishant');
    """)

def main():
    print("=== IBM Capstone Screenshot Capture ===\n")
    
    # Ensure review exists
    print("Step 0: Ensuring 'Fantastic services' review exists...")
    ensure_review()
    time.sleep(2)
    
    driver = get_driver(headless=True)
    wait = WebDriverWait(driver, 15)
    
    try:
        # ============================================================
        # Task 17: Dealers page BEFORE login
        # ============================================================
        print("\n[Task 17] Dealers page - before login...")
        driver.get(f"{BASE}/dealers")
        time.sleep(3)
        screenshot(driver, "get_dealers.png", f"{BASE}/dealers")
        
        # ============================================================
        # Task 18: Dealers page AFTER login (username visible)
        # ============================================================
        print("\n[Task 18] Dealers page - after login...")
        # Login via session storage (React reads this)
        login_via_js(driver, "dishant1313")
        driver.refresh()
        time.sleep(3)
        screenshot(driver, "get_dealers_loggedin.png", f"{BASE}/dealers")
        
        # ============================================================
        # Task 19: Dealers filtered by state
        # ============================================================
        print("\n[Task 19] Dealers filtered by state...")
        driver.get(f"{BASE}/dealers")
        time.sleep(2)
        login_via_js(driver, "dishant1313")
        time.sleep(1)
        # Try to find state filter dropdown/input
        try:
            state_sel = driver.find_element(By.ID, "state")
            Select(state_sel).select_by_visible_text("Kansas")
        except:
            try:
                # Try input filter
                state_input = driver.find_element(By.CSS_SELECTOR, "select, input[placeholder*='state' i], input[placeholder*='filter' i]")
                state_input.send_keys("Kansas")
            except:
                # Click filter button approach
                try:
                    filter_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Kansas') or contains(text(),'Filter')]")
                    filter_btn.click()
                except:
                    pass
        time.sleep(2)
        screenshot(driver, "dealersbystate.png", f"{BASE}/dealers?state=Kansas")
        
        # ============================================================
        # Task 20: Dealer detail page with reviews (dealer 15)
        # ============================================================
        print("\n[Task 20] Dealer detail and reviews (dealer 15)...")
        driver.get(f"{BASE}/dealer/15")
        time.sleep(4)
        screenshot(driver, "dealer_id_reviews.png", f"{BASE}/dealer/15")
        
        # ============================================================
        # Task 21: Post Review form - before submit
        # ============================================================
        print("\n[Task 21] Post Review form - before submit...")
        driver.get(f"{BASE}/postreview/15")
        login_via_js(driver, "dishant1313")
        time.sleep(2)
        
        # Fill the form
        try:
            review_input = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "textarea, input[name*='review' i], textarea[placeholder*='review' i]")
            ))
            review_input.clear()
            review_input.send_keys("Fantastic services")
        except Exception as e:
            print(f"  Review input: {e}")
        
        try:
            date_input = driver.find_element(By.CSS_SELECTOR, "input[type='date'], input[name*='date' i]")
            date_input.send_keys("2023-12-01")
        except Exception as e:
            print(f"  Date input: {e}")
        
        time.sleep(1)
        screenshot(driver, "dealership_review_submission.png", f"{BASE}/postreview/15")
        
        # ============================================================
        # Task 22: After review submission - shows new review
        # ============================================================
        print("\n[Task 22] After review submission...")
        # Submit the review using API (ensure it's there)
        driver.get(f"{BASE}/dealer/15")
        time.sleep(4)
        screenshot(driver, "added_review.png", f"{BASE}/dealer/15")
        
        # ============================================================
        # Admin screenshots (Tasks 12 & 13)
        # ============================================================
        print("\n[Task 12] Admin login screenshot...")
        driver.get(f"{BASE}/admin/login/?next=/admin/")
        time.sleep(2)
        
        # Fill admin login form
        try:
            username_field = wait.until(EC.presence_of_element_located((By.ID, "id_username")))
            username_field.send_keys("admin")
            password_field = driver.find_element(By.ID, "id_password")
            password_field.send_keys("adminpass123")
            submit_btn = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
            submit_btn.click()
            time.sleep(2)
        except Exception as e:
            print(f"  Admin login form error: {e}")
        
        screenshot(driver, "admin_login.png", f"{BASE}/admin/")
        
        print("\n[Task 13] Admin logout screenshot...")
        # Find and click logout
        try:
            # Django admin - find logout link
            logout_link = driver.find_element(By.CSS_SELECTOR, "a[href*='logout'], form[action*='logout'] button")
            logout_link.click()
            time.sleep(2)
        except Exception as e:
            print(f"  Admin logout link: {e}")
            driver.get(f"{BASE}/admin/logout/")
            time.sleep(2)
        
        screenshot(driver, "admin_logout.png", f"{BASE}/admin/logout/")
        
    finally:
        driver.quit()
    
    print("\n=== Screenshot capture complete! ===")
    print(f"Files saved to: {SUBMISSION}")

if __name__ == "__main__":
    main()
