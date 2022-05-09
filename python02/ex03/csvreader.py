class CsvReader():

    def __init__(self,
                 filename=None, sep=',',
                 header=False, skip_top=0,
                 skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        try:
            self.fp = open(self.filename, "r")
        except FileNotFoundError:
            return None
        self.list_list = [i.strip('\n').strip(self.sep).split(self.sep)
                          for i in self.fp]
        for i in self.list_list:
            if len(i) != len(self.list_list[0]):
                return None
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self.fp.close()
        except AttributeError:
            pass

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Returns:
        nested list (list(list, list, ...)) representing the data.
        """
        return (self.list_list[self.skip_top
                + self.header:len(self.list_list)
                - self.skip_bottom])

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if self.header is True:
            return self.list_list[0]
        else:
            return None
