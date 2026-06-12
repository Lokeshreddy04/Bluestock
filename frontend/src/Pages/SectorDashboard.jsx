import { useEffect, useState } from "react";
import api from "../api/api";

function SectorDashboard() {

  const [sectors, setSectors] = useState([]);
  const [selectedSector, setSelectedSector] = useState("");
  const [data, setData] = useState(null);
  const [loading, setLoading] =
  useState(false);

const [error, setError] =
  useState(false);

  useEffect(() => {

    api
      .get("/sectors/")
      .then((res) => {
        setSectors(res.data);
      });

  }, []);

  const loadSector = async (
  sector
) => {

  setLoading(true);

  try {

    const res =
      await api.get(
        `/sectors/${sector}/`
      );

    setData(res.data);

  } catch (err) {

    setError(true);

  }

  setLoading(false);

};

if (loading) {
  return (
    <h2>
      Loading Sector...
    </h2>
  );
}

if (error) {
  return (
    <h2>
      Something went wrong
    </h2>
  );
}

  return (
    <div>

      <h1>Sector Analytics</h1>

      <div>

        {sectors.map((sector) => (

          <button
            key={sector}
            onClick={() => loadSector(sector)}
          >
            {sector}
          </button>

        ))}

      </div>

      {data && (

        <div>

          <h2>{data.sector}</h2>

          <p>
            Companies:
            {data.company_count}
          </p>

          <p>
            Avg Revenue:
            {data.avg_revenue}
          </p>

          <p>
            Avg Profit:
            {data.avg_profit}
          </p>

          <p>
            Avg Health:
            {data.avg_health_score}
          </p>

        </div>

      )}

    </div>
  );
}

export default SectorDashboard;