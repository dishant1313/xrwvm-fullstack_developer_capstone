import React from 'react';
import "../assets/style.css";
import "../assets/bootstrap.min.css";

const Header = () => {
  const logout = async (e) => {
    e.preventDefault();
    let logout_url = window.location.origin + "/djangoapp/logout";
    try {
      const res = await fetch(logout_url, {
        method: "GET",
      });
      const json = await res.json();
      if (json) {
        let username = sessionStorage.getItem('username');
        sessionStorage.removeItem('username');
        sessionStorage.removeItem('firstname');
        sessionStorage.removeItem('lastname');
        window.location.href = window.location.origin;
      } else {
        alert("The user could not be logged out.");
      }
    } catch (err) {
      console.error("Logout error:", err);
      sessionStorage.removeItem('username');
      window.location.href = window.location.origin;
    }
  };

  let curr_user = sessionStorage.getItem('username');

  let home_page_items = (
    <div className="loginlink" style={{ display: "flex", alignItems: "center" }}>
      <a className="btn-nav-action" href="/login">Login</a>
      <a className="btn-nav-action" href="/register">Register</a>
    </div>
  );

  if (curr_user !== null && curr_user !== "") {
    home_page_items = (
      <div className="loginlink" style={{ display: "flex", alignItems: "center" }}>
        <span className="username-display">{curr_user}</span>
        <a className="btn-nav-action" href="/djangoapp/logout" onClick={logout}>Logout</a>
      </div>
    );
  }

  return (
    <div>
      <nav className="navbar navbar-expand-lg navbar-dark dealership-navbar">
        <div className="container-fluid px-4">
          <a className="navbar-brand brand-title" href="/">Dealerships</a>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarText">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
              <li className="nav-item">
                <a className="nav-link" href="/">Home</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="/dealers">Dealerships</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="/about">About Us</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="/contact">Contact Us</a>
              </li>
            </ul>
            <span className="navbar-text">
              <div id="loginlogout">
                {home_page_items}
              </div>
            </span>
          </div>
        </div>
      </nav>
    </div>
  );
};

export default Header;
