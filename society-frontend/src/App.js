import { Routes, Route, Navigate, useNavigate } from "react-router-dom";
import { useState } from "react";
import Login from "./pages/Login";
import Register from "./pages/Register";
import AddResident from "./pages/AddResident";
import GenerateGatePass from "./pages/GenerateGatePass";
import "./App.css";

function App() {
  const [user, setUser] = useState(
    JSON.parse(localStorage.getItem("user"))
  );

  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("user");
    setUser(null);
    navigate("/login");
  };

  if (!user) {
    return (
      <Routes>
        <Route path="/" element={<Navigate to="/login" />} />
        <Route path="/login" element={<Login onLogin={setUser} />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    );
  }

  return (
    <div className="app-container">
      <div className="dashboard-card">
        <h2 className="welcome">
          Welcome {user.username}
          <span className="role">({user.role})</span>
        </h2>

        <div className="action-buttons">
          <button onClick={() => navigate("/add-resident")}>
            Add Resident
          </button>
          <button onClick={() => navigate("/gate-pass")}>
            Generate Gate Pass
          </button>
        </div>

        <button className="logout-btn" onClick={handleLogout}>
          Logout
        </button>
      </div>

      <div className="page-content">
        <Routes>
          <Route path="/add-resident" element={<AddResident />} />
          <Route path="/gate-pass" element={<GenerateGatePass />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
