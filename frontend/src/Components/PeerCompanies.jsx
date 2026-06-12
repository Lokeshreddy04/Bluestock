import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/api";

function PeerCompanies({ symbol }) {

  const [peers, setPeers] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {

    api
      .get(`/peers/${symbol}/`)
      .then((res) => {
        setPeers(res.data.peers);
      });

  }, [symbol]);

 return (

  <div className="card">

    <h3>
      Similar Companies
    </h3>

    {
      peers.map((peer) => (

        <div
          key={peer}
          className="peer-item"
          onClick={() =>
            navigate(
              `/company/${peer}`
            )
          }
        >

          ✓ {peer}

        </div>

      ))
    }

  </div>

)
}

export default PeerCompanies;