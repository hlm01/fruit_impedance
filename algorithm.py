import csv

def make_dictionary():
    with open('data/Impedance & Phase Data.csv', "r+",newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        # row[0] is the frequency row[1] is the Impedance
        fruit_dict = {int(rows[0]):float(rows[1]) for rows in reader}
        csvfile.seek(0)
        csvfile.truncate() # delete contents of file
        return fruit_dict
