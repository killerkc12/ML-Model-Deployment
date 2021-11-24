import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def marks_analysis(marks):
    X = pd.read_csv('./Linear_X_Train.csv')
    y = pd.read_csv('./Linear_y_Train.csv')

    X = X.values
    y = y.values

    model = LinearRegression()
    model.fit(X, y)

    X_test = np.array(marks)
    X_test = X_test.reshape(1, -1)

    return model.predict(X_test)