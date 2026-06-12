import SearchBar from "../components/SearchBar";
import { Link } from "react-router-dom";
function Home() {

  return (
    <div>

    <div className="hero">

  <h1>
    Bluestock Analytics
  </h1>

  <p className="subtitle">

    Financial Analytics
    Platform for
    Indian Listed Companies

  </p>

</div>
      <SearchBar />
<Link to="/sectors">
  Sector Analytics
</Link>
    </div>
  );
}

export default Home;