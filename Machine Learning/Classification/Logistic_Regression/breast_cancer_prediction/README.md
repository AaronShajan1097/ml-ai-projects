# 🩺 Breast Cancer Prediction using Logistic Regression

## 📌 Problem Statement
The objective of this project is to build a **binary classification model** that predicts whether a breast tumor is **malignant (1)** or **benign (0)** using Logistic Regression.

Early detection of malignant tumors is critical in medical diagnosis, making this a real-world healthcare machine learning application.

---

# 🧠 Approach

### 1️⃣ Data Understanding
- Loaded dataset using Pandas
- Inspected structure using `.head()` and `.info()`

### 2️⃣ Data Preprocessing
- Converted target variable:
  - Malignant (M) → 1
  - Benign (B) → 0
- Separated features (X) and target (y)

### 3️⃣ Exploratory Data Analysis (EDA)
- Visualized class distribution
- Checked dataset balance

### 4️⃣ Cross-Validation
- Applied 5-Fold Cross Validation
- Evaluated model stability using mean accuracy

### 5️⃣ Train-Test Split
- Used 70–30 split
- Applied `stratify=y` to maintain class balance

### 6️⃣ Feature Scaling
- Standardized features using `StandardScaler`
- Fit on training data and transformed test data to prevent data leakage

### 7️⃣ Model Training
- Trained Logistic Regression model with `max_iter=1000`

### 8️⃣ Model Evaluation
Evaluated performance using:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- ROC Curve
- AUC Score

### 9️⃣ Feature Importance
- Analyzed Logistic Regression coefficients
- Identified features influencing malignant prediction

---

# 📊 Model Performance

- ✅ Accuracy: **98%**
- 📈 High Recall for malignant class
- 📊 Strong ROC-AUC score indicating excellent classification capability

---

# ⚠ Why Recall is Important in Cancer Detection?

In medical diagnosis, **False Negatives are dangerous**.

If a malignant tumor is classified as benign:
- Treatment may be delayed
- Patient risk increases

Therefore, **Recall is more important than Accuracy** in this healthcare use case.


---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

# 📂 Project Structure

spam-email-classifier
│
  ├── emails.csv
  ├── spam_email_classifier.ipynb
  ├── README.md

---

# 🎯 Learning Outcomes

- Implemented Logistic Regression for binary classification
- Applied Cross-Validation for reliable performance estimation
- Prevented data leakage during feature scaling
- Evaluated model using multiple classification metrics
- Understood importance of Recall in medical datasets
- Interpreted Logistic Regression coefficients

---

# 🚀 Future Improvements

- Hyperparameter tuning using GridSearchCV
- Compare with SVM, Random Forest, and KNN
- Threshold tuning to optimize Recall
- Deploy model using Flask or FastAPI

---

# 📌 Conclusion

Logistic Regression achieved strong performance on the dataset, demonstrating that a well-preprocessed linear classifier can effectively solve real-world medical classification problems.

This project highlights:
- Proper ML workflow
- Evaluation beyond accuracy
- Importance of domain understanding in model building
