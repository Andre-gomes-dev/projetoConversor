from forex_python.converter import CurrencyRates

teste =  CurrencyRates


def obterCotacao(moeda1, moeda2, quantidade):
    lib = CurrencyRates()
    taxa= lib.get_rate(moeda1, moeda2)
    conversão = quantidade  * taxa
    return  conversão


moeda1     =  "USD"
moeda2     =  "BRL"
quantidade = 100


valorConv =  obterCotacao(moeda1, moeda2, quantidade)
print(f'{quantidade} {moeda1} equivalem a {valorConv:.2f} {moeda2}')
