def proportion_by_sport(data, year, sport, sex):
    try:
        return (len(data.loc[(data["Sex"] == sex)
                    & (data["Year"] == year)
                    & (data["Sport"] == sport), "Name"].unique())
                / len(data.loc[(data["Sex"] == sex)
                               & (data["Year"] == year), "Name"].unique()))
    except Exception as e:
        print("Error :", e)
        return None
