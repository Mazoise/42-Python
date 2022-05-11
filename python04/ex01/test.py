from FileLoader import FileLoader
from YoungestFellah import youngestfellah

fl = FileLoader()
df = fl.load("../asserts/athlete_events.csv")
print(youngestfellah(df, 2004))
print(youngestfellah(df, 1991))