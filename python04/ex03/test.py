from FileLoader import FileLoader
from HowManyMedals import how_many_medals

fl = FileLoader()
df = fl.load("../asserts/athlete_events.csv")

print(how_many_medals(df, 'Kjetil Andr Aamodt'))
