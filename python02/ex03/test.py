from csvreader import CsvReader

if __name__ == "__main__":
    print("TEST1 : Good file, first 2 lines, header true")
    with CsvReader('good.csv', header=True, skip_bottom=16) as file:
        data = file.getdata()
        header = file.getheader()
        print("HEADER : ", header)
        for i in data:
            print(i)
    print("\nTEST2 : Good file, lines 2 to 4, header false")
    with CsvReader('good.csv', skip_top=3, skip_bottom=14) as file:
        data = file.getdata()
        header = file.getheader()
        print("HEADER : ", header)
        for i in data:
            print(i)
    print("\nTEST3 : Good file, last 2 lines")
    with CsvReader('good.csv', header=True, skip_top=16) as file:
        data = file.getdata()
        header = file.getheader()
        print("HEADER : ", header)
        for i in data:
            print(i)
    print("\nTEST4 : Perso file, sep=space")
    with CsvReader('perso.csv', sep=' ', header=True) as file:
        data = file.getdata()
        header = file.getheader()
        print("HEADER : ", header)
        for i in data:
            print(i)
    print("\nTEST5 : Bad file")
    with CsvReader('bad.csv') as file:
        if file is None:
            print("File is corrupted")
    print("\nTEST6 : No existing file")
    with CsvReader('noexist.csv') as file:
        if file is None:
            print("File does not exist")
