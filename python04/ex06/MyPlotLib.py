import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
matplotlib.get_backend()


class MyPlotLib:

    def __init__(self) -> None:
        pass

    def histogram(self, data, **features):
        try:
            subdata = data.iloc[:, 1:]
            numerics = ['int16', 'int32', 'int64',
                        'float16', 'float32', 'float64']
            numdata = subdata.select_dtypes(include=numerics).columns
            if len(numdata) > 1:
                fig, ax = plt.subplots(1, len(numdata),
                                       constrained_layout=True)
                for i in range(0, len(numdata)):
                    sns.histplot(subdata, x=numdata[i], ax=ax[i], **features)
            else:
                sns.histplot(subdata, x=numdata[0], **features)
            plt.show()
        except Exception as e:
            print("Error :", e)

    def density(self, data, **features):
        try:
            subdata = data.iloc[:, 1:]
            sns.kdeplot(data=subdata, **features)
            plt.show()
        except Exception as e:
            print("Error :", e)

    def pair_plot(self, data, **features):
        try:
            subdata = data.iloc[:, 1:]
            sns.pairplot(data=subdata, **features)
            plt.show()
        except Exception as e:
            print("Error :", e)

    def box_plot(self, data, **features):
        try:
            subdata = data.iloc[:, 1:]
            fig, ax = plt.subplots()
            ax = sns.boxplot(data=subdata, **features)
            plt.show()
        except Exception as e:
            print("Error :", e)
