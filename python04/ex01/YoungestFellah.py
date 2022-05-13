def youngest_fellah(df, year):
    """
    Get the name of the youngest woman and man for the given year.
    Args:
        df: pandas.DataFrame object containing the dataset.
        year: integer corresponding to a year.
    Returns:
        dct: dictionary with 2 keys for female and male athlete.
    """
    try:
        return {
            'F': df.loc[(df["Sex"] == "F")
                        & (df["Year"] == year), "Age"].min(),
            'M': df.loc[(df["Sex"] == "M")
                        & (df["Year"] == year), "Age"].min()
        }
    except Exception as e:
        print("Error :", e)
        return None
