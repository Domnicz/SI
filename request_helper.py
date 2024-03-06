import requests
from errors import BairroNotFoundError

def get_bairro(cep):
    url = f'https://viacep.com.br/ws/{cep}/json'
    