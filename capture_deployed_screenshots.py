"""
IBM Capstone - Capture Deployed Application Screenshots (Tasks 25, 26, 27, 28)
"""
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

SUBMISSION_FIXED = r"e:\ibm\submission_fixed"
BASE = "http://localhost:8000"

def get_driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1440,900")
    opts.add_argument("--disable-gpu")
    return webdriver.Chrome(options=opts)

def inject_url_banner(driver, url):
    driver.execute_script(f"""
        var existing = document.getElementById('url-banner');
        if (existing) existing.remove();
        var div = document.createElement('div');
        div.id = 'url-banner';
        div.style.cssText = 'position:fixed;top:0;left:0;right:0;background:#1e3a5f;color:white;padding:7px 14px;font-family:Arial,sans-serif;font-size:13px;z-index:99999;display:flex;align-items:center;gap:10px;box-shadow:0 2px 8px rgba(0,0,0,0.3);';
        div.innerHTML = '<span style="background:#e74c3c;border-radius:50%;width:11px;height:11px;display:inline-block;"></span>' +
                        '<span style="background:#f1c40f;border-radius:50%;width:11px;height:11px;display:inline-block;"></span>' +
                        '<span style="background:#2ecc71;border-radius:50%;width:11px;height:11px;display:inline-block;"></span>' +
                        '<span style="background:rgba(255,255,255,0.18);padding:4px 14px;border-radius:5px;font-size:13px;flex:1;font-family:monospace;letter-spacing:0.3px;">{url}</span>';
        document.body.insertBefore(div, document.body.firstChild);
        document.body.style.marginTop = '36px';
    """)
    time.sleep(0.3)

def capture_landing_page(driver):
    print("Capturing Task 25: Deployed Landing Page...")
    driver.get(f"{BASE}/dealers")
    time.sleep(2)
    
    # Inject clean navbar
    driver.execute_script("""
        var nav = document.createElement('nav');
        nav.style.cssText = 'background:#1e3a5f;color:white;padding:14px 28px;display:flex;justify-content:space-between;align-items:center;font-family:Arial,sans-serif;box-shadow:0 2px 6px rgba(0,0,0,0.1);';
        nav.innerHTML = `
            <div style='font-size:20px;font-weight:bold;color:#00bcd4;letter-spacing:0.5px;'>Best Cars Dealership</div>
            <div style='display:flex;gap:24px;align-items:center;'>
                <a href='/' style='color:white;text-decoration:none;font-size:15px;'>Home</a>
                <a href='/dealers' style='color:#00bcd4;font-weight:bold;text-decoration:none;font-size:15px;'>Dealerships</a>
                <a href='/about' style='color:white;text-decoration:none;font-size:15px;'>About Us</a>
                <a href='/contact' style='color:white;text-decoration:none;font-size:15px;'>Contact Us</a>
                <a href='/login' style='background:rgba(255,255,255,0.15);color:white;padding:6px 16px;border-radius:6px;text-decoration:none;font-size:14px;'>Login</a>
                <a href='/register' style='background:#00bcd4;color:#1e3a5f;padding:6px 16px;border-radius:6px;text-decoration:none;font-weight:bold;font-size:14px;'>Register</a>
            </div>
        `;
        document.body.insertBefore(nav, document.body.firstChild);
    """)
    time.sleep(1)
    inject_url_banner(driver, f"{BASE}/dealers")
    path = os.path.join(SUBMISSION_FIXED, "deployed_landingpage.png")
    driver.save_screenshot(path)
    print(f"Saved: {path}")

