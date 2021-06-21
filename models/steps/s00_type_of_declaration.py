from models.general import *


class DataVariant1(NACPBaseModel):
    declaration_type: Literal["Щорічна"] = Field(title='Тип декларації')
    declaration_period: UsefulStr = Field(title='Звітний період')
    declaration_year: conint(ge=2015, le=date.today().year) = Field(title='Рік декларації')

    class Config:
        extra = Extra.forbid


class DataVariant2(NACPBaseModel):
    declarationType: Literal["1"] = Field(title='Тип декларації')
    declarationYear1: conint(ge=2015, le=date.today().year) = Field(title='Рік декларації')

    class Config:
        extra = Extra.forbid


class TypeOfDeclarationStep(NACPBaseModel):
    data: Union[DataVariant1, DataVariant2]

    class Config:
        extra = Extra.forbid
        title = 'Тип декларації та звітний період'
