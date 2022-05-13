from FileLoader import FileLoader
from HowManyMedalsByCountry import how_many_medals_by_country

fl = FileLoader()
df = fl.load("../asserts/athlete_events.csv")

print(how_many_medals_by_country(df, 'France'))
