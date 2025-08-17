import { useState } from "react";

function App() {
  const [length, setLength] = useState("");
  const [rirth, setRirth] = useState("");
  const [result, setResult] = useState("");

  const sendData = async () => {
    const data = { length: Number(length), rirth: Number(rirth) };

    const response = await fetch("http://127.0.0.1:8000/count", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    });

    const resJson = await response.json();
    setResult(resJson.size);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Calculator size</h1>
      length
      <input
        type="number"
        placeholder="Length"
        value={length}
        onChange={(e) => setLength(e.target.value)}
      /> in cm
      <br />

      rirth <input
        type="number"
        placeholder="Rirth"
        value={rirth}
        onChange={(e) => setRirth(e.target.value)}
      /> in mm
      <br />

      <button onClick={sendData}>Send</button>

      {result && <h2>Size: {result}</h2>}
    </div>
  );
}

export default App;
