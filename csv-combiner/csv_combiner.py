import csv
import sys
import argparse


def combineCSVFiles(files):
    spamwriter = csv.writer(sys.stdout)
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


def getHeading(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        heading = next(reader)
        heading.append("filename")
    return heading


def getBaseName(file):
    index = file.rfind("/")
    base_name = file[index+1:]
    return base_name


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(prog = 'Combiner', description = 'Combines CSV files')
    # all command-line args present are gathered into a list. Additionally, an error message will be generated if there wasn’t at least one command-line argument present.
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('files', nargs='*', type=str)
        args = parser.parse_args()
        files = args.files
        if len(files) == 0:
            raise Exception("Must input csv files as arguments")
        for file in files:
            index = file.rfind(".")
            if file[index:] != ".csv":
                raise Exception("Must be csv files")
        combineCSVFiles(files)
    except Exception as e:
        print(e)
