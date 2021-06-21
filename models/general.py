import re
from datetime import datetime, date
from uuid import UUID
from enum import Enum, IntEnum
from typing import Optional, Union, Literal, List, TypeVar, Dict
from pydantic import BaseModel, Field, Extra, constr, conlist, \
    conint, PositiveInt, PositiveFloat, EmailStr


class BaseRegexType(str):
    pattern = None
    title = ''
    description = ''
    examples = []
    type = 'string'
    format = ''

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        assert cls.pattern
        if not isinstance(value, str):
            raise TypeError('string required')
        match = re.fullmatch(cls.pattern, value)
        if not match:
            raise ValueError(f'value not match regex "{cls.pattern}"')
        return value

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(
            type=cls.type,
            pattern=cls.pattern,
        )

        if cls.format:
            field_schema['format'] = cls.format

        if cls.description:
            if field_schema.get('description'):
                field_schema['description'] += ' ' + cls.description
            else:
                field_schema['description'] = cls.description

        if cls.examples:
            examples_str = ', '.join([f'`{x}`' for x in cls.examples])
            if field_schema.get('description'):
                field_schema['description'] += f'Examples: {examples_str}'
            else:
                field_schema['description'] = f'Examples: {examples_str}'
            field_schema['examples'] = cls.examples
        if not field_schema.get('title', False) and cls.title:
            field_schema['title'] = cls.title

    def __repr__(self):
        return f'{self.__class__.__name__}({super().__repr__()})'


class NACPBaseModel(BaseModel):
    def __init__(self, **kwargs):
        remove_keys = [k for k in kwargs if k.endswith('_extendedstatus')]
        for key in remove_keys:
            del kwargs[key]
        super().__init__(**kwargs)


class NoDataEnum(str, Enum):
    EMPTY_STRING = ''
    ConfidentialInformation = '[Конфіденційна інформація]'
    NotApplicable = '[Не застосовується]'
    Unknown = '[Не відомо]'
    FamilyMemberDidNotProvideInformation = '[Член сім\'ї не надав інформацію]'


NoData = Optional[NoDataEnum]


class YesNo(str, Enum):
    YES = 'Так'
    NO = 'Ні'


class YesNoStrNum(str, Enum):
    """
    1 - Так
    0 - Ні
    """
    YES = '1'
    NO = '0'


class YesNoInt(Enum):
    """
    1 - Так
    0 - Ні
    """
    YES = 1
    NO = 0


class ExtendedStatus(str, Enum):
    """
    Від НАЗК:
    1 - Не застосовується
    2 - Не відомо
    3 - Член сім’ї не надав інформацію
    """
    STATUS0 = '0'
    STATUS1 = '1'
    STATUS2 = '2'
    STATUS3 = '3'


ExtendedStatus = Optional[ExtendedStatus]


class ConfidentialInformation(str, Enum):
    TYPE1 = '[Конфіденційна інформація]'
    EMPTY = ''


ConfidentialInformation = Optional[ConfidentialInformation]

Unknown = Literal[
    '[Не застосовується]',
    '[Не відомо]',
    "[Член сім'ї не надав інформацію]",
    '',
]


class UsefulStr(BaseRegexType):
    pattern = r'^(?!\[)(.|\n)+(?<!\])$'
    type = 'useful string'
    # title = 'Текст з корисним вмістом'
    # description = 'Такий тип не включає текст який починається та закінчується квадратними дужками.'


class City(BaseRegexType):
    pattern = r'^(\d+\.){2,8}\d+$'
    examples = ['1.2.80', '1.2.68.2.24.8.98.1.2']


City = Optional[Union[City, Unknown]]


class CityType(BaseRegexType):
    pattern = r"^(\w|[ ,'.\-\(\)])+( ?/ ?(\w|[ ,'.\-])+?)*$"
    examples = [
        'Сільради, Підпордковані Макіївській Міськраді / Макіївка / Донецька область / Україна',
        'Кременець / Тернопільська Область/м.Тернопіль / Україна',
    ]


CityType = Union[CityType, Unknown]


class CompanyCode(BaseRegexType):
    pattern = r'^[0-9A-Za-z.\- ]{2,22}$'
    title = 'Код компанії'
    examples = [
        '58', '456789', '00885623', '45674895213', '1245896325874125896',
        '679-316-65-71', '289828', 'DMCC-096576', '000000000', 'CH-501.3.017.626-8'
    ]


class BrokenFloat(BaseRegexType):
    pattern = r'^\d+[,.]?(\d+)?$'
    examples = ["33,58", "33.58", "11", "35."]


class ChangesData(BaseModel):
    changesYear: str = Field(title='Звітний рік в ППСЗ')

    class Config:
        extra = Extra.forbid


class PersonInfoEnum(Enum):
    """
    1 - суб'єкт декларування;
    j - третя особа;
    {час_створення_запису} = відповідає id члена сім'ї суб'єкта декларування.
    """
    SELF_NUM = 1
    SELF = '1'
    THIRD_PERSON = 'j'


PersonInfo = TypeVar('PersonInfo', PersonInfoEnum, conint(gt=1))


class DateUK(BaseRegexType):
    pattern = r'^\d{2}\.\d{2}\.\d{4}$'
    format = 'date'
    examples = ["25.05.2019"]


Currency = Literal[
    'UAH',
    'USD',
    'EUR',
    'RUB',
    'CHF',
    'GBP',
    'PLN',
    'CAD',
    'GEL',
    'CNY',
    'HRK',
    'SEK',
]
