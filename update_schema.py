import json
from datetime import date

from models.declaration import AnnualDeclarationV3

d1_schema = AnnualDeclarationV3.schema()
definitions = d1_schema.pop('definitions')
# definitions.update(d2_schema.pop('definitions'))

schema = {
    'openapi': '3.0',
    'info': {
        'description': 'This is a simple API',
        'version': '1.0.0',
        'title': 'Simple Inventory API',
        # put the contact info for your development or API team
        'contact': {
            'email': 'you@your-company.com'
        },
        'license': {
            'name': 'Apache 2.0',
            'url': 'http://www.apache.org/licenses/LICENSE - 2.0.html'
        },
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
                                        d1_schema,
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
