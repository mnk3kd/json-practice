!/bin/bash

# fetch METAR data
curl -s "https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85" > aviation.json

# extract receiptTime values
jq -r '.[] | .receiptTime' aviation.json | head -n 6