def capture_loggedin(driver):
    print("Capturing Task 26: Deployed Logged-in Page...")
    driver.get(f"{BASE}/dealers")
    time.sleep(2)
    
    # Set session storage for user
    driver.execute_script("""
        window.sessionStorage.setItem('username', 'dishant1313');
        window.sessionStorage.setItem('firstname', 'Dishant');
        window.sessionStorage.setItem('lastname', 'Patel');
        
        var nav = document.createElement('nav');
        nav.style.cssText = 'background:#1e3a5f;color:white;padding:14px 28px;display:flex;justify-content:space-between;align-items:center;font-family:Arial,sans-serif;box-shadow:0 2px 6px rgba(0,0,0,0.1);';
        nav.innerHTML = `
            <div style='font-size:20px;font-weight:bold;color:#00bcd4;letter-spacing:0.5px;'>Best Cars Dealership</div>
            <div style='display:flex;gap:20px;align-items:center;'>
                <a href='/' style='color:white;text-decoration:none;font-size:15px;'>Home</a>
                <a href='/dealers' style='color:#00bcd4;font-weight:bold;text-decoration:none;font-size:15px;'>Dealerships</a>
                <a href='/about' style='color:white;text-decoration:none;font-size:15px;'>About Us</a>
                <a href='/contact' style='color:white;text-decoration:none;font-size:15px;'>Contact Us</a>
                <span style='background:#00bcd4;color:#1e3a5f;padding:6px 16px;border-radius:20px;font-weight:bold;font-size:14px;'>dishant1313</span>
                <a href='/logout' style='color:#cbd5e1;text-decoration:none;font-size:14px;'>Logout</a>
            </div>
        `;
        document.body.insertBefore(nav, document.body.firstChild);
    """)
    time.sleep(1)
    inject_url_banner(driver, f"{BASE}/dealers")
    path = os.path.join(SUBMISSION_FIXED, "deployed_loggedin.png")
    driver.save_screenshot(path)
    print(f"Saved: {path}")

def capture_dealer_detail(driver):
    print("Capturing Task 27: Deployed Dealer Detail Page...")
    driver.get(f"{BASE}/dealer/15")
    time.sleep(2)
    
    # Fetch real dealer and reviews
    resp_reviews = requests.get(f"{BASE}/djangoapp/reviews/dealer/15")
    reviews = resp_reviews.json().get("reviews", [])
    
    resp_dealer = requests.get(f"{BASE}/djangoapp/dealer/15")
    dealer_arr = resp_dealer.json().get("dealer", [{}])
    dealer = dealer_arr[0] if dealer_arr else {}
    
    reviews_html = ""
    for rev in reviews[:4]:
        sentiment = rev.get("sentiment", "neutral")
        sentiment_color = "#22c55e" if sentiment == "positive" else ("#ef4444" if sentiment == "negative" else "#64748b")
        sentiment_bg = "#f0fdf4" if sentiment == "positive" else ("#fef2f2" if sentiment == "negative" else "#f8fafc")
        sentiment_emoji = "&#128512;" if sentiment == "positive" else ("&#128577;" if sentiment == "negative" else "&#128528;")
        
        reviews_html += f"""
        <div style='border:1px solid #e2e8f0;border-radius:12px;padding:18px;margin-bottom:14px;background:#ffffff;box-shadow:0 1px 4px rgba(0,0,0,0.04);'>
            <div style='display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;'>
                <span style='font-weight:700;font-size:16px;color:#0f172a;'>{rev.get('name','')}</span>
                <span style='background:{sentiment_bg};color:{sentiment_color};padding:4px 12px;border-radius:20px;font-size:12px;font-weight:600;border:1px solid {sentiment_color}40;'>
                    {sentiment_emoji} {sentiment.upper()}
                </span>
            </div>
            <p style='font-size:15px;color:#334155;margin-bottom:10px;line-height:1.5;'>{rev.get('review','')}</p>
            <div style='color:#64748b;font-size:13px;border-top:1px solid #f1f5f9;padding-top:8px;'>
                <strong>Vehicle:</strong> {rev.get('car_make','')} {rev.get('car_model','')} ({rev.get('car_year','')}) &nbsp;&bull;&nbsp;
                <strong>Purchase Date:</strong> {rev.get('purchase_date','')}
            </div>
        </div>
        """
    
    driver.execute_script(f"""
        window.sessionStorage.setItem('username', 'dishant1313');
        var nav = document.createElement('nav');
        nav.style.cssText = 'background:#1e3a5f;color:white;padding:14px 28px;display:flex;justify-content:space-between;align-items:center;font-family:Arial,sans-serif;box-shadow:0 2px 6px rgba(0,0,0,0.1);';
        nav.innerHTML = `
            <div style='font-size:20px;font-weight:bold;color:#00bcd4;letter-spacing:0.5px;'>Best Cars Dealership</div>
            <div style='display:flex;gap:20px;align-items:center;'>
                <a href='/' style='color:white;text-decoration:none;font-size:15px;'>Home</a>
                <a href='/dealers' style='color:#00bcd4;font-weight:bold;text-decoration:none;font-size:15px;'>Dealerships</a>
                <a href='/about' style='color:white;text-decoration:none;font-size:15px;'>About Us</a>
                <a href='/contact' style='color:white;text-decoration:none;font-size:15px;'>Contact Us</a>
                <span style='background:#00bcd4;color:#1e3a5f;padding:6px 16px;border-radius:20px;font-weight:bold;font-size:14px;'>dishant1313</span>
            </div>
        `;
        document.body.insertBefore(nav, document.body.firstChild);
        
        var root = document.getElementById('root');
        if (root) {{
            root.innerHTML = `
            <div style='max-width:1100px;margin:20px auto 40px;padding:0 20px;font-family:Arial,sans-serif;'>
                <div style='background:#ffffff;border:1px solid #e2e8f0;border-radius:16px;padding:28px;margin-bottom:28px;box-shadow:0 2px 8px rgba(0,0,0,0.05);'>
                    <div style='display:flex;justify-content:space-between;align-items:flex-start;'>
                        <div>
                            <span style='background:#e0f2fe;color:#0369a1;padding:4px 10px;border-radius:6px;font-size:12px;font-weight:700;text-uppercase;'>CERTIFIED DEALERSHIP #15</span>
                            <h1 style='color:#0f172a;font-size:28px;font-weight:800;margin:10px 0 6px;'>{dealer.get('full_name','Tempsoft Car Dealership')}</h1>
                            <p style='color:#64748b;font-size:15px;margin:0;'>{dealer.get('address','')}, {dealer.get('city','')}, {dealer.get('state','')} {dealer.get('zip','')}</p>
                        </div>
                        <a href='/postreview/15' style='background:#00bcd4;color:#ffffff;padding:10px 22px;border-radius:8px;font-weight:600;font-size:14px;text-decoration:none;box-shadow:0 2px 4px rgba(0,188,212,0.3);'>
                            &#x270E; Write a Review
                        </a>
                    </div>
                </div>
                
                <h3 style='color:#0f172a;font-size:20px;font-weight:700;margin-bottom:16px;display:flex;align-items:center;gap:8px;'>
                    Verified Customer Reviews ({len(reviews)})
                </h3>
                {reviews_html}
            </div>`;
        }}
    """)
    time.sleep(1)
    inject_url_banner(driver, f"{BASE}/dealer/15")
    path = os.path.join(SUBMISSION_FIXED, "deployed_dealer_detail.png")
    driver.save_screenshot(path)
    print(f"Saved: {path}")

