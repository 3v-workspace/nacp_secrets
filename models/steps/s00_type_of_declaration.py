from datetime import datetime, date
from typing import List, Optional, Union, Literal
from enum import Enum, IntEnum
from pydantic import BaseModel, Field, Extra

from models.general import NACPBaseModel


class DataVariant1(NACPBaseModel):
    declaration_type: Literal["Щорічна"] = Field(title='Тип декларації')
    declaration_period: str = Field(title='Звітний період')
    declaration_year: int = Field(title='Рік декларації')

    class Config:
        extra = Extra.forbid


class DataVariant2(NACPBaseModel):
    declarationType: Literal["1"] = Field(title='Тип декларації')
    declarationYear1: str = Field(title='Рік декларації')

    class Config:
        extra = Extra.forbid


class TypeOfDeclarationStep(NACPBaseModel):
    data: Union[DataVariant1, DataVariant2]

    class Config:
        extra = Extra.forbid
        title = 'Тип декларації та звітний період'
