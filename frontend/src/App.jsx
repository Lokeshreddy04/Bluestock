import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import Home from "./pages/Home";
import CompanyDashboard from "./pages/CompanyDashboard";
import SectorDashboard
from "./pages/SectorDashboard";

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