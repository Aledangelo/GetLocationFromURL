import socket
from ip2geotools.databases.noncommercial import DbIpCity
from django.core.validators import URLValidator

validate = URLValidator()
url = input("Insert a URL (www.example.com): ")

try:
    tryURL = "https://" + url
    validate(tryURL)
except:
    print("Invalid URL")
    exit()

IP = socket.gethostbyname(url)
response = DbIpCity.get(IP, api_key='free')

print("IP: ", IP)
print("City: ", response.city)
print("Region: ", response.region)
print("Country: ", response.country)
