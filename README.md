# 💳 Credit Card Fraud Detection

A machine learning project for detecting fraudulent credit card transactions using supervised and anomaly detection algorithms. The project focuses on handling highly imbalanced data with SMOTE, optimizing classification performance, and explaining model predictions using SHAP.

---

## 📌 Overview

Credit card fraud detection is a highly imbalanced binary classification problem where fraudulent transactions represent only a tiny fraction of all transactions. This project builds and compares multiple machine learning models to accurately identify fraudulent transactions while minimizing false positives and false negatives.

---

## ✨ Features

* 📊 Exploratory Data Analysis (EDA)
* 🧹 Data Preprocessing
* ⚖️ Class Imbalance Analysis
* 🔄 SMOTE Oversampling
* 📏 Feature Scaling
* 📈 Logistic Regression
* 🌲 Random Forest Classifier
* 🌳 Isolation Forest
* 🎯 Threshold Tuning
* 📉 ROC Curve
* 📈 Precision-Recall Curve
* 📋 Confusion Matrix
* 📊 Feature Importance
* 🔍 SHAP Explainability
* 💾 Model Saving & Loading
* 🖥️ Prediction Script

---

## 📂 Dataset

This project uses the **Credit Card Fraud Detection** dataset from Kaggle.

**Dataset Link:**

https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

### Dataset Usage

The project uses the dataset in two ways:

### 1. Jupyter Notebook

The notebook downloads the dataset automatically using **KaggleHub**.

```python
import kagglehub

path = kagglehub.dataset_download("mlg-ulb/creditcardfraud")
```

The notebook can therefore be run without manually placing the dataset in the `data/` directory.

### 2. Training and Prediction Scripts

The `train.py` and `predict.py` scripts use the local CSV dataset:

```text
data/
└── creditcard.csv
```

The dataset is **not included in this repository** because of its large size.

### Install KaggleHub

```bash
pip install kagglehub
```

> **Note:** A Kaggle account may be required to access the dataset through KaggleHub.

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Imbalanced-learn
* SHAP
* Matplotlib
* Seaborn
* Joblib
* KaggleHub
* Jupyter Notebook

---

## 📁 Project Structure

```text
credit-card-fraud-detection/
│
├── data/
│   └── creditcard.csv
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

## 📓 Run the Notebook

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
notebooks/fraud_detection.ipynb
```

The notebook downloads the dataset automatically using **KaggleHub**.

---

## ▶️ Train the Model

Make sure the dataset is available at:

```text
data/creditcard.csv
```

Then run:

```bash
cd src
python train.py --data "../data/creditcard.csv"
```

The training script processes the dataset, trains the machine learning models, evaluates their performance, and saves the trained model.

---

## 🔮 Make Predictions

After training the model, predictions can be generated using:

```bash
cd src
python predict.py --input "../data/creditcard.csv"
```

---

## 🤖 Models

The project evaluates the following models:

* Logistic Regression
* Random Forest Classifier
* Isolation Forest

The supervised models use different sampling techniques to handle the highly imbalanced fraud dataset.

---

## ⚖️ Imbalance Handling

The dataset contains significantly fewer fraudulent transactions than legitimate transactions.

The project uses:

* **SMOTE (Synthetic Minority Over-sampling Technique)**
* **RandomUnderSampler**

SMOTE generates synthetic samples for the minority fraud class, while RandomUnderSampler reduces the number of majority-class samples.

---

## 📊 Evaluation Metrics

The models are evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score
* Precision-Recall Curve
* Confusion Matrix

For fraud detection, **Precision, Recall, and F1 Score** are especially important because ROC-AUC alone does not fully represent the model's ability to detect fraudulent transactions.

---

## 🏆 Final Model

**Random Forest with SMOTE** was selected as the final model.

The model achieved:

| Metric    | Score |
| --------- | ----: |
| Precision |  0.95 |
| Recall    |  0.79 |
| F1 Score  |  0.86 |

Although Random Forest with RandomUnderSampler achieved a slightly higher ROC-AUC, its F1 Score was significantly lower. Therefore, **RF + SMOTE** provided a better balance between precision and recall for fraud detection.

---

## 🎯 Threshold Tuning

Threshold tuning was performed to improve the final model's prediction performance.

* **Best threshold:** `0.51`
* **Precision before tuning:** `0.93`
* **Precision after tuning:** `0.95`

The tuned threshold improved precision while maintaining strong fraud detection performance.

---

## 🔍 SHAP Explainability

SHAP was used to understand which features have the greatest influence on the Random Forest model's predictions.

The analysis showed:

* **V14** is the most important feature.
* **Low V14 values** tend to push the model toward predicting fraud.
* Other important features include **V4, V12, V10, and V3**.

---

## 📷 Visualizations

The project includes visualizations for:

* Class Distribution
* Correlation Heatmap
* ROC Curve
* Precision-Recall Curve
* Confusion Matrix
* Feature Importance
* SHAP Summary Plot

---

## 🎯 Learning Outcomes

* Handling highly imbalanced datasets
* Fraud detection using machine learning
* Applying SMOTE for minority-class oversampling
* Comparing different sampling techniques
* Anomaly detection with Isolation Forest
* Ensemble learning with Random Forest
* Threshold optimization
* Evaluating models using Precision, Recall, and F1 Score
* Model explainability using SHAP
* Building reusable machine learning pipelines
* Working with both KaggleHub and local datasets

---

## 👨‍💻 Author

**Rabi Sah**

---

## 📄 License

This project is licensed under the MIT License.
