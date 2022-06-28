
import pandas as pd
import numpy as np
from mylinearregression import MyLinearRegression as MyLR

data = pd.read_csv("spacecraft_data.csv")
Price = np.array(data["Sell_price"]).reshape(-1, 1)
Age = np.array(data["Age"]).reshape(-1, 1)
Thrust_p = np.array(data["Thrust_power"]).reshape(-1, 1)
Terameters = np.array(data["Terameters"]).reshape(-1, 1)

age_model = MyLR(np.array([[600], [-10]]), 0.01, 100000)
print("Price prediction for age")
print(age_model.fit_(Age, Price))
age_model.plot_(Age, Price,
                ("$x_1$ : age (in years)"),
                "y : sell price (in keuros)",
                "Sell price",
                ("navy"), ("dodgerblue"))
print("MSE : ", age_model.mse_(age_model.predict_(Age), Price))
thrust_model = MyLR(np.array([[3], [4]]), 0.00001, 100000)
print("Price prediction for thrust power")
print(thrust_model.fit_(Thrust_p, Price))
thrust_model.plot_(Thrust_p, Price,
                   ("$x_2$ : thrust power (in 10Km/s)"),
                   "y : sell price (in keuros)",
                   "Sell price",
                   ("green"), ("lime"))
print("MSE : ", thrust_model.mse_(thrust_model.predict_(Thrust_p), Price))
terameters_model = MyLR(np.array([[700], [-2]]), 0.0001, 100000)
print("Price prediction for terameters")
print(terameters_model.fit_(Terameters, Price))
terameters_model.plot_(Terameters, Price,
                       ("$x_3$ : distance totalizer value\
 of spacecraft (in Tmeters)"),
                       "y : sell price (in keuros)",
                       "Sell price",
                       ("darkviolet"), ("hotpink"))
print("MSE : ", terameters_model.mse_(terameters_model.predict_(Terameters),
                                      Price))

all_data = np.concatenate((Age, Thrust_p, Terameters), axis=1)
all_model = MyLR(np.array([[400], [-24.5], [5.6], [-2.7]]), 0.00001, 100000)
print("Price prediction with all data")
print(all_model.fit_(all_data, Price))
all_model.plot_(all_data, Price,
                ("$x_1$ : Age (in years)",
                 "$x_2$ : thrust power (in 10Km/s)",
                 "$x_3$ : distance totalizer value\
 of spacecraft (in Tmeters)"),
                "y : sell price (in keuros)",
                "Sell price",
                ("navy", "green", "darkviolet"),
                ("dodgerblue", "lime", "hotpink"))
print("MSE : ", all_model.mse_(all_model.predict_(all_data), Price))
