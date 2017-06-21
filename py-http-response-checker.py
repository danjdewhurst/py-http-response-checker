import sys
import requests

try:
    r = requests.head(sys.argv[1])
    print(sys.argv[1] + " returned a status code of: " + str(r.status_code))
except requests.ConnectionError:
    print("Connection error")
