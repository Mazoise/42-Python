import pandas as pd
import numpy as np
from my_linear_regression import MyLinearRegression as MyLR

data = pd.read_csv("are_blue_pills_magics.csv")
Xpill = np.array(data["Micrograms"]).reshape(-1, 1)
Yscore = np.array(data["Score"]).reshape(-1, 1)

linear_model1 = MyLR(np.array([[1], [1]]), 0.01, 15000)
print("Theta0 and Theta1 after fit function :")
print(linear_model1.fit_(Xpill, Yscore))
Y_model1 = linear_model1.predict_(Xpill)
linear_model1.plot_(Xpill, Yscore,
                    "Quantity of blue pills (in micrograms)",
                    "Space driving score",
                    "pills")
linear_model1.plot_loss_(Xpill, Yscore)
print("MSE :", linear_model1.mse_(Yscore, Y_model1))
