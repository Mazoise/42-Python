def count_medals(data, country, medal, year):
    team_sports = ['Basketball', 'Football',  'Tug-Of-War', 'Badminton',
                   'Sailing', 'Handball', 'Water Polo', 'Hockey',
                   'Rowing', 'Bobsleigh', 'Softball', 'Volleyball',
                   'Synchronized Swimming', 'Baseball', 'Rugby Sevens',
                   'Rugby', 'Lacrosse', 'Polo']
    all = list(data.loc[(data["Team"] == country)
                        & (data["Year"] == year)
                        & (data["Medal"] == medal), "Sport"])
    team_count = len(dict.fromkeys(filter(lambda x: x in team_sports, all)))
    single_count = len(list(filter(lambda x: x not in team_sports, all)))
    return team_count + single_count


def how_many_medals_by_country(data, country):

    try:
        years = (data.loc[data["Team"] == country, "Year"]).unique()
        years.sort()
        ret = dict()
        for year in years:
            ret[year] = {'G': count_medals(data, country, "Gold", year),
                         'S': count_medals(data, country, "Silver", year),
                         'B': count_medals(data, country, "Bronze", year)}
        return ret
    except Exception as e:
        print("Error :", e)
        return None
