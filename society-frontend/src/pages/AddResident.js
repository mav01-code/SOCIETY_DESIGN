import { useState } from "react";

function AddResident() {
  const [username, setUsername] = useState("");
  const [name, setName] = useState("");
  const [authorization, setAuthorization] = useState("");
  const [totalFamilyMembers, setTotalFamilyMembers] = useState("");
  const [message, setMessage] = useState("");

  const handleAddResident = async (e) => {
    e.preventDefault();

    try {
      const res = await fetch(
        `http://127.0.0.1:8000/residents/?username=${username}`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            name,
            authorization,
            total_family_members: Number(totalFamilyMembers),
          }),
        }
      );

      if (!res.ok) {
        setMessage("Failed to add resident");
        return;
      }

      const data = await res.json();
      setMessage(`Resident added: ${data.name} (${data.block}-${data.flat_number})`);
      setUsername("");
      setName("");
      setAuthorization("");
      setTotalFamilyMembers("");
    } catch (err) {
      setMessage("Error adding resident");
    }
  };

  return (
    <div style={{
      maxWidth: "400px",
      margin: "40px auto",
      padding: "20px",
      borderRadius: "12px",
      backgroundColor: "#DDaEDD",
      boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
    }}>
      <h2 style={{ color: "#213C51", textAlign: "center", marginBottom: "20px" }}>Add Resident</h2>
      <form onSubmit={handleAddResident} style={{ display: "flex", flexDirection: "column", gap: "15px" }}>
        <input
          placeholder="Block-Flat (e.g., A-101)"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
          style={{
            padding: "10px",
            borderRadius: "8px",
            border: "1px solid #6594B1",
            outline: "none",
            backgroundColor: "#FFFFFF",
            color: "#213C51"
          }}
        />
        <input
          placeholder="Resident Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
          style={{
            padding: "10px",
            borderRadius: "8px",
            border: "1px solid #6594B1",
            outline: "none",
            backgroundColor: "#FFFFFF",
            color: "#213C51"
          }}
        />
        <input
          placeholder="Authorization"
          value={authorization}
          onChange={(e) => setAuthorization(e.target.value)}
          required
          style={{
            padding: "10px",
            borderRadius: "8px",
            border: "1px solid #6594B1",
            outline: "none",
            backgroundColor: "#FFFFFF",
            color: "#213C51"
          }}
        />
        <input
          type="number"
          placeholder="Total Family Members"
          value={totalFamilyMembers}
          onChange={(e) => setTotalFamilyMembers(e.target.value)}
          required
          style={{
            padding: "10px",
            borderRadius: "8px",
            border: "1px solid #6594B1",
            outline: "none",
            backgroundColor: "#FFFFFF",
            color: "#213C51"
          }}
        />
        <button
          type="submit"
          style={{
            padding: "10px",
            borderRadius: "8px",
            border: "none",
            backgroundColor: "#213C51",
            color: "#FFFFFF",
            fontWeight: "bold",
            cursor: "pointer",
            transition: "0.3s",
          }}
          onMouseOver={(e) => e.currentTarget.style.backgroundColor = "#6594B1"}
          onMouseOut={(e) => e.currentTarget.style.backgroundColor = "#213C51"}
        >
          Add Resident
        </button>
      </form>

      {message && (
        <p style={{
          marginTop: "20px",
          textAlign: "center",
          color: "#213C51",
          fontWeight: "500"
        }}>
          {message}
        </p>
      )}
    </div>
  );
}

export default AddResident;
