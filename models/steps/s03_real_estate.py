from datetime import datetime, date
from typing import List, Optional, Union, Literal
from enum import Enum, IntEnum
from pydantic import BaseModel, Field, Extra, constr
from models.general import NoDataEnum, CityType, YesNo, NoData, \
    YesNoNumber, ExtendedStatus, City, ConfidentialInformation, \
    NotApplicable, FamilyMemberNotProvideInformation, EmptyString, NotKnown, NotKnownFull, NACPBaseModel

ObjectType = Literal[
    'Кімната',
    'Земельна ділянка',
    'Квартира',
    'Житловий будинок',
    'Гараж',
    'Садовий (дачний) будинок',
    'Офіс',
    'Інше',
]

OwnershipType = Literal[
    'Спільна власність',
    'Власність',
    'Інше право користування',
    'Спільна сумісна власність',
    'Оренда',
    'Власником є третя особа',
    'Право власності третьої особи, але наявні ознаки відповідно до частини 3 статті 46 ЗУ «Про запобігання корупції»',
    "[Член сім'ї не надав інформацію]",
]


class PersonInfo(str, Enum):
    """
    1 - суб'єкт декларування;
    j - третя особа;
    {час_створення_запису} = відповідає id члена сім'ї суб'єкта декларування.
    """
    SELF = '1'
    THIRD_PERSON = 'j'


Citizen = Literal[
    'Громадянин України',
    'Юридична особа, зареєстрована в Україні',
    'Іноземний громадянин',
    'Юридична особа, зареєстрована за кордоном',
]

# PersonInfo = Union[PersonInfo, int]


class BaseRight(NACPBaseModel):
    ownershipType: OwnershipType
    otherOwnership: Optional[str]
    percent_ownership: Optional[Union[constr(regex=r'^\d+([,.]\d+)?$'), NotKnownFull]] = Field(
        title='percent-ownership (%)', alias='percent-ownership',
        description='Приклади: "33,58", "33.58", "11"'
    )
    rights_id: Optional[int]
    ua_livingAddressFull: ConfidentialInformation
    ua_regAddressFull: Optional[Literal["[Конфіденційна інформація]", ""]]

    class Config:
        extra = Extra.forbid


class Right1(BaseRight):
    rightBelongs: Union[Literal['1'], int]


class Right2(BaseRight):
    rightBelongs: Literal['j']
    citizen: Citizen
    ua_birthday: Optional[Literal["[Конфіденційна інформація]"]]
    ua_firstname: Optional[str]
    ua_lastname: Optional[str]
    ua_middlename: Optional[str]
    ua_sameRegLivingAddress: Optional[YesNoNumber]
    ua_taxNumber: Optional[Literal["[Конфіденційна інформація]"]]

    eng_birthday: ConfidentialInformation
    eng_fullname: Optional[str]
    eng_regAddress: ConfidentialInformation
    eng_taxNumber: ConfidentialInformation
    ukr_actualAddress: ConfidentialInformation
    ukr_fullname: Optional[str]


class Right3(BaseRight):
    rightBelongs: Literal['j']
    citizen: Citizen
    ua_company_code: Optional[Union[constr(regex=r'^\d{8,10}$', max_length=10, min_length=8), NotKnown]]
    ua_company_name: Optional[str]

    eng_company_address: Optional[str]
    eng_company_code: Optional[NotKnown]
    eng_company_name: Optional[str]
    ukr_company_address: Optional[str]
    ukr_company_name: Optional[str]

    ua_birthday: Optional[Literal['[Конфіденційна інформація]']]
    ua_firstname: Optional[Literal["[Член сім'ї не надав інформацію]"]]
    ua_lastname: Optional[Literal["[Член сім'ї не надав інформацію]"]]
    ua_regAddressFull: Optional[Literal['[Конфіденційна інформація]']]
    ua_taxNumber: Optional[Literal['[Конфіденційна інформація]']]


class BaseData(NACPBaseModel):
    iteration: int
    country: int
    city: City
    ua_street: ConfidentialInformation
    ua_apartmentsNum: ConfidentialInformation
    ua_houseNum: ConfidentialInformation
    objectType: ObjectType
    otherObjectType: Optional[str]

    owningDate: Union[constr(regex=r'^\d{2}\.\d{2}\.\d{4}$'), Literal["[Член сім'ї не надав інформацію]"]] \
        = Field(title='Дата набуття права, DD.MM.YYYY')
    regNumber: ConfidentialInformation
    cityPath: ConfidentialInformation
    ua_postCode: ConfidentialInformation
    district: ConfidentialInformation
    district: ConfidentialInformation
    rights: Optional[List[Union[Right1, Right2, Right3]]]
    ua_housePartNum: ConfidentialInformation
    region: ConfidentialInformation
    ua_cityType: Optional[CityType]
    ua_streetType: ConfidentialInformation

    cost_date_assessment: Optional[Union[int, NotKnownFull]]

    costAssessment: Optional[Union[int, NotKnownFull]]
    costDate: Optional[Union[int, NotKnownFull]]
    person: Optional[Union[PersonInfo, int]]

    totalArea: Union[constr(regex=r'^\d+([,.]\d+)?$'), NotKnownFull] = Field(
        title='Загальна площа М2', description='Приклади: "109,8", "109.8", "1523"'
    )
    loc_engLivingAddress: ConfidentialInformation
    loc_ukrLivingAddress: ConfidentialInformation
    postCode: ConfidentialInformation

    class Config:
        extra = Extra.forbid


class DataV3(BaseData):
    pass


class RealEstateStepV3(NACPBaseModel):
    data: List[DataV3]

    class Config:
        extra = Extra.forbid
        title = "Об'єкти нерухомості"
