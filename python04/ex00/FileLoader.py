import pandas
import matplotlib.pyplot as plt


class FileLoader:

    def __init__(self) -> None:
        pass

    def load(self, path):
        try:
            ret = pandas.read_csv(path)
            print("Loading dataset of dimensions",
                  ret.shape[0], "X", ret.shape[1])
            return ret
        except Exception as e:
            print("Error :", e)
            return None

    def display(self, df, n):
        try:
            if n >= 0:
                print(df.loc[:,1:].head(n))
            else:
                print(df[:,1:].tail(-n))
        except Exception as e:
            print("Error :", e)
            return None
