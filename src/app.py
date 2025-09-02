import joblib
import pandas as pd

# Load the trained and saved model
MODEL_PATH = "BodyFatPrediction/models/bodyfat_model.pkl"
model = joblib.load(MODEL_PATH)

# Get exact feature names from the trained model
FEATURES = list(model.feature_names_in_)

# Define units for features
UNITS = {
    "Density": "g/cm^3",
    "Age": "years",
    "Weight": "lbs",
    "Height": "inches",
    "Neck": "cm",
    "Chest": "cm",
    "Abdomen": "cm",
    "Hip": "cm",
    "Thigh": "cm",
    "Knee": "cm",
    "Ankle": "cm",
    "Biceps": "cm",
    "Forearm": "cm",
    "Wrist": "cm",
}

def get_float_input(prompt):
    # validating user input
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def main():
    print("\n-----🔥Body Fat % Predictor-----\n")

    # Collect user inputs dynamically
    values = []
    for feature in FEATURES:
        unit = UNITS.get(feature, "")  # Default to no unit if not listed
        prompt = f"Enter {feature}{f' ({unit})' if unit else ''}: "
        values.append(get_float_input(prompt))

    # Create DataFrame in exact feature order
    input_df = pd.DataFrame([values], columns=FEATURES)

    # Predict
    prediction = model.predict(input_df)[0]
    print(f"\n🎯 Estimated Body Fat: {prediction:.2f}%")

if __name__ == "__main__":
    main()
