from FileLoader import FileLoader
from Komparator import Komparator


fl = FileLoader()
df = fl.load("../asserts/athlete_events.csv")
kp = Komparator(df)

kp.compare_box_plots("Sex", "Height")
kp.density("Sex", "Height")
kp.compare_histograms("Sex", "Height")

kp.compare_box_plots("Sport", "Year")
kp.density("Sex", "Age")
kp.compare_histograms("City", "Year")
