from models.general import *
from models.steps.s03_real_estate import Citizen, OwnershipType


MovablePropertyType = Literal[
    'Персональні або домашні електронні пристрої',
    'Антикварний виріб',
    'Одяг',
    'Твір мистецтва (картина тощо)',
    'Ювелірні вироби',
    'Інше',
]


class Right(NACPBaseModel):
    rights_id: Optional[PersonInfo]
    ownershipType: OwnershipType
    otherOwnership: Optional[Union[UsefulStr, Unknown]]
    rightBelongs: PersonInfo
    percent_ownership: Optional[Union[BrokenFloat, Unknown]] = Field(alias='percent-ownership')
    citizen: Optional[Citizen]
    ua_firstname: Optional[Union[UsefulStr, Unknown]]
    ua_lastname: Optional[Union[UsefulStr, Unknown]]
    ua_middlename: Optional[Union[UsefulStr, Unknown]]
    ua_sameRegLivingAddress: Optional[YesNoStrNum]

    ua_company_code: Optional[Union[CompanyCode, Unknown]]
    ua_company_name: Optional[UsefulStr]

    ua_birthday: ConfidentialInformation
    ua_regAddressFull: ConfidentialInformation
    ua_taxNumber: ConfidentialInformation
    ua_livingAddressFull: ConfidentialInformation

    class Config:
        extra = Extra.forbid


class Data(NACPBaseModel):
    rights: Optional[List[Right]] = Field(description='ІНФОРМАЦІЯ ЩОДО ПРАВ НА МАЙНО, Може не існувати для V2')
    iteration: Optional[PositiveInt] = Field(description='Може не існувати для V2')
    person: Optional[PersonInfo]
    acqBeforeFD: YesNoStrNum
    acqPeriod: Optional[UsefulStr]
    costDateUse: Union[PositiveInt, PositiveFloat, Unknown] = Field(
        title='ВАРТІСТЬ НА ДАТУ НАБУТТЯ У ВЛАСНІСТЬ, ВОЛОДІННЯ ЧИ КОРИСТУВАННЯ АБО ЗА ОСТАННЬОЮ ГРОШОВОЮ ОЦІНКОЮ',
    )
    dateUse: Union[DateUK, Unknown] = Field(description='Дата набуття права, DD.MM.YYYY')
    manufacturerName: Union[UsefulStr, Unknown] = Field(title='Найменування виробника')
    objectType: MovablePropertyType = Field(title='Вид майна, якщо Інше то дані в otherObjectType')
    otherObjectType: Optional[Union[UsefulStr, Literal['']]]
    propertyDescr: Union[UsefulStr, Unknown] = Field(title='Опис майна')
    trademark: Union[UsefulStr, Unknown] = Field(title='Торгова марка')

    class Config:
        extra = Extra.forbid


class ValuableMovablePropertyStep(NACPBaseModel):
    data: List[Data]

    class Config:
        extra = Extra.forbid
        title = "Цінне рухоме майно (крім транспортних засобів)"
