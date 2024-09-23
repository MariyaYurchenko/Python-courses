import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit()

url = "https://itunes.apple.com/search?entity=song&limit=90&term=" + sys.argv[1]
response = requests.get(url)
print("\n  "+sys.argv[1] + "'s songs in itunes:")
res = response.json()
i = 1
for r in res["results"]:
    track = r["trackName"]
    print(f"    {i}) {track}")
    i+=1