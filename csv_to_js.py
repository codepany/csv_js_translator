import csv
import json
from collections import Counter

try:
    # From JSON to CSV:

    csvFile = open("translation.csv", "r")
    jsonFile = open("translation.json", "w")

    reader = csv.DictReader(csvFile)

    data = []

    for row in reader:
        data.append(row)

    data_json = json.dumps(data)

    translation = {}
    pl = {}
    en = {}
    keys = []
    val_pl = []
    val_en = []

    # Add data to translation JSON:
    for row in data:
        pl.update({row['key']: row['pl']})
        val_pl.append(row['pl'])
        en.update({row['key']: row['en']})
        val_en.append(row['en'])
        keys.append(row['key'])

    jsonFile.write("t =\n")
    translation.update({"pl": pl, "en": en})
    json.dump(translation, jsonFile)

    # Check repeated of keys:
    for key in keys:
        times = keys.count(key)
        if keys.count(key) > 1:
            print("{} times reapeat key: {}".format(times, key))

    # Check repeated of value PL:
    for value in val_pl:
        times = val_pl.count(value)
        if times > 1:
            print("{} times reapeat value PL: {}".format(times, value))

    # Check repeated of value EN:
    for value in val_en:
        times = val_en.count(value)
        if times > 1:
            print("{} times reapeat value EN: {}".format(times, value))

    jsonFile.close()

except Exception as e:
    print(e)
