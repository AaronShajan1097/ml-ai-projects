# California Housing Price Prediction

## 📖 Overview
This project applies Linear Regression to predict median house values using the California Housing dataset. The objective is to understand feature influence, evaluate model performance, and interpret regression outputs in a real-world scenario.

## 📊 Dataset
The project uses the California Housing dataset available through sklearn.  
It contains housing-related features such as:

- Median Income
- House Age
- Average Rooms
- Population
- Latitude & Longitude

Target Variable:
- Median House Value

## ⚙️ Project Workflow

The project follows a structured machine learning workflow:

1. Data Collection – Loaded the California Housing dataset from sklearn.
2. Exploratory Data Analysis – Inspected features, distributions, and correlations.
3. Data Preprocessing – Split dataset into training and testing sets and applied feature scaling.
4. Model Training – Trained a Linear Regression model on the processed data.
5. Model Evaluation – Evaluated performance using MSE, RMSE, and R² score.
6. Visualization – Compared actual vs predicted values and analyzed residuals.
7. Interpretation – Analyzed feature coefficients to understand their impact on house prices.

## 📈 Evaluation Metrics

- **MSE (Mean Squared Error)** – Measures average squared prediction error.
- **RMSE (Root Mean Squared Error)** – Interpretable error in target units.
- **R² Score** – Indicates the proportion of variance explained by the model.

## 📊 Results

The model demonstrates strong predictive performance with a high R² score, indicating effective learning of housing price patterns.

Residual analysis confirms that predictions align well with actual values, with no severe systematic bias.

## 🧠 Key Learnings

- Importance of feature scaling in regression models
- Interpretation of regression coefficients
- Difference between training and testing evaluation
- Detecting underfitting/overfitting through residual analysis

## 🚀 Future Improvements

- Implement Gradient Descent-based training
- Add regularization (Ridge/Lasso)
- Explore Polynomial Regression
- Perform hyperparameter tuning

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn