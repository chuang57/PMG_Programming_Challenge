import csv
import sys
import argparse

#function to combine csv files and output the combination to stdout
def combineCSVFiles(files):
    spamwriter = csv.writer(sys.stdout, lineterminator='\n')
    spamwriter.writerow(getHeading(files[0]))
    for file in files:
        with open(file, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            base_name = getBaseName(file)
            next(reader)
            for row in reader:
                if row != []:
                    row.append(base_name)
                    spamwriter.writerow(row)


#function to get the heading row of a csv file
def getHeading(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        heading = next(reader)
        heading.append("filename")
    return heading


#function to get the base name of a path
def getBaseName(file):
    index = file.rfind("/")
    base_name = file[index+1:]
    return base_name


if __name__ == "__main__":
    try:
        # all command-line args present are gathered into a list.
        parser = argparse.ArgumentParser()
        parser.add_argument('files', nargs='*', type=str)
        args = parser.parse_args()
        files = args.files
        if len(files) == 0:
            raise Exception("Must input csv files as arguments")
        for file in files:
            index = file.rfind(".")
            if file[index:] != ".csv":
                raise Exception(file + " must be a csv file")
        combineCSVFiles(files)
    except Exception as e:
        print(e)
