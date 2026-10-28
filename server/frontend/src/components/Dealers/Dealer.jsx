import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import "./Dealers.css";
import "../assets/style.css";
import positive_icon from "../assets/positive.png";
import neutral_icon from "../assets/neutral.png";
import negative_icon from "../assets/negative.png";
import review_icon from "../assets/reviewbutton.png";
import Header from '../Header/Header';

const Dealer = () => {
  const [dealer, setDealer] = useState({});
  const [reviews, setReviews] = useState([]);
  const [unreviewed, setUnreviewed] = useState(false);
  const [postReview, setPostReview] = useState(<></>);

  const params = useParams();
  const id = params.id;
  const dealer_url = `/djangoapp/dealer/${id}`;
  const reviews_url = `/djangoapp/reviews/dealer/${id}`;
  const post_review_url = `/postreview/${id}`;

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

  const get_reviews = async () => {
    try {
      const res = await fetch(reviews_url, { method: "GET" });
      const retobj = await res.json();
      if (retobj.status === 200 && retobj.reviews) {
        if (retobj.reviews.length > 0) {
          setReviews(retobj.reviews);
        } else {
          setUnreviewed(true);
        }
      } else {
        setUnreviewed(true);
      }
    } catch (err) {
      console.error("Error fetching reviews:", err);
      setUnreviewed(true);
    }
  };

  const senti_icon = (sentiment) => {
    if (sentiment === "positive") return positive_icon;
    if (sentiment === "negative") return negative_icon;
    return neutral_icon;
  };

  useEffect(() => {
    get_dealer();
    get_reviews();
    if (sessionStorage.getItem("username")) {
      setPostReview(
        <a href={post_review_url} style={{ textDecoration: "none", marginLeft: "15px" }}>
          <img
            src={review_icon}
            style={{ width: "140px", verticalAlign: "middle" }}
            alt="Post Review"
          />
        </a>
      );
    }
  }, [id]);

  return (
    <div>
      <Header />
      <div style={{ margin: "30px 50px" }}>
        <div style={{ marginBottom: "25px" }}>
          <h1 style={{ color: "#0F172A", fontWeight: "700", display: "inline-flex", alignItems: "center" }}>
            {dealer.full_name || "Dealership Details"}
            {postReview}
          </h1>
          <h4 style={{ color: "#64748B", fontWeight: "400", marginTop: "8px" }}>
            {dealer.city}, {dealer.address}, Zip - {dealer.zip}, {dealer.state}
          </h4>
        </div>

        <h3 style={{ color: "#0F172A", fontWeight: "600", marginBottom: "20px" }}>Customer Reviews</h3>

        <div className="reviews_panel">
          {reviews.length === 0 && !unreviewed ? (
            <div style={{ color: "#64748B", padding: "20px" }}>Loading Reviews...</div>
          ) : unreviewed || reviews.length === 0 ? (
            <div style={{ color: "#64748B", padding: "20px", fontStyle: "italic" }}>
              No reviews yet for this dealership! Be the first to share your experience.
            </div>
          ) : (
            reviews.map((review, index) => (
              <div key={review.id || index} className="review_panel">
                <img src={senti_icon(review.sentiment)} className="emotion_icon" alt={`Sentiment: ${review.sentiment}`} />
                <div className="review">{review.review}</div>
                <div className="reviewer">
                  <strong>{review.name}</strong>
                  {review.purchase && review.car_make && (
                    <span> — {review.car_year} {review.car_make} {review.car_model}</span>
                  )}
                  {review.purchase_date && (
                    <span style={{ color: "#94A3B8", marginLeft: "8px" }}>({review.purchase_date})</span>
                  )}
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
};

export default Dealer;
