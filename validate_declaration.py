import json
from pprint import pprint
from pydantic import ValidationError, ListError
from pydantic.error_wrappers import ErrorWrapper
from colorama import Fore

from models.declaration import (
    Declaration,
    AnnualDeclarationV3,
    AnnualDeclarationV2,
)
import sys
import os

SCHEMAS = {
    1: {
        2: AnnualDeclarationV2,
        3: AnnualDeclarationV3,
    },
}

FILES_DIRS = {
    't1_2020',
    't1_2019',
    't1_2018',
    't1_2017',
    't1_2016',
    't1_2015',
}

declarations = []
for dir_name in FILES_DIRS:
    for file_name in os.listdir(f'data/{dir_name}'):
        with open(f'data/{dir_name}/{file_name}') as f:
            declarations += json.load(f)


def validate(declaration: dict):
    d_type = declaration['declaration_type']
    schema_v = declaration['schema_version']
    try:
        SCHEMAS[d_type][schema_v].validate(declaration)
    except KeyError:
        raise ValueError(f'No Schema for {d_type = }, {schema_v = }')


def validate_one(index):
    declaration = declarations[index]
    try:
        validate(declaration)
    except ValidationError as e:
        pprint(declaration)
        sys.stdout.flush()
        raise


def display_loc(loc):
    if loc:
        return '.'.join([str(x) for x in loc])
    return ''


def get_value(obj, loc):
    val = obj
    for key in loc:
        try:
            val = val[key]
        except KeyError:
            return 'No Value'
    if isinstance(val, str):
        return f'"{val}"'
    return val


indent = -1


def flatten_errors(obj, errors, loc=None):
    global indent

    for error in errors:
        indent += 1
        if isinstance(error, ErrorWrapper):

            if loc:
                error_loc = loc + error.loc_tuple()
            else:
                error_loc = error.loc_tuple()

            if isinstance(error.exc, ValidationError):
                print(
                    ' |----' * indent,
                    f'{Fore.BLUE}{error.exc.model.__name__} '
                    f'{Fore.RESET}-> '
                    f'{Fore.CYAN}{display_loc(error_loc)} '
                    # f'{Fore.RESET}= '
                    # f'{Fore.GREEN}{get_value(obj, error_loc)}'
                    f'{Fore.RESET}'
                )
                flatten_errors(obj, error.exc.raw_errors, error_loc)
            else:
                print(
                    ' |----' * indent,
                    f'{Fore.RED}{error.exc} '
                    f'{Fore.RESET}-> '
                    f'{Fore.CYAN}{display_loc(error_loc)} '
                    f'{Fore.RESET}= '
                    f'{Fore.GREEN}{get_value(obj, error_loc)}'
                    f'{Fore.RESET}'
                )
        elif isinstance(error, list):
            indent -= 1
            flatten_errors(obj, error, loc=loc)
            indent += 1
        else:
            raise RuntimeError(f'Unknown error object: {error}')
        indent -= 1


def validate_all():
    for i, declaration in enumerate(declarations):
        try:
            validate(declaration)
        except ValidationError as e:
            pprint(declaration)
            flatten_errors(declaration, e.raw_errors)
            exit()
            # make_error_three(e)
            # exit()
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
