import joblib

# Load ML model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def analyze_answer(text):
    words = text.split()

    # Avoid empty input
    if len(words) == 0:
        return {
            "communication": 0,
            "confidence": 0,
            "technical": 0,
            "ml_score": 0,
            "prediction": "Invalid",
            "feedback": ["Please enter a valid answer"]
        }

    # -------------------------------
    # ✅ Rule-Based Scores (your logic)
    # -------------------------------

    # Communication
    unique_words = len(set(words))
    communication = (unique_words / len(words)) * 100

    # Confidence
    weak_words = ["maybe", "i think", "probably", "not sure"]
    weak_count = sum(phrase in text.lower() for phrase in weak_words)
    confidence = max(0, 100 - weak_count * 15)

    # Technical
    keywords = ["python", "sql", "api", "data", "machine learning"]
    match_count = sum(word in text.lower() for word in keywords)
    technical = (match_count / len(keywords)) * 100

    # -------------------------------
    # 🤖 ML Prediction (NEW PART)
    # -------------------------------

    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]

    if prediction == 1:
        ml_score = 80
        ml_feedback = "Strong answer (ML detected)"
    else:
        ml_score = 40
        ml_feedback = "Weak answer (ML detected)"

    # -------------------------------
    # 🧠 Combined Feedback
    # -------------------------------

    feedback = []

    if communication < 50:
        feedback.append("Try to use more varied vocabulary.")

    if confidence < 60:
        feedback.append("Avoid weak phrases like 'maybe', 'I think'.")

    if technical < 50:
        feedback.append("Include more technical keywords relevant to the role.")

    # Add ML feedback
    feedback.append(ml_feedback)

    if len(feedback) == 1:
        feedback.append("Good answer! Keep it up 👍")

    # -------------------------------
    # 🎯 Final Output
    # -------------------------------

    return {
        "communication": round(communication, 2),
        "confidence": confidence,
        "technical": round(technical, 2),
        "ml_score": ml_score,
        "prediction": "Good" if prediction == 1 else "Weak",
        "feedback": feedback
    }