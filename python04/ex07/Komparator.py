from MyPlotLib import MyPlotLib


class Komparator:

    def __init__(self, data):
        self.data = data
        self.pl = MyPlotLib()

    def compare_box_plots(self, categorical_var, numerical_var):
        try:
            self.pl.box_plot(self.data, y=categorical_var, x=numerical_var)
        except Exception as e:
            print("Error:", e)

    def density(self, categorical_var, numerical_var):
        try:
            self.pl.density(self.data, hue=categorical_var, x=numerical_var)
        except Exception as e:
            print("Error:", e)

    def compare_histograms(self, categorical_var, numerical_var):
        try:
            subdata = self.data[["ID", categorical_var, numerical_var]]
            self.pl.histogram(subdata, hue=categorical_var, multiple="stack")
        except Exception as e:
            print("Error:", e)
