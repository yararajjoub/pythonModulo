"""
* Lagra data med JSON
 - för att kunna lagra en annan typ av data än 'String'

* JSON har följande datatyper:
    - Numbers int, float /(no distinction between them)
    - String str
    - Boolean True, False bool
    - Array list(tuple)  # an ordered list of zero or more elem
    - Object dict # collection of key-value pairs, keys must be string

VI KAN INTE LAGRA SET I JSON, däremot kan vi lagra tuplar men de måste omvandla dem till list-format först

* serialize - encoding data into JSON format
            dump()
* Deserialize - decoding JSON data back into native python objects
            load()
"""
# create a dict and write it to a JSON-file

import json
en_sv = {'one': 'en', 'two': 'tvo', 'three': 'tre'}
with open('en_sv.json', 'w') as f:
    json.dump(en_sv, f)

# the file en_sv.json now contains the following:
"""  sparade i JSON-filen som :

{"one": "en", "two": "tvo", "three": "tre"}
"""
# The file can later be read into a dict variabel using the function load:
with open('en_sv.json') as f:
    translation = json.load(f)

""""""""""""""""""""""""""""""""""""
filname = input('File name: ')
try:
    with open(filname) as myfile:  # read
        grade_book = json.load(myfile)  # att läsa från filen
except FileNotFoundError:  # om filen icke finns, skapa en ny dict
    grade_book = dict()


def read_scores(results):
    while True:
        name = input('Name: ')
        if name == '':
            return  # avbryt kunde använde break för att ta oss ur satsen
        score = int(input('Score: '))

        if name in results:  # finns namnet i dictionary? det blir "nyckel" i dictionary
            results[name].append(score)  # then add to list of score , (name = key, score = value)
        else:
            results[name] = [score]  # om den inte finns skapar vi nytt par med namn och resultat


read_scores(grade_book)  # modify

with open(filname, 'w') as f:  # write
    json.dump(grade_book, f) # att skriva i filen

# LÄSA -- MODIFIERA -- SKRIVA
