class SpatioTemporalData:

    def __init__(self, data):
        self.data = data

    def when(self, location):
        try:
            return(list(self.data.loc[self.data["City"] == location,
                        "Year"].unique()))
        except Exception as e:
            print("Error :", e)
            return None

    def where(self, date):
        try:
            return(list(self.data.loc[self.data["Year"] == date,
                                      "City"].unique()))
        except Exception as e:
            print("Error :", e)
            return None
