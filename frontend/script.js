async function analyze() {
    const text = document.getElementById("answer").value;

    if (!text) {
        alert("Please enter an answer!");
        return;
    }

    const response = await fetch("https://interview-backend-xi7q.onrender.com/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ answer: text })
    });

    const data = await response.json();

    document.getElementById("result").innerHTML = `
        <h3>Results:</h3>
        <p><b>Communication:</b> ${data.communication}</p>
        <p><b>Confidence:</b> ${data.confidence}</p>
        <p><b>Technical:</b> ${data.technical}</p>
        <p><b>ML Score:</b> ${data.ml_score}</p>
        <p><b>Prediction:</b> ${data.prediction}</p>
        <p><b>Feedback:</b> ${data.feedback.join(", ")}</p>
    `;
}