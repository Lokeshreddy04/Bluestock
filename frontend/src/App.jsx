import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import Home from "./Pages/Home";
import CompanyDashboard from "./Pages/CompanyDashboard";
import SectorDashboard
from "./Pages/SectorDashboard";

function App() {

  return (
    <BrowserRouter>

      <Routes>

        <Route
          path="/"
          element={<Home />}
        />

        <Route
          path="/company/:symbol"
          element={<CompanyDashboard />}
        />
        <Route
  path="/sectors"
  element={<SectorDashboard />}
/>

      </Routes>

    </BrowserRouter>
  );
}

export default App;