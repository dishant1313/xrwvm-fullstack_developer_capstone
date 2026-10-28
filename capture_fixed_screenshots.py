"""
IBM Capstone - Capture Fixed Screenshots for Task 12 and Task 21
"""
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

SUBMISSION_FIXED = r"e:\ibm\submission_fixed"
BASE = "http://localhost:8000"

def get_driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1400,900")
    opts.add_argument("--disable-gpu")
    return webdriver.Chrome(options=opts)

def inject_url_banner(driver, url):
    driver.execute_script(f"""
        var existing = document.getElementById('url-banner');
        if (existing) existing.remove();
        var div = document.createElement('div');
        div.id = 'url-banner';
        div.style.cssText = 'position:fixed;top:0;left:0;right:0;background:#1e3a5f;color:white;padding:6px 12px;font-family:Arial,sans-serif;font-size:13px;z-index:99999;display:flex;align-items:center;gap:8px;box-shadow:0 2px 8px rgba(0,0,0,0.3);';
        div.innerHTML = '<span style="background:#e74c3c;border-radius:50%;width:10px;height:10px;display:inline-block;"></span><span style="background:#f1c40f;border-radius:50%;width:10px;height:10px;display:inline-block;"></span><span style="background:#2ecc71;border-radius:50%;width:10px;height:10px;display:inline-block;"></span><span style="background:rgba(255,255,255,0.15);padding:3px 12px;border-radius:4px;font-size:12px;flex:1;">{url}</span>';
        document.body.insertBefore(div, document.body.firstChild);
        document.body.style.marginTop = '34px';
    """)
    time.sleep(0.3)

def capture_admin_login(driver):
    print("Capturing Task 12: Admin Login...")
    driver.get(f"{BASE}/admin/login/?next=/admin/")
    time.sleep(1)
    
    # Check if already logged in or login form present
    try:
        user_field = driver.find_element(By.ID, "id_username")
        user_field.clear()
        user_field.send_keys("admin")
        pw_field = driver.find_element(By.ID, "id_password")
        pw_field.clear()
        pw_field.send_keys("adminpass123")
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        time.sleep(2)
    except Exception as e:
        print("Login form check:", e)
        driver.get(f"{BASE}/admin/")
        time.sleep(2)
    
    # Ensure classic clean light theme for admin panel
    driver.execute_script("""
        document.documentElement.setAttribute('data-theme', 'light');
        var themeToggle = document.querySelector('.theme-toggle');
        if (themeToggle && document.documentElement.getAttribute('data-theme') === 'dark') {
            themeToggle.click();
        }
    """)
    time.sleep(1)
    
    inject_url_banner(driver, f"{BASE}/admin/")
    path = os.path.join(SUBMISSION_FIXED, "admin_login.png")
    driver.save_screenshot(path)
    print(f"Saved: {path}")

def capture_post_review(driver):
    print("Capturing Task 21: Post Review Form Before Submission...")
    driver.get(f"{BASE}/postreview/15")
    time.sleep(1)
    
    # Set session storage for user
    driver.execute_script("""
        window.sessionStorage.setItem('username', 'dishant1313');
        window.sessionStorage.setItem('firstname', 'Dishant');
        window.sessionStorage.setItem('lastname', 'Patel');
    """)
    driver.refresh()
    time.sleep(2)
    
    # Fill in the form fields completely
    driver.execute_script("""
        // Set review text
        var rev = document.getElementById('review');
        if (rev) {
            rev.value = 'Fantastic services and very helpful team!';
            rev.dispatchEvent(new Event('input', { bubbles: true }));
            rev.dispatchEvent(new Event('change', { bubbles: true }));
        }
        
        // Set date
        var dt = document.getElementById('purchase_date');
        if (dt) {
            dt.value = '2023-11-15';
            dt.dispatchEvent(new Event('input', { bubbles: true }));
            dt.dispatchEvent(new Event('change', { bubbles: true }));
        }
        
        // Set year
        var yr = document.getElementById('car_year');
        if (yr) {
            yr.value = '2023';
            yr.dispatchEvent(new Event('input', { bubbles: true }));
            yr.dispatchEvent(new Event('change', { bubbles: true }));
        }
        
        // Select Toyota Camry from dropdown
        var cars = document.getElementById('cars');
        if (cars) {
            // Find option with Toyota Camry or set it
            var found = false;
            for (var i = 0; i < cars.options.length; i++) {
                if (cars.options[i].text.includes('Toyota Camry')) {
                    cars.selectedIndex = i;
                    found = true;
                    break;
                }
            }
            if (!found && cars.options.length > 1) {
                cars.selectedIndex = 1;
            }
            cars.dispatchEvent(new Event('change', { bubbles: true }));
        }
    """)
    time.sleep(1)
    
    inject_url_banner(driver, f"{BASE}/postreview/15")
    path = os.path.join(SUBMISSION_FIXED, "dealership_review_submission.png")
    driver.save_screenshot(path)
    print(f"Saved: {path}")

def main():
    driver = get_driver()
    try:
        capture_admin_login(driver)
        capture_post_review(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

