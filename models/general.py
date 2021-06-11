import re
from enum import Enum
from typing import Optional, Union, Literal

from pydantic import BaseModel, Field, Extra, constr

uuid_regex = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{8}'


class NACPBaseModel(BaseModel):
    def __init__(self, **kwargs):
        remove_keys = [k for k in kwargs if k.endswith('_extendedstatus')]
        for key in remove_keys:
            del kwargs[key]
        super().__init__(**kwargs)


NO_DATA = {
    None,
    '',
    '[Не застосовується]',
    '[Не відомо]',
    "[Член сім'ї не надав інформацію]",
    '[Конфіденційна інформація]'
}


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


class YesNoNumber(str, Enum):
    """
    1 - Так
    0 - Ні
    """
    YES = '1'
    NO = '0'


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


# ConfidentialInformation = Literal['[Конфіденційна інформація]']
ConfidentialInformation = Optional[ConfidentialInformation]
NotApplicable = Literal['[Не застосовується]']
NotKnown = Literal['[Не відомо]']
NotKnownFull = Literal['[Не застосовується]', '[Не відомо]', "[Член сім'ї не надав інформацію]"]
FamilyMemberNotProvideInformation = Literal["[Член сім'ї не надав інформацію]"]
EmptyString = Literal[""]

City = Optional[Union[
    constr(regex=r'^(\d+\.){6,8}\d+$'),
    Literal[
        '[Не застосовується]',
        "[Член сім'ї не надав інформацію]",
        '',
    ],
]]

CityType = Union[
    constr(regex=r"^(\w| |-|')+( ?/ (\w| |-|')+?)*$"),
    Literal[
        '[Не застосовується]',
        "[Член сім'ї не надав інформацію]",
    ],
]


class ChangesData(BaseModel):
    changesYear: str = Field(title='Звітний рік в ППСЗ')

    class Config:
        extra = Extra.forbid
