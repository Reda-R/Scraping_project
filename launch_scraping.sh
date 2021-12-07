#!/bin/bash

python3 convert.py

sleep 2s

python3 replace.py

sleep 2s

python3 scraping.py

sleep 2s

mv ./json/data.json ./json/.old_json

sleep 2s

mv ./csv/data.csv ./csv/.old_csv

sleep 2s

echo "-------------- Working -----------------"

cat ./csv/links_verified.csv

echo "----------------------------------------"
