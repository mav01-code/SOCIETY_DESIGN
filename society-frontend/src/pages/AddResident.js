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
    <div>
      <h2>Add Resident</h2>
      <form onSubmit={handleAddResident}>
        <input
          placeholder="Block-Flat (e.g., A-101)"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <input
          placeholder="Resident Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <input
          placeholder="Authorization"
          value={authorization}
          onChange={(e) => setAuthorization(e.target.value)}
          required
        />
        <input
          type="number"
          placeholder="Total Family Members"
          value={totalFamilyMembers}
          onChange={(e) => setTotalFamilyMembers(e.target.value)}
          required
        />
        <button type="submit">Add Resident</button>
      </form>

      {message && <p>{message}</p>}
    </div>
  );
}

export default AddResident;
