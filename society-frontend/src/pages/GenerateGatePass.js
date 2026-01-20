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
      validUntil.setHours(validUntil.getHours() + 2);

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
    <div style={{
      maxWidth: "450px",
      margin: "40px auto",
      padding: "25px",
      borderRadius: "12px",
      backgroundColor: "#DDAEDD",
      boxShadow: "0 6px 15px rgba(0,0,0,0.1)"
    }}>
      <h2 style={{ color: "#213C51", textAlign: "center", marginBottom: "20px" }}>
        Generate Gate Pass
      </h2>
      <form onSubmit={handleGenerate} style={{ display: "flex", flexDirection: "column", gap: "15px" }}>
        <input
          placeholder="Block-Flat (e.g., A-101)"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
          style={{
            padding: "12px",
            borderRadius: "8px",
            border: "1px solid #6594B1",
            outline: "none",
            backgroundColor: "#EEEEEE",
            color: "#213C51",
            fontWeight: "500"
          }}
        />
        <button
          type="submit"
          style={{
            padding: "12px",
            borderRadius: "8px",
            border: "none",
            backgroundColor: "#213C51",
            color: "#FFFFFF",
            fontWeight: "bold",
            cursor: "pointer",
            transition: "0.3s"
          }}
          onMouseOver={(e) => e.currentTarget.style.backgroundColor = "#6594B1"}
          onMouseOut={(e) => e.currentTarget.style.backgroundColor = "#213C51"}
        >
          Generate
        </button>
      </form>

      {error && (
        <p style={{
          marginTop: "15px",
          textAlign: "center",
          color: "red",
          fontWeight: "500"
        }}>
          {error}
        </p>
      )}

      {gatepass && (
        <div style={{
          marginTop: "25px",
          padding: "15px",
          borderRadius: "10px",
          backgroundColor: "#EEEEEE",
          textAlign: "center",
          color: "#213C51"
        }}>
          <h3 style={{ marginBottom: "10px" }}>Gate Pass</h3>
          <p><strong>Block:</strong> {gatepass.block}</p>
          <p><strong>Flat:</strong> {gatepass.flat_number}</p>
          <p><strong>Pass ID:</strong> {gatepass.pass_id}</p>
          <p><strong>Valid Until:</strong> {new Date(gatepass.valid_until).toLocaleString()}</p>

          <h4 style={{ marginTop: "15px", marginBottom: "10px" }}>QR Code:</h4>
          <img
            src={gatepass.qr_url}
            alt="Gate Pass QR"
            width={200}
            height={200}
            style={{ borderRadius: "8px", border: "1px solid #6594B1" }}
          />
        </div>
      )}
    </div>
  );
}

export default GenerateGatePass;
