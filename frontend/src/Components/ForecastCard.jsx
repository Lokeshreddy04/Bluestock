import { useEffect, useState } from "react";
import api from "../api/api";



const formatNumber = (value) => {

  if (!value) {
    return "0";
  }

  return new Intl.NumberFormat(
    "en-IN",
    {
      maximumFractionDigits: 0,
    }
  ).format(value);

};
function ForecastCard({ symbol }) {
  
  const [forecast, setForecast] =
    useState(null);

  useEffect(() => {

    api
      .get(`/forecast/${symbol}/`)
      .then((res) => {
        setForecast(res.data);
      });

  }, [symbol]);

  if (!forecast) return null;

  return (
  <div className="card">

    <h3>
      Forecast Revenue
    </h3>

    <p>
      ₹{
        formatNumber(
          forecast.forecast_sales
        )
      }
    </p>

  </div>
);
} 
export default ForecastCard;