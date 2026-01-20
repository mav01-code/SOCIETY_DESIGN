import { useState } from "react";
import Register from "./pages/Register";
import Login from "./pages/Login";
import AddResident from "./pages/AddResident"; // import your AddResident page

function App() {
  const [user, setUser] = useState(
    JSON.parse(localStorage.getItem("user"))
  );
  const [showLogin, setShowLogin] = useState(true);
  const [currentPage, setCurrentPage] = useState(""); // track dashboard page

  const handleLogout = () => {
    localStorage.removeItem("user");
    setUser(null);
    setCurrentPage("");
  };

  if (!user) {
    return showLogin ? (
      <>
        <Login onLogin={setUser} />
        <button onClick={() => setShowLogin(false)}>Go to Register</button>
      </>
    ) : (
      <>
        <Register />
        <button onClick={() => setShowLogin(true)}>Go to Login</button>
      </>
    );
  }

  // Logged-in dashboard
  return (
    <div>
      <h2>
        Welcome {user.username} ({user.role})
      </h2>

      <button onClick={() => setCurrentPage("addResident")}>
        Add Resident
      </button>

      <button onClick={() => setCurrentPage("gatePass")}>
        Generate Gate Pass
      </button>

      <br />
      <br />

      <button onClick={handleLogout}>Logout</button>

      <div>
        {currentPage === "addResident" && <AddResident />}
        {currentPage === "gatePass" && <p>Gate Pass Page (to implement)</p>}
      </div>
    </div>
  );
}

export default App;
