#!/bin/bash

python3 convert.py

sleep 2s

python3 replace.py

sleep 2s

python3 scraping.py

sleep 2s

mv data.json ./.tmp_bin

sleep 2s

echo "-------------- Working -----------------"

cat ./csv/links_verified.csv

echo "----------------------------------------"
