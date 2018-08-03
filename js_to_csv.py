import csv
import json

try:
    # From JSON to CSV:

    inputFile = open("translation.js", "r")
    outputFile = open("translation.csv", "w")

    data = json.loads(inputFile.read())

    keys = []
    for key, value in data["en"].iteritems():
        keys.append(key)

    myFields = ["key", "en", "pl"]
    writer = csv.DictWriter(outputFile, fieldnames=myFields)

    writer.writeheader()

    for key in keys:
        key_encode = key.encode("UTF-8", "replace")
        pl = ''
        en = ''

        if key in data["pl"]:
            pl = data["pl"][key].encode("UTF-8", "replace")

        if key in data["en"]:
            en = data["en"][key].encode("UTF-8", "replace")

        writer.writerow({"key": key_encode, "pl": pl, "en": en})

except Exception as e:
    print(e)
