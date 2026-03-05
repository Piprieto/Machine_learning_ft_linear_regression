# ft_linear_regression

## Introduction

This project is an introduction to **Machine Learning** through the implementation of a **simple linear regression algorithm** trained with **gradient descent**.

The objective is to predict the **price of a a car based on its mileage** using a mathematical model trained on a dataset.

Instead of using machine learning libraries that solve the problem automatically, the algorithm is implemented **from scratch** in order to understand the fundamentals of machine learning.

---

## Project

The general objective of this project is to create a model capable of predicting the **price of a car** using the following linear hypothesis:
---

## 1. Prediction Program

This program predicts the price of a car for a given mileage.

When executed, it asks the user for a mileage value and returns the estimated price.

## 2. Training Program

The training program reads the dataset and performs linear regression using gradient descent to determine the optimal values of θ0 and θ1.

The algorithm iteratively adjusts the parameters to minimize the prediction error. Is very important the parameters are updated simultaneously.
After training, the parameters are saved and used by the prediction program.

## Bonus Features

Data Visualization: Plot the dataset to visualize the distribution of mileage and price.

Regression Line: Plot the regression line on top of the dataset to visualize the model result.

Model Precision: Evaluate the accuracy of the model using metrics such as Mean Squared Error (MSE), Mean Absolute Error (MAE) and R² (coefficient of determination)

