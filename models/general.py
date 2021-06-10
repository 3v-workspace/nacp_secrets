import re
from enum import Enum
from typing import Optional, Union, Literal

from pydantic import BaseModel, Field, Extra, constr

uuid_regex = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{8}'

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
    STATUS3 = '3'


ExtendedStatus = Optional[ExtendedStatus]

ConfidentialInformation = Literal['[Конфіденційна інформація]']
NotApplicable = Literal['[Не застосовується]']
FamilyMemberNotProvideInformation = Literal["[Член сім'ї не надав інформацію]"]
EmptyString = Literal[""]

City = Optional[Union[
    constr(regex=r'^(\d+\.){6,8}\d+$'),
    NotApplicable,
    FamilyMemberNotProvideInformation,
    EmptyString,
]]

CityType = Union[
    constr(regex=r"^(\w| |-|')+( ?/ (\w| |-|')+?)*$"),
    FamilyMemberNotProvideInformation,
    NotApplicable,
]


class ChangesData(BaseModel):
    changesYear: str = Field(title='Звітний рік в ППСЗ')

    class Config:
        extra = Extra.forbid
