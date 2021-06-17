from datetime import datetime, date
from uuid import UUID
from enum import Enum, IntEnum
from typing import Optional, Union, Literal, List, TypeVar
from pydantic import BaseModel, Field, Extra, constr, conlist, \
    conint, PositiveInt, PositiveFloat, EmailStr


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

UsefulStr = constr(regex=r'^(?!\[)(.|\n)+(?<!\])$')

City = Optional[Union[
    constr(regex=r'^(\d+\.){2,8}\d+$'),
    Unknown,
]]

CityType = Union[
    constr(regex=r"^(\w|[ '.\-\(\)])+( ?/ ?(\w|[ '.\-\(\)])+?)*$"),
    Unknown,
]


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


DateUK = constr(regex=r'^\d{2}\.\d{2}\.\d{4}$')
