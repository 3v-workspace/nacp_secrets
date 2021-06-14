import json
import os
from pprint import pprint
import requests
from models.declaration import DeclarationType


NACP_LIST = 'https://public-api.nazk.gov.ua/v2/documents/list/'
NACP_RETRIEVE = 'https://public-api.nazk.gov.ua/v2/documents/'


def get_one(_id):
    resp = requests.get(f'{NACP_RETRIEVE}{_id}')
    return resp.json()


def save_file(data, filename):
    full_declarations = []
    i = 0
    if data:
        for d in data:
            i += 1
            full_declarations.append(get_one(d['id']))
            print(f'\rProcessed {i} from {len(data)}', end='', flush=True)
        print()
        with open(filename, 'w') as f:
            json.dump(full_declarations, f, ensure_ascii=False, indent=2)
        print(f'Saved: {filename}')
    else:
        print('No Data')


def download(declaration_type, declaration_year, page=1):
    assert 0 <= declaration_type <= 5
    assert 2015 <= declaration_year <= 2021
    assert 1 <= page <= 100
    print(f'Start download {declaration_type = }, {declaration_year = }, {page = }')

    dir_name = f'./data/t{declaration_type}_{declaration_year}'
    os.makedirs(dir_name, exist_ok=True)
    filename = f'{dir_name}/t{declaration_type}_{declaration_year}_p{page}.json'

    resp = requests.get(NACP_LIST, params={
        'declaration_type': declaration_type,
        'declaration_year': declaration_year,
        'page': page,
    })
    data = resp.json()['data']
    save_file(data, filename)


def download_custom(*, filename='declarations.json', user_declarant_id=None, declaration_type=None,
                    declaration_year=None, page=1):
    assert 1 <= page <= 100

    params = {}
    if user_declarant_id:
        assert type(user_declarant_id) == int
        params['user_declarant_id'] = user_declarant_id
    if declaration_type:
        assert 0 <= declaration_type <= 5
        params['declaration_type'] = declaration_type
    if declaration_year:
        assert 2015 <= declaration_year <= 2021
        params['declaration_year'] = declaration_year

    resp = requests.get(NACP_LIST, params)
    data = resp.json()['data']
    save_file(data, filename)


if __name__ == '__main__':
    download(declaration_type=1, declaration_year=2019, page=2)
    download(declaration_type=1, declaration_year=2019, page=3)
    download(declaration_type=1, declaration_year=2019, page=8)
    download(declaration_type=1, declaration_year=2019, page=15)
    download(declaration_type=1, declaration_year=2019, page=30)
    download(declaration_type=1, declaration_year=2019, page=40)
    download(declaration_type=1, declaration_year=2019, page=60)
    download(declaration_type=1, declaration_year=2019, page=70)
    download(declaration_type=1, declaration_year=2019, page=80)
    download(declaration_type=1, declaration_year=2019, page=95)
    download(declaration_type=1, declaration_year=2019, page=99)
    print('Done')
