import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/api";

function SearchBar() {

  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  const navigate = useNavigate();

  const handleSearch = async (value) => {

    setQuery(value);

    if (!value) {
      setResults([]);
      return;
    }

    const res = await api.get(
      `/search/?q=${value}`
    );

    setResults(res.data);
  };

 return (
  <div>

    <input
      type="text"
      value={query}
     onChange={(e) => handleSearch(e.target.value)}
      placeholder="Search Company"
    />

    <div className="search-results">

      {results.map((company) => (

        <div
          key={company.symbol}
          className="search-item"
          onClick={() =>
            navigate(
              `/company/${company.symbol}`
            )
          }
        >

          {company.company_name}

        </div>

      ))}

    </div>

  </div>
  );
}

export default SearchBar;