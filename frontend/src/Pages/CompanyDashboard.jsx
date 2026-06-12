import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import api from "../api/api";

import RevenueChart from "../components/RevenueChart";
import PeerCompanies from "../components/PeerCompanies";
import ForecastCard from "../components/ForecastCard";
import "../styles/dashboard.css";



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
function CompanyDashboard() {
  const { symbol } = useParams();

  const [data, setData] = useState(null);
  const [error, setError] = useState(false);

  useEffect(() => {
    api
      .get(`/company-dashboard/${symbol}/`)
      .then((res) => {
        setData(res.data);
      })
      .catch((err) => {
        console.error(err);
        setError(true);
      });
  }, [symbol]);

  if (error) {
    return <h2>Company not found</h2>;
  }

  if (!data) {
    return <h2>Loading Dashboard...</h2>;
  }

  const latestProfitLoss =
    data.profit_loss?.[
      data.profit_loss.length - 1
    ];

  const latestBalanceSheet =
    data.balance_sheet?.[
      data.balance_sheet.length - 1
    ];

  const latestCashFlow =
    data.cash_flow?.[
      data.cash_flow.length - 1
    ];

  return (
    <div className="dashboard-container">

      <h1 className="company-title">
        {data.company.company_name}
      </h1>

      <div className="company-meta">
        Sector: {data.company.sector_name}
      </div>

      {/* KPI Cards */}
      <div className="kpi-grid">

        <div className="card">
          <h3>Revenue</h3>
          <p>
            ₹{
              formatNumber(
                latestProfitLoss?.sales
              )
            }
          </p>
        </div>

        <div className="card">
          <h3>Net Profit</h3>
          <p>
            ₹{
              formatNumber(
                latestProfitLoss?.net_profit
              )
            }
          </p>
        </div>

        <div className="card">
          <h3>Assets</h3>
          <p>
            ₹{
              formatNumber(
                latestBalanceSheet?.total_assets
              )
            }
          </p>
        </div>

        <div className="card">
          <h3>Free Cash Flow</h3>
          <p>
            ₹{
              formatNumber(
                latestCashFlow?.free_cash_flow
              )
            }
          </p>
        </div>

      </div>

      <br />

      {/* Forecast */}
      <ForecastCard
        symbol={symbol}
      />

      <br />

      {/* Revenue Trend */}
      <div className="card">
        <h2>Revenue Trend</h2>

        <RevenueChart
          profitLoss={data.profit_loss}
        />
      </div>

      <br />

      {/* Similar Companies */}
      {/* Similar Companies */}
<PeerCompanies
  symbol={symbol}
/>

<br />

<div className="card health-score">

  <h2>
    Health Score
  </h2>

  <div className="health-value">
    {data.health_score?.score?.toFixed(2)}
  </div>

  <div
    className={`health-label ${
      data.health_score?.label?.toLowerCase()
    }`}
  >
    {data.health_score?.label}
  </div>

</div>
      

    </div>
  );
}

export default CompanyDashboard;