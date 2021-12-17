"""
Служебная программка, сохраняет список словарей в json? которые затем будут подгружаться в контекст страницы
"""
import json
import os.path
from pprint import pprint

JSON_EXT = '.json'

def get_filename(name):
    return os.path.join(os.getcwd(), f'{name}{JSON_EXT}')

def save_to_json(data, name):
    with open(get_filename(name),'w') as f:
        json.dump(data, f)

def read_from_json(name):
    with open(get_filename(name),'r') as f:
        return json.load( f)

if __name__ == '__main__':
    data = [
        {'city': 'Москва',
        'phone': '+7-888-111-1111',
        'email': 'info@geekshop.ru',
        'address': 'В пределах МКАД'
        },
        {'city': 'Санкт-Петербург',
        'phone': '+7-888-222-2222',
        'email': 'info@geekshop.ru',
        'address': 'МКАД'
        },
        {'city': 'Краснодар',
        'phone': '+7-888-333-3333',
        'email': 'info@geekshop.ru',
        'address': 'Южный обход'
        }]

    fname='saveddata'
    save_to_json(data, fname)
    pprint(read_from_json(fname))
