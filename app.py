from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained model
with open("pcos_model.pkl", "rb") as file:
    best_model = pickle.load(file)

# Feature columns used in training
feature_columns = ['age', 'weight_kg', 'hormonal_imbalance', 'hyperandrogenism',
                   'hirsutism', 'conception_difficulty', 'insulin_resistance',
                   'exercise_frequency', 'exercise_type', 'exercise_duration',
                   'sleep_hours', 'exercise_benefit']
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        # Get user input
        inputs = [
            float(request.form["age"]),
            float(request.form["weight_kg"]),
            1 if request.form["hormonal_imbalance"] == "Yes" else 0,
            1 if request.form["hyperandrogenism"] == "Yes" else 0,
            1 if request.form["hirsutism"] == "Yes" else 0,
            1 if request.form["conception_difficulty"] == "Yes" else 0,
            1 if request.form["insulin_resistance"] == "Yes" else 0,
            int(request.form["exercise_frequency"]),
            int(request.form["exercise_type"]),
            int(request.form["exercise_duration"]),  # Fixed type to int
            int(request.form["sleep_hours"]),  # Fixed type to int
            1 if request.form["exercise_benefit"] == "Yes" else 0
        ]

        # Debug: Print inputs to verify they are correct
        print("Inputs:", inputs)

        # Convert input to DataFrame
        sample_input = pd.DataFrame([inputs], columns=feature_columns)

        # Make prediction
        prediction = best_model.predict_proba(sample_input)[:, 1][0]
        probability = round(prediction * 100, 2)  # Convert to percentage

        # Debug: Print prediction to verify it is correct
        print("Prediction:", prediction)
        print("Probability:", probability)

        return render_template("result.html", probability=probability)

    return render_template("predict.html")


if __name__ == "__main__":
    app.run(debug=True)