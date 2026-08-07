# 💳 Credit Card Fraud Detection

A machine learning project for detecting fraudulent credit card transactions using supervised and anomaly detection algorithms. The project focuses on handling highly imbalanced data with SMOTE, optimizing classification performance, and explaining model predictions using SHAP.

---

## 📌 Overview

Credit card fraud detection is a highly imbalanced binary classification problem where fraudulent transactions represent only a tiny fraction of all transactions. This project builds and compares multiple machine learning models to accurately identify fraudulent transactions while minimizing false positives and false negatives.

---

## ✨ Features

- 📊 Exploratory Data Analysis (EDA)
- 🧹 Data Preprocessing
- ⚖️ Class Imbalance Analysis
- 🔄 SMOTE Oversampling
- 📏 Feature Scaling
- 📈 Logistic Regression
- 🌲 Random Forest Classifier
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

This project uses the **Credit Card Fraud Detection** dataset from Kaggle.

**Dataset Link:**  
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

The dataset is downloaded automatically using **KaggleHub**.
The dataset is **not included** in this repository because of its large size.
Download the dataset from Kaggle and place the required files inside the `data/` directory.


### Install KaggleHub

```bash
pip install kagglehub
```

The dataset will be downloaded automatically the first time you run the project.

> **Note:** A Kaggle account may be required to access the dataset.

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
- KaggleHub
- Jupyter Notebook

---

## 📁 Project Structure

```text
credit-card-fraud-detection/
│
├── data/
│   └── .gitkeep
│
├── models/
│   └── .gitkeep
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
│   └── .gitkeep
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository.

```bash
git clone https://github.com/yourusername/credit-card-fraud-detection.git
```

Navigate to the project directory.

```bash
cd credit-card-fraud-detection
```

Install the required dependencies.

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Model

```bash
cd src

python train.py
```

---

## 🔮 Make Predictions

```bash
cd src

python predict.py
```

---

## 🤖 Models

- Logistic Regression
- Random Forest Classifier
- Isolation Forest

---

## 📊 Evaluation Metrics

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

- Handling highly imbalanced datasets
- Fraud detection using machine learning
- Anomaly detection with Isolation Forest
- Ensemble learning with Random Forest
- Threshold optimization
- Model explainability using SHAP
- Building reusable machine learning pipelines

---

## 👨‍💻 Author

**Rabi Sah**

---

## 📄 License

This project is licensed under the MIT License.