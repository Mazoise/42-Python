def how_many_medals(data, name):

    try:
        years = data.loc[data["Name"] == name, "Year"].unique()
        ret = dict()
        for year in years:
            ret[year] = {'G': len(data.loc[(data["Name"] == name)
                                           & (data["Year"] == year)
                                           & (data["Medal"] == 'Gold')]),
                         'S': len(data.loc[(data["Name"] == name)
                                           & (data["Year"] == year)
                                           & (data["Medal"] == 'Silver')]),
                         'B': len(data.loc[(data["Name"] == name)
                                           & (data["Year"] == year)
                                           & (data["Medal"] == 'Bronze')])}
        return ret
    except Exception as e:
        print("Error:", e)
        return None
