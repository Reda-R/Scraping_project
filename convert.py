import csv
import json

csvfile = open('./csv/data.csv', 'r')
jsonfile = open('data.json', 'w')
jsonfile.write('[')

fieldnames = ("web-scraper-order", "web-scraper-start-url", "url_link", "url-href")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
jsonfile.write(']')
