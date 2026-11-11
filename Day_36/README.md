# Day 36 — Machine Learning Foundations

## Objective

Understand the fundamentals of machine learning and train a supervised classification model using Python and Scikit-learn.

## Topics Covered

- Introduction to machine learning
- Traditional programming vs machine learning
- Supervised learning
- Unsupervised learning
- Reinforcement learning
- Features and labels
- Classification vs regression
- Training and testing datasets
- Logistic Regression
- Model predictions
- Model evaluation
- Accuracy, precision, recall and F1-score
- Confusion matrix
- Overfitting and underfitting
- Generalization

## Notebook

`36_machine_learning_fundamentals.ipynb`

## Dataset

Iris flower classification dataset from Scikit-learn.

The dataset contains:
- 150 flower samples
- 4 numerical features
- 3 flower species

## Practical Work

- Loaded and explored the Iris dataset.
- Created a Pandas DataFrame.
- Separated input features (X) and labels (y).
- Split the dataset into training and testing sets.
- Trained a Logistic Regression classifier.
- Generated predictions on unseen test data.
- Evaluated model accuracy.
- Created a confusion matrix.
- Generated a classification report.
- Compared training and testing accuracy.
- Predicted the species of a new flower.
- Experimented with a Decision Tree classifier.

## Tools and Libraries

- Python
- Jupyter Notebook
- Scikit-learn
- Pandas
- Matplotlib

## Important Lessons

- Machine learning algorithms learn patterns from data.
- Supervised learning uses labelled examples.
- Features are inputs and labels are target outputs.
- Classification predicts categories.
- Regression predicts numerical values.
- Training and testing data serve different purposes.
- Accuracy alone does not fully describe model quality.
- Overfitting occurs when a model learns training data too closely.
- Good models should generalize to unseen examples.
- Data leakage can make evaluation results misleading.

## Installation

```bash
pip install scikit-learn pandas matplotlib
```

## Git Commands

```bash
git add Day_36/
git commit -m "Complete Day 36 machine learning fundamentals"
git push
```

## Key Takeaway

Machine learning allows computers to learn patterns from examples instead of relying entirely on manually written rules.
