# 💳 Credit Card Fraud Detection using Logistic Regression

A Machine Learning project that detects **fraudulent credit card transactions** using **Logistic Regression**.  
The model classifies transactions as **Legitimate (0)** or **Fraudulent (1)** based on transaction features.

---

## 🚀 Project Overview

Credit card fraud is a major financial problem that causes significant losses for banks and customers. Detecting fraudulent transactions quickly is essential to prevent financial damage.

In this project, a **Logistic Regression classifier** is used to identify fraudulent credit card transactions. The workflow includes **data preprocessing, exploratory data analysis, feature scaling, cross validation, model training, and model evaluation**.

---

## 🧠 Approach

The following steps were followed to build the fraud detection model:

### 1️⃣ Data Loading
- Loaded the dataset `creditcard.csv`
- Inspected the dataset using `.head()`, `.info()`, and `.describe()`

### 2️⃣ Data Preprocessing
- Separated **features (X)** and **target variable (y)**
- Target variable meaning:
  - **0 → Legitimate transaction**
  - **1 → Fraudulent transaction**

### 3️⃣ Exploratory Data Analysis (EDA)
- Visualized the distribution of fraudulent and legitimate transactions using **Seaborn countplot**.

### 4️⃣ Train-Test Split
- Dataset split into:
  - **70% training data**
  - **30% testing data**

### 5️⃣ Feature Scaling
- Applied **StandardScaler** to normalize feature values.

### 6️⃣ Cross Validation
- Used **7-Fold Cross Validation** on the training dataset to evaluate model stability and reduce overfitting.

### 7️⃣ Model Training
- Trained a **Logistic Regression model** using the scaled training dataset.

### 8️⃣ Model Evaluation
The model was evaluated using:

- Accuracy Score
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## ⚠️ Class Imbalance

Credit card fraud datasets are **highly imbalanced**, meaning fraudulent transactions are much rarer than legitimate ones.

Because of this imbalance, **precision and recall are more important than accuracy** when evaluating the model.

---

## 📊 Model Evaluation Metrics

The following metrics were used to evaluate the classifier:

- **Accuracy**
- **Precision**
- **Recall**
- **F1 Score**
- **Confusion Matrix**

These metrics help determine how well the model identifies fraudulent transactions.

---

## 📈 Visualization

The project includes the following visualizations:

- Fraudulent vs Legitimate transaction distribution
- Confusion Matrix heatmap

These plots help interpret model performance.

---

## 📂 Project Structure

```
credit_card_fraud_detection
│
├── credit_card_fraud_detection.ipynb
├── creditcard.csv
├── README.md
```

---

## 🛠 Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

---

# 🎯 Learning Outcome

Through this project, the following machine learning concepts were applied:

- Logistic Regression for binary classification
- Data preprocessing and feature scaling
- Cross Validation for reliable model evaluation
- Understanding class imbalance in fraud detection
- Evaluating classification models using multiple metrics
- Interpreting confusion matrices

---

# ⭐ Future Improvements

Possible improvements for this project:

- Apply **SMOTE or other resampling techniques** to handle class imbalance
- Compare with other models such as **Random Forest or XGBoost**
- Perform hyperparameter tuning
- Deploy the model using **Flask or FastAPI**
