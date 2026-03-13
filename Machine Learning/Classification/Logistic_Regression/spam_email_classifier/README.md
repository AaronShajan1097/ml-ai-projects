# 📧 Spam Email Classifier using Logistic Regression

A Machine Learning project that classifies emails as **Spam or Not Spam** using **Logistic Regression**.
The model is trained on email word-frequency features and evaluated using multiple performance metrics.

---

# 📌 Problem Statement

Email spam is a major issue that affects communication and productivity. Spam emails often contain advertisements, phishing links, or malicious content that can compromise user security.

The goal of this project is to build a machine learning model that can automatically classify emails as Spam or Not Spam based on their features.

Using the Logistic Regression algorithm, we train a classifier on an email dataset and evaluate its performance using various metrics such as accuracy, precision, recall, confusion matrix, and ROC-AUC score.

This model helps demonstrate how machine learning techniques can be applied to solve real-world problems such as spam detection in email systems.

---

# 🚀 Project Overview

Email spam detection is a common **binary classification problem** in machine learning.
In this project, a **Logistic Regression classifier** is used to determine whether an email is spam.

The workflow includes:

* Data preprocessing
* Exploratory Data Analysis (EDA)
* Feature scaling
* Cross Validation
* Model training
* Model evaluation

---

# 🧠 Approach

The following steps were followed to build the model:

### 1️⃣ Data Loading

* Import the dataset (`emails.csv`)
* Inspect the dataset using `.head()`, `.info()`, `.describe()`

### 2️⃣ Data Preprocessing

* Removed unnecessary column: **Email No.**
* Split dataset into:

  * **Features (X)**
  * **Target (y)**

### 3️⃣ Exploratory Data Analysis (EDA)

* Checked **spam vs non-spam distribution** using a countplot.

### 4️⃣ Train-Test Split

* Dataset split into:

  * **70% training data**
  * **30% testing data**

### 5️⃣ Feature Scaling

* Applied **StandardScaler** to normalize features.

### 6️⃣ Cross Validation

* Used **7-Fold Cross Validation** on the training data to evaluate model stability and reduce overfitting.

### 7️⃣ Model Training

* Trained a **Logistic Regression** classifier.

### 8️⃣ Model Evaluation

The model performance was evaluated using:

* Accuracy Score
* Classification Report
* Confusion Matrix
* ROC Curve
* AUC Score

---

# 📊 Model Evaluation Metrics

The following metrics were used to evaluate the classifier:

* **Accuracy**
* **Precision**
* **Recall**
* **F1 Score**
* **ROC-AUC**

These metrics help measure how effectively the model distinguishes spam emails from non-spam emails.

---

# 📈 Visualizations

The project includes the following visualizations:

* Spam vs Non-Spam distribution
* Confusion Matrix heatmap
* ROC Curve with AUC score

These visualizations help interpret model performance.

---

# 📂 Project Structure

```
spam-email-classifier
│
├── emails.csv
├── spam_email_classifier.ipynb
├── README.md
```

---

# 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

# 🎯 Learning Outcome

Through this project, the following concepts were learned:

* Logistic Regression for classification
* Feature scaling using StandardScaler
* Cross Validation for reliable model evaluation
* Evaluation metrics for classification models
* Confusion matrix and ROC curve interpretation
* Building a structured machine learning workflow

---

# ⭐ Future Improvements

Possible future enhancements:

* Compare multiple models (Naive Bayes, Random Forest)
* Hyperparameter tuning
* Feature importance analysis
* Deploy the model using Flask or FastAPI