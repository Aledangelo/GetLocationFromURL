import socket
from ip2geotools.databases.noncommercial import DbIpCity
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError, ImproperlyConfigured

validate = URLValidator()
url = input("Insert a URL (www.example.com): ")

try:
    tryURL = "https://" + url
    validate(tryURL)
except ValidationError or ImproperlyConfigured as e:
    print("Invalid URL")
    #print(e)
    exit()

try:
    IP = socket.gethostbyname(url)
except socket.gaierror as e:
    x = url.split("/")
    url = x[0]
    try:
        IP = socket.gethostbyname(url)
    except socket.gaierror as e:
        print("Invalid URL")
        #print(e)
        exit()

response = DbIpCity.get(IP, api_key='free')

print("IP: ", IP)
print("City: ", response.city)
print("Region: ", response.region)
print("Country: ", response.country)
