from FileLoader import FileLoader
from YoungestFellah import youngest_fellah

fl = FileLoader()
df = fl.load("../asserts/athlete_events.csv")
print(youngest_fellah(df, 2004))
print(youngest_fellah(df, 1991))
