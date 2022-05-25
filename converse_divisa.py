# First program, this converted divisas MXN to USD

import requests

menu = """
    -----------------------------------------------------------------
                 <<< Conversor de Moneda >>>
    -----------------------------------------------------------------
    
    1.- Pesos (MXN) a Dolares (USD)
    2.- Dolares (USD) a Pesos (MXN)
    3.- Cualquier tecla para salir 

    Seleccione una opcion: """

option = int(input('Seleccione una opcion: '))


def conversor(amount:  float, exchange_rate: str):
    amount = float(input('Ingresa la cantidad de' + exchange_rate +' : '))
    count_divise = str(count_divise)

if option == 1:
    conversor(100, 'Pesos (MXN)')

# url for get a conversion directly
# url = "https://api.apilayer.com/exchangerates_data/convert?to=MXN&from=USD&amount=" + count_divise

# url for get the value of divise
url = "https://api.apilayer.com/exchangerates_data/latest?symbols=MXN&base=USD"

url = "https://api.apilayer.com/exchangerates_data/latest?symbols=MXN&base=USD"

payload = {}
headers= {
  "apikey": "fMRuOGbmuqb3kHNKa17ycA3QgoHhNGrX"
}

response = requests.request("GET", url, headers=headers, data = payload)
json_data = response.json() if response and response.status_code == 200 else None

#status_code = response.status_code

""" if json_data and 'info' in json_data:
    if 'rate' in json_data['info']:
        usd = json_data['info'].get('rate') """

if json_data and 'rates' in json_data:
    usd = json_data['rates'].get('MXN')

#count_usd = round(float(count_divise) / usd, 2)

footer = """

    El valor del Dolar (USD) es de: ' + str(usd)
    -----------------------------------------------------------
"""

#print(count_divise + ' MXN es equivalente a ' + str(count_usd) + ' USD')
#print('')

    

def run():
    print(menu)


if __name__ == "__main__":
    run()
