from FileLoader import FileLoader


fl = FileLoader()
df = fl.load("../asserts/athlete_events.csv")
print(type(df))
fl.display(df, 11)
fl.display(df, -8)
