# Day 37 — Regression Algorithms

## Objective

Learn regression algorithms and build machine learning models that predict numerical values using Python and Scikit-learn.

## Topics Covered

- Classification vs regression
- Introduction to linear regression
- Simple linear regression
- Multiple linear regression
- Slope, weight and intercept
- Features and target variables
- Training and testing datasets
- Model training and predictions
- Loss functions and squared error
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R-squared (R²)
- Residuals and residual plots
- Model evaluation

## Notebook

`37_regression_algorithms.ipynb`

## Project Structure

```text
Day_37/
├── 37_regression_algorithms.ipynb
└── README.md
```

## Practical Work

- Created a sample house-price dataset.
- Visualized house size and price relationships.
- Separated features (X) and target (y).
- Split data into training and testing sets.
- Trained a Simple Linear Regression model.
- Inspected the learned slope and intercept.
- Generated predictions for test data.
- Visualized the regression line.
- Evaluated the model using MAE, MSE, RMSE and R².
- Calculated squared-error loss manually.
- Created a residual plot.
- Trained a Multiple Linear Regression model.
- Predicted the price of a new property.

## Tools and Libraries

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

## Important Lessons

- Regression predicts numerical values.
- Linear regression learns a relationship between input features and a numerical target.
- Simple linear regression uses one feature.
- Multiple linear regression uses multiple features.
- Training data is used to fit a model.
- Testing data helps evaluate performance on unseen examples.
- MAE measures average absolute error.
- MSE penalizes larger errors more heavily.
- RMSE expresses error in the target's original units.
- R² measures model fit relative to a mean-prediction baseline.
- Residuals are the differences between actual and predicted values.

## Installation

```bash
pip install numpy pandas matplotlib scikit-learn
```

## Git Commands

```bash
git add Day_37/
git commit -m "Complete Day 37 regression algorithms"
git push
```

## Key Takeaway

Regression is a supervised machine learning technique used to predict numerical values. Today, I trained simple and multiple linear regression models and learned how to evaluate their predictions using different regression metrics.