from FileLoader import FileLoader
from MyPlotLib import MyPlotLib


fl = FileLoader()
df = fl.load("../asserts/athlete_events.csv")
mpl = MyPlotLib()
mpl.histogram(df)
mpl.histogram(df, bins=10, color='g', element="step")
mpl.density(df)
mpl.density(df, palette="rocket", fill=True, alpha=.5)
mpl.pair_plot(df)
mpl.pair_plot(df, hue="Sex", vars=['Height', 'Weight'], height=7,
              plot_kws={'color': 'darkred', 's': 12, 'palette': "rocket_r"})
mpl.box_plot(df)
mpl.box_plot(df, x="Height", y="Sport", orient="h", palette="rocket")
