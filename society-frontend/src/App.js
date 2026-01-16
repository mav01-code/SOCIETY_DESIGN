import { useState } from "react";
import Register from "./pages/Register";
import Login from "./pages/Login";

function App() {
  const [user, setUser] = useState(
    JSON.parse(localStorage.getItem("user"))
  );
  const [showLogin, setShowLogin] = useState(true);

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

  return <h2>Welcome {user.username} ({user.role})</h2>;
}

export default App;
