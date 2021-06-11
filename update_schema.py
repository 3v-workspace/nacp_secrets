import json
from datetime import date

from models.declaration import AnnualDeclarationV3, AnnualDeclarationV2, Declaration

annual_schema_v3 = AnnualDeclarationV3.schema()
annual_schema_v2 = AnnualDeclarationV2.schema()
definitions = annual_schema_v3.pop('definitions')
definitions.update(annual_schema_v2.pop('definitions'))

schema = {
    'openapi': '3.0',
    'info': {
        # 'description': '',
        'version': '0.1.0',
        'title': 'NACP Declarations API Documentation',
        'contact': {
            'email': 'roman.tiukh@dataocean.us'
        },
        # 'license': {
        #     'name': 'Apache 2.0',
        #     'url': 'http://www.apache.org/licenses/LICENSE - 2.0.html'
        # },
    },
    'definitions': definitions,
    'paths': {
        '/v2/documents/{id}': {
            'get': {
                'summary': 'NACP Retrieve Declaration',
                'parameters': [
                    {
                        'in': 'path',
                        'name': 'id',
                        'schema': {
                            'type': 'UUID',
                        },
                    },
                ],
                'responses': {
                    '200': {
                        'description': 'Success',
                        'content': {
                            'application/json': {
                                'schema': {
                                    'oneOf': [
                                        annual_schema_v3,
                                        annual_schema_v2,
                                    ],
                                },
                            },
                        },
                    },
                },
            },
        },
        '/v2/documents': {
            'get': {
                'summary': 'NACP List Declarations',
                'parameters': [
                    {
                        'in': 'query',
                        'name': 'user_declaration_id',
                        'schema': {
                            'type': 'number',
                        },
                    },
                    {
                        'in': 'query',
                        'name': 'declaration_type',
                        'schema': {
                            'type': 'number',
                            'minimum': 0,
                            'maximum': 5,
                        },
                    },
                    {
                        'in': 'query',
                        'name': 'declaration_year',
                        'schema': {
                            'type': 'number',
                            'maximum': date.today().year,
                            'minimum': 2015,
                        },
                    },
                    {
                        'in': 'query',
                        'name': 'page',
                        'schema': {
                            'type': 'number',
                            'minimum': 1,
                            'maximum': 100,
                        },
                    },
                ],
            },
        },
    },
}

with open('./web/schema.json', 'w') as file:
    json.dump(schema, file, ensure_ascii=False, indent=2)
