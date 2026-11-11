# Day 38 — Decision Trees and Random Forests

## Objective

Understand tree-based machine learning algorithms and train Decision Tree and Random Forest models for both classification and regression.

## Topics Covered

- Introduction to Decision Trees
- Root nodes, branches and leaf nodes
- How Decision Trees learn
- Gini impurity
- Entropy
- Decision Tree classification
- Decision Tree regression
- Overfitting and tree depth
- Random Forest
- Bootstrap sampling
- Random feature selection
- Ensemble learning
- Classification majority voting
- Regression prediction averaging
- Feature importance
- Model evaluation and comparison

## Notebook

`38_decision_trees_random_forests.ipynb`

## Project Structure

```text
Day_38/
├── 38_decision_trees_random_forests.ipynb
└── README.md
```

## Practical Work

- Loaded and explored the Iris dataset.
- Split data into training and testing sets.
- Trained a Decision Tree classifier.
- Visualized the learned Decision Tree.
- Compared shallow and deep trees.
- Trained a Random Forest classifier.
- Compared classification accuracy.
- Evaluated predictions using a confusion matrix and classification report.
- Inspected Random Forest feature importance.
- Generated a synthetic regression dataset.
- Trained a Decision Tree regressor.
- Trained a Random Forest regressor.
- Compared regression models using MAE, RMSE and R².
- Made predictions for new examples.

## Tools and Libraries

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

## Important Lessons

- Decision Trees learn decision rules by splitting data.
- Gini impurity and entropy are common classification splitting criteria.
- Deep trees can overfit training data.
- Random Forest combines multiple decision trees.
- Bootstrap sampling and random feature selection create diversity among trees.
- Classification forests commonly use majority voting.
- Regression forests commonly average tree predictions.
- Feature importance estimates contribution to impurity reduction.
- Both Decision Trees and Random Forests support classification and regression.

## Installation

```bash
pip install numpy pandas matplotlib scikit-learn
```

## Git Commands

```bash
git add Day_38/
git commit -m "Complete Day 38 decision trees and random forests"
git push
```

## Key Takeaway

Decision Trees learn understandable decision rules from data. Random Forests combine many randomized trees to produce predictions that often generalize better than a single tree.

Today, I trained and compared tree-based models for both classification and regression.