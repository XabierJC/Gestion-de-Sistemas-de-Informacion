from urllib.request import urlopen
from datetime import date
import time
import json

class ExchangeAPIClient():

    def get_rates(self):
        api_url = 'https://api.exchangeratesapi.io/latest'
        response = urlopen(api_url)
        rates = json.loads(response.read())
        return rates['rates']

    def convert(self, moneda , cantidad):
        rates = self.get_rates()
        return rates[moneda] * int (cantidad)

today = date.today()
f = open("divisas.txt","r")
g  = open("ahorros.txt","a")
total = 0 

conversor = ExchangeAPIClient()

for linea in f:
	moneda,cantidad = linea.split()
	moneda = moneda[0 : (len(moneda)-1)]
	if moneda == 'EUR':
		total+=int (cantidad)
	else:
		total += conversor.convert(moneda, cantidad)

g.write("{}-{}-{}, {} \n".format(today.year, today.month, today.day, total))
print("{}-{}-{}, {}".format(today.year, today.month, today.day, total))
f.close()
g.close()
