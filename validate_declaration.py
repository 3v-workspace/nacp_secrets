import json
from pprint import pprint
from pydantic import ValidationError
from models.declaration import Declaration, AnnualDeclarationV3
import sys
import os

SCHEMA = AnnualDeclarationV3
FILES_DIRS = {
    't1_2020',
    't1_2019',
}


declarations = []
for dir_name in FILES_DIRS:
    for file_name in os.listdir(f'data/{dir_name}'):
        with open(f'data/{dir_name}/{file_name}') as f:
            declarations += json.load(f)


def validate(declaration: dict):
    SCHEMA.validate(declaration)


def validate_one(index):
    declaration = declarations[index]
    try:
        validate(declaration)
    except ValidationError as e:
        pprint(declaration)
        sys.stdout.flush()
        raise


def validate_all():
    for i, declaration in enumerate(declarations):
        try:
            validate(declaration)
        except ValidationError as e:
            pprint(declaration)
            print(f'index = {i}')
            for error in e.errors():
                loc = '.'.join([str(x) for x in error['loc']])
                val = declaration
                for key in error['loc']:
                    try:
                        val = val[key]
                    except KeyError:
                        val = 'No Value'
                        break
                print(f'------------------')
                print(f'{error["msg"]}')
                print(f'  {loc} = {val}')
                sys.stdout.flush()
                input('')
            sys.stdout.flush()
            exit()


if __name__ == '__main__':
    # validate_one(4)
    validate_all()
