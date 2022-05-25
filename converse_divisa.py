# First program, this converted divisas MXN to USD

import requests

menu_start = """
    -----------------------------------------------------------------
                 <<< Conversor de Moneda >>>
    -----------------------------------------------------------------
    
    1.- Pesos (MXN) a Dolares (USD)
    2.- Dolares (USD) a Pesos (MXN)
    3.- Cualquier tecla para salir 

    Seleccione una opcion: 
    """

option = int(input(menu_start))

payload = {}
headers= {
    "apikey": "fMRuOGbmuqb3kHNKa17ycA3QgoHhNGrX"
}

def conversor(amount:  float):
    if option == 1:
        
        url = "https://api.apilayer.com/exchangerates_data/latest?symbols=MXN&base=USD"        

        response = requests.request("GET", url, headers=headers, data = payload)
        json_data = response.json() if response and response.status_code == 200 else None

        if json_data and 'rates' in json_data:
            usd = json_data['rates'].get('MXN')

        amount = round(float(amount) / usd, 2)
        print(str(amount))
        


    if option == 2:

        url = "https://api.apilayer.com/exchangerates_data/latest?symbols=USD&base=MXN"

        response = requests.request("GET", url, headers=headers, data = payload)
        json_data = response.json() if response and response.status_code == 200 else None

        if json_data and 'rates' in json_data:
            mxn = json_data['rates'].get('USD')

        amount = round(float(amount) / mxn, 2)
        print(str(amount))


# url for get a conversion directly
# url = "https://api.apilayer.com/exchangerates_data/convert?to=MXN&from=USD&amount=" + count_divise

#status_code = response.status_code

""" if json_data and 'info' in json_data:
    if 'rate' in json_data['info']:
        usd = json_data['info'].get('rate') """


def run():
    print(menu_start)

    if option == 1:
        exchange_rate = 'Pesos (MXN)'
        amount = float(input('  Ingresa la cantidad de ' + exchange_rate +' : '))
        conversor(amount)

    if option == 2:
        exchange_rate = 'Dolares (USD)'
        amount = float(input('  Ingresa la cantidad de ' + exchange_rate +' : '))
        conversor(amount)


if __name__ == "__main__":
    run()
