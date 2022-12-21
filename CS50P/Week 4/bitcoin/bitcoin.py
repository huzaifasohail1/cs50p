import requests
from sys import argv, exit

try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentp.json')
except requests.RequestException:
    exit()

res = response.json()
p = res['bpi']['USD']['rate'].replace(',','')
p = float(p)

if len(argv) != 2:
    exit('Missing command-line argument')
else:
    try:
        number = float(argv[1])
    except:
        exit('Command-line argument is not a number')

t = number * p

print(f'${t:,.4f}')