import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import "./Dealers.css";
import "../assets/style.css";
import Header from '../Header/Header';

const PostReview = () => {
  const [dealer, setDealer] = useState({});
  const [review, setReview] = useState("");
  const [model, setModel] = useState("");
  const [year, setYear] = useState("");
  const [date, setDate] = useState("");
  const [carmodels, setCarmodels] = useState([]);

  const params = useParams();
  const id = params.id;
  const dealer_url = `/djangoapp/dealer/${id}`;
  const review_url = `/djangoapp/add_review`;
  const carmodels_url = `/djangoapp/get_cars`;

  const postreview = async () => {
    let name = (sessionStorage.getItem("firstname") || "") + " " + (sessionStorage.getItem("lastname") || "");
    name = name.trim();
    if (!name || name.includes("null")) {
      name = sessionStorage.getItem("username") || "Verified Customer";
    }

    if (!model || review === "" || date === "" || year === "") {
      alert("All details are mandatory");
      return;
    }

    const model_split = model.split(" ");
    const make_chosen = model_split[0];
    const model_chosen = model_split.slice(1).join(" ");

    const payload = {
      name: name,
      dealership: parseInt(id, 10),
      review: review,
      purchase: true,
      purchase_date: date,
      car_make: make_chosen,
      car_model: model_chosen,
      car_year: parseInt(year, 10),
    };

    try {
      const res = await fetch(review_url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      const json = await res.json();
      if (json.status === 200) {
        window.location.href = window.location.origin + `/dealer/${id}`;
      } else {
        alert("Failed to submit review: " + (json.message || "Unknown error"));
      }
    } catch (err) {
      console.error("Error submitting review:", err);
      alert("Error submitting review. Please try again.");
    }
  };

  const get_dealer = async () => {
    try {
      const res = await fetch(dealer_url, { method: "GET" });
      const retobj = await res.json();
      if (retobj.status === 200 && retobj.dealer) {
        const dealerobjs = Array.isArray(retobj.dealer) ? retobj.dealer : [retobj.dealer];
        if (dealerobjs.length > 0) {
          setDealer(dealerobjs[0]);
        }
      }
    } catch (err) {
      console.error("Error fetching dealer:", err);
    }
  };

  const get_cars = async () => {
    try {
      const res = await fetch(carmodels_url, { method: "GET" });
      const retobj = await res.json();
      if (retobj.CarModels) {
        setCarmodels(Array.from(retobj.CarModels));
      }
    } catch (err) {
      console.error("Error fetching car models:", err);
    }
  };

  useEffect(() => {
    get_dealer();
    get_cars();
  }, [id]);

  return (
    <div>
      <Header />
      <div style={{ margin: "40px auto", maxWidth: "700px", padding: "0 20px" }}>
        <div className="card p-4 shadow-sm" style={{ borderRadius: "16px", border: "1px solid #E2E8F0" }}>
          <h2 style={{ color: "#0F172A", fontWeight: "700", marginBottom: "8px" }}>
            Review: {dealer.full_name || "Dealership"}
          </h2>
          <p style={{ color: "#64748B", marginBottom: "25px" }}>
            Share your authentic purchase or service experience with our community.
          </p>

          <div style={{ marginBottom: "20px" }}>
            <label htmlFor="review" style={{ display: "block", fontWeight: "600", color: "#0F172A", marginBottom: "6px" }}>
              Your Review Experience
            </label>
            <textarea
              id="review"
              className="form-control"
              rows="5"
              placeholder="Write your honest review here... (e.g. Fantastic services and very helpful team!)"
              onChange={(e) => setReview(e.target.value)}
              style={{ borderRadius: "10px", borderColor: "#CBD5E1" }}
            ></textarea>
          </div>

          <div className="row g-3" style={{ marginBottom: "25px" }}>
            <div className="col-md-4">
              <label htmlFor="purchase_date" style={{ display: "block", fontWeight: "600", color: "#0F172A", marginBottom: "6px" }}>
                Purchase Date
              </label>
              <input
                id="purchase_date"
                type="date"
                className="form-control"
                onChange={(e) => setDate(e.target.value)}
                style={{ borderRadius: "10px" }}
              />
            </div>

            <div className="col-md-5">
              <label htmlFor="cars" style={{ display: "block", fontWeight: "600", color: "#0F172A", marginBottom: "6px" }}>
                Car Make & Model
              </label>
              <select
                id="cars"
                name="cars"
                className="form-select"
                defaultValue=""
                onChange={(e) => setModel(e.target.value)}
                style={{ borderRadius: "10px" }}
              >
                <option value="" disabled hidden>Choose Make & Model</option>
                {carmodels.map((carmodel, idx) => (
                  <option key={idx} value={`${carmodel.CarMake} ${carmodel.CarModel}`}>
                    {carmodel.CarMake} {carmodel.CarModel}
                  </option>
                ))}
              </select>
            </div>

            <div className="col-md-3">
              <label htmlFor="car_year" style={{ display: "block", fontWeight: "600", color: "#0F172A", marginBottom: "6px" }}>
                Car Year
              </label>
              <input
                id="car_year"
                type="number"
                className="form-control"
                min="2015"
                max="2023"
                placeholder="2023"
                onChange={(e) => setYear(e.target.value)}
                style={{ borderRadius: "10px" }}
              />
            </div>
          </div>

          <div>
            <button
              className="btn btn-navy-primary w-100 py-2 fs-6 fw-semibold"
              onClick={postreview}
              style={{ borderRadius: "10px" }}
            >
              Post Review
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default PostReview;
