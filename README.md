# 🔥 Body Fat Percentage Predictor

Predict **Body Fat Percentage** from body measurements with a highly accurate Linear Regression model trained on the [Body Fat Dataset](https://www.kaggle.com/datasets/fedesoriano/body-fat-prediction-dataset).  
This project demonstrates **end to end ML workflow**: data analysis, model training, evaluation, and a simple CLI-based prediction app.

---

## Features
-  **Exploratory Data Analysis (EDA)** with correlation heatmaps & scatter plots
-  **Linear Regression Model** trained with scikit-learn
- **Interactive CLI app for custom user input predictions**
- **Error Handling** for smooth user experience
---

## Model Performance 
**R² Score:** 0.99
**Mean Squared Error:** 0.38  
**Root Mean Squared Error:** 0.61 

---

## Requirements
```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:
```
pandas
matplotlib
seaborn
scikit-learn
joblib
```

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/AyaanNadeem12/BodyFatPrediction.git
   cd BodyFatPrediction
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python app.py
   ```

> Ensure Python 3.8 or above is installed on your system.

---
## Project Structure

```
bodyfat-predictor/
├── data/
│ └── bodyfat.csv # Dataset
├── notebooks/
│ └── ModelTrain.ipynb # EDA + Training Notebook
├── models/
│ └── bodyfat_model.pkl # Saved Model
├── src/
│ └── app.py # CLI Prediction App
├── requirements.txt
├── README.md
└── .gitignore
```
---
## License


This project is open-source and available under the [MIT License](LICENSE).
