import pandas as pd
import numpy as np
from mylinearregression import MyLinearRegression as MyLR

data = pd.read_csv("spacecraft_data.csv")
X = np.array(data['Age']).reshape(-1, 1)
Y = np.array(data['Sell_price']).reshape(-1, 1)
myLR_age = MyLR(theta=np.array([[1000.0], [-1.0]]),
                alpha=2.5e-5, max_iter=100000)
print("theta : \n", myLR_age.fit_(X, Y))
print("MSE : ", myLR_age.mse_(myLR_age.predict_(X), Y))

X = np.array(data[['Age', 'Thrust_power', 'Terameters']])
my_lreg = MyLR(theta=np.array([[1.0], [1.0], [1.0], [1.0]]),
               alpha=1e-5, max_iter=600000)
print(my_lreg.mse_(my_lreg.predict_(X), Y))
print(my_lreg.fit_(X, Y))
print(my_lreg.mse_(my_lreg.predict_(X), Y))
