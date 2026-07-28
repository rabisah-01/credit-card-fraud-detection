# 💳 Credit Card Fraud Detection

A machine learning project for detecting fraudulent credit card transactions using supervised and anomaly detection techniques. The project focuses on handling highly imbalanced data, optimizing classification performance, and explaining model predictions.

---

## 📌 Overview

Credit card fraud is a significant financial problem due to the extremely small number of fraudulent transactions compared to legitimate ones. This project builds and evaluates multiple machine learning models to identify fraudulent transactions while minimizing false positives and false negatives.

---

## 🚀 Features

- 📊 Exploratory Data Analysis (EDA)
- 🧹 Data Preprocessing
- ⚖️ Class Imbalance Analysis
- 🔄 SMOTE Oversampling
- 📏 Feature Scaling
- 🌲 Random Forest Classifier
- 📈 Logistic Regression
- 🌳 Isolation Forest
- 🎯 Threshold Tuning
- 📉 ROC Curve
- 📈 Precision-Recall Curve
- 📋 Confusion Matrix
- 📊 Feature Importance
- 🔍 SHAP Explainability
- 💾 Model Saving & Loading
- 🖥️ Prediction Script

---

## 📂 Dataset

**Dataset:** Credit Card Fraud Detection

https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

### Features

| Feature | Description |
|----------|-------------|
| Time | Seconds elapsed between transactions |
| V1-V28 | PCA transformed features |
| Amount | Transaction amount |
| Class | 0 = Legitimate, 1 = Fraud |

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Imbalanced-learn
- SHAP
- Matplotlib
- Joblib
- Jupyter Notebook

---

## 📁 Project Structure

```text
credit-card-fraud-detection/
│
├── data/
│   └── creditcard.csv
│
├── models/
│   ├── logistic_regression.pkl
│   ├── random_forest.pkl
│   └── isolation_forest.pkl
│
├── notebooks/
│   └── fraud_detection.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   ├── predict.py
│   └── utils.py
│
├── visuals/
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/credit-card-fraud-detection.git

cd credit-card-fraud-detection

pip install -r requirements.txt
```

---

## ▶️ Train Model

```bash
cd src

python train.py
```

---

## 🔮 Predict

```bash
cd src

python predict.py
```

---

## 📊 Models

- Logistic Regression
- Random Forest Classifier
- Isolation Forest

---

## 📈 Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Precision-Recall Curve
- Confusion Matrix

---

## 📷 Visualizations

- Class Distribution
- Correlation Heatmap
- ROC Curve
- Precision-Recall Curve
- Confusion Matrix
- Feature Importance
- SHAP Summary Plot

---

## 🎯 Learning Outcomes

- Handling extremely imbalanced datasets
- Fraud detection using machine learning
- Ensemble learning
- Anomaly detection
- Threshold optimization
- Model explainability using SHAP
- Building reusable ML pipelines

---

## 👨‍💻 Author

**Rabi Sah**

---

## 📄 License

This project is licensed under the MIT License.