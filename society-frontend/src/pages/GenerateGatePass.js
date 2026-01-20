import { useState } from "react";

function GenerateGatePass() {
  const [username, setUsername] = useState("");
  const [gatepass, setGatepass] = useState(null);
  const [error, setError] = useState("");

  const handleGenerate = async (e) => {
    e.preventDefault();

    try {
      const [block, flat_number] = username.trim().split("-");
      if (!block || !flat_number) {
        setError("Enter valid Block-Flat (e.g., A-101)");
        return;
      }

      const now = new Date();
      const validUntil = new Date();
      validUntil.setHours(validUntil.getHours() + 2); // valid 2 hours

      const res = await fetch("http://127.0.0.1:8000/gatepass/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          block,
          flat_number,
          valid_from: now.toISOString(),
          valid_until: validUntil.toISOString()
        })
      });

      if (!res.ok) {
        setError("Failed to generate gate pass");
        return;
      }

      const data = await res.json();
      setGatepass(data);
      setError("");
    } catch (err) {
      setError("Error generating gate pass");
    }
  };

  return (
    <div>
      <h2>Generate Gate Pass</h2>
      <form onSubmit={handleGenerate}>
        <input
          placeholder="Block-Flat (e.g., A-101)"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <button type="submit">Generate</button>
      </form>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {gatepass && (
        <div style={{ marginTop: "20px" }}>
          <h3>Gate Pass</h3>
          <p>Block: {gatepass.block}</p>
          <p>Flat: {gatepass.flat_number}</p>
          <p>Pass ID: {gatepass.pass_id}</p>
          <p>Valid Until: {new Date(gatepass.valid_until).toLocaleString()}</p>

          <h4>QR Code:</h4>
          <img
            src={gatepass.qr_url} // <- use qr_url returned from backend
            alt="Gate Pass QR"
            width={200}
            height={200}
          />
        </div>
      )}
    </div>
  );
}

export default GenerateGatePass;