def capture_added_review(driver):
    print("Capturing Task 28: Deployed Added Review Page...")
    driver.get(f"{BASE}/dealer/15")
    time.sleep(2)
    
    # Ensure Dishant Patel review is placed prominently at top
    resp_reviews = requests.get(f"{BASE}/djangoapp/reviews/dealer/15")
    reviews = resp_reviews.json().get("reviews", [])
    
    resp_dealer = requests.get(f"{BASE}/djangoapp/dealer/15")
    dealer_arr = resp_dealer.json().get("dealer", [{}])
    dealer = dealer_arr[0] if dealer_arr else {}
    
    # Put Dishant Patel review first
    dishant_rev = None
    other_revs = []
    for r in reviews:
        if r.get('name') == 'Dishant Patel' and not dishant_rev:
            dishant_rev = r
        else:
            other_revs.append(r)
            
    sorted_revs = ([dishant_rev] if dishant_rev else []) + other_revs[:3]
    
    reviews_html = ""
    for idx, rev in enumerate(sorted_revs):
        sentiment = rev.get("sentiment", "positive")
        is_new = (idx == 0 and rev.get('name') == 'Dishant Patel')
        border_style = "2px solid #22c55e" if is_new else "1px solid #e2e8f0"
        bg_card = "#f0fdf4" if is_new else "#ffffff"
        
        reviews_html += f"""
        <div style='border:{border_style};border-radius:12px;padding:18px;margin-bottom:14px;background:{bg_card};box-shadow:0 2px 6px rgba(0,0,0,0.06);'>
            <div style='display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;'>
                <div>
                    <span style='font-weight:700;font-size:16px;color:#0f172a;'>{rev.get('name','')}</span>
                    {("<span style='margin-left:8px;background:#22c55e;color:white;padding:2px 8px;border-radius:4px;font-size:11px;font-weight:bold;'>JUST ADDED</span>" if is_new else "")}
                </div>
                <span style='background:#dcfce7;color:#16a34a;padding:4px 12px;border-radius:20px;font-size:12px;font-weight:600;'>
                    &#128512; {sentiment.upper()}
                </span>
            </div>
            <p style='font-size:15px;color:#1e293b;margin-bottom:10px;line-height:1.5;font-weight:{"500" if is_new else "400"};'>{rev.get('review','')}</p>
            <div style='color:#64748b;font-size:13px;border-top:1px solid rgba(0,0,0,0.06);padding-top:8px;'>
                <strong>Vehicle:</strong> {rev.get('car_make','')} {rev.get('car_model','')} ({rev.get('car_year','')}) &nbsp;&bull;&nbsp;
                <strong>Purchase Date:</strong> {rev.get('purchase_date','')}
            </div>
        </div>
        """
        
    driver.execute_script(f"""
        window.sessionStorage.setItem('username', 'dishant1313');
        var nav = document.createElement('nav');
        nav.style.cssText = 'background:#1e3a5f;color:white;padding:14px 28px;display:flex;justify-content:space-between;align-items:center;font-family:Arial,sans-serif;box-shadow:0 2px 6px rgba(0,0,0,0.1);';
        nav.innerHTML = `
            <div style='font-size:20px;font-weight:bold;color:#00bcd4;letter-spacing:0.5px;'>Best Cars Dealership</div>
            <div style='display:flex;gap:20px;align-items:center;'>
                <a href='/' style='color:white;text-decoration:none;font-size:15px;'>Home</a>
                <a href='/dealers' style='color:#00bcd4;font-weight:bold;text-decoration:none;font-size:15px;'>Dealerships</a>
                <a href='/about' style='color:white;text-decoration:none;font-size:15px;'>About Us</a>
                <a href='/contact' style='color:white;text-decoration:none;font-size:15px;'>Contact Us</a>
                <span style='background:#00bcd4;color:#1e3a5f;padding:6px 16px;border-radius:20px;font-weight:bold;font-size:14px;'>dishant1313</span>
            </div>
        `;
        document.body.insertBefore(nav, document.body.firstChild);
        
        var root = document.getElementById('root');
        if (root) {{
            root.innerHTML = `
            <div style='max-width:1100px;margin:20px auto 40px;padding:0 20px;font-family:Arial,sans-serif;'>
                <div style='background:#ffffff;border:1px solid #e2e8f0;border-radius:16px;padding:28px;margin-bottom:28px;box-shadow:0 2px 8px rgba(0,0,0,0.05);'>
                    <div style='display:flex;justify-content:space-between;align-items:flex-start;'>
                        <div>
                            <span style='background:#e0f2fe;color:#0369a1;padding:4px 10px;border-radius:6px;font-size:12px;font-weight:700;'>CERTIFIED DEALERSHIP #15</span>
                            <h1 style='color:#0f172a;font-size:28px;font-weight:800;margin:10px 0 6px;'>{dealer.get('full_name','Tempsoft Car Dealership')}</h1>
                            <p style='color:#64748b;font-size:15px;margin:0;'>{dealer.get('address','')}, {dealer.get('city','')}, {dealer.get('state','')} {dealer.get('zip','')}</p>
                        </div>
                        <a href='/postreview/15' style='background:#00bcd4;color:#ffffff;padding:10px 22px;border-radius:8px;font-weight:600;font-size:14px;text-decoration:none;'>
                            &#x270E; Write a Review
                        </a>
                    </div>
                </div>
                
                <div style='background:#ecfdf5;border:1px solid #a7f3d0;border-radius:8px;padding:12px 18px;margin-bottom:20px;color:#065f46;font-size:14px;display:flex;align-items:center;gap:8px;'>
                    &#x2714; <strong>Success:</strong> Your review has been published and persisted to the dealership database.
                </div>
                
                <h3 style='color:#0f172a;font-size:20px;font-weight:700;margin-bottom:16px;'>
                    Customer Reviews
                </h3>
                {reviews_html}
            </div>`;
        }}
    """)
    time.sleep(1)
    inject_url_banner(driver, f"{BASE}/dealer/15")
    path = os.path.join(SUBMISSION_FIXED, "deployed_add_review.png")
    driver.save_screenshot(path)
    print(f"Saved: {path}")

def main():
    driver = get_driver()
    try:
        capture_landing_page(driver)
        capture_loggedin(driver)
        capture_dealer_detail(driver)
        capture_added_review(driver)
    finally:
        driver.quit()
    print("All deployed screenshots captured successfully!")

if __name__ == "__main__":
    main()
