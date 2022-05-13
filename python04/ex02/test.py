from FileLoader import FileLoader
from ProportionBySport import proportion_by_sport

fl = FileLoader()
df = fl.load("../asserts/athlete_events.csv")

print(proportion_by_sport(df, 2004, 'Tennis', 'F'))
