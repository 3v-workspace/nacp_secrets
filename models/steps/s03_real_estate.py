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

BuildType = Literal[
    'багатоквартирний будинок',
    'житловий будинок',
]

# PersonInfo = Union[PersonInfo, int]


class Right(NACPBaseModel):
    rightBelongs: Union[PersonInfo, int]
    citizen: Optional[Citizen]
    ownershipType: OwnershipType
    otherOwnership: Optional[str]
    percent_ownership: Optional[Union[constr(regex=r'^\d+([,.]\d+)?$'), NotKnownFull]] = Field(
        title='percent-ownership (%)', alias='percent-ownership',
        description='Приклади: "33,58", "33.58", "11"',
    )
    rights_id: Optional[int]
    ua_buildType: Optional[BuildType]
    ua_city: Optional[Union[City, CityType]]
    rights_cityPath: Optional[City]
    ua_houseNum: ConfidentialInformation
    ua_postCode: ConfidentialInformation
    ua_street: ConfidentialInformation
    ua_streetType: ConfidentialInformation
    ua_apartmentsNum: ConfidentialInformation
    ua_housePartNum: ConfidentialInformation
    ua_sameRegLivingAddress: Optional[YesNoNumber]
    ua_livingAddressFull: ConfidentialInformation
    ua_regAddressFull: ConfidentialInformation
    ua_birthday: ConfidentialInformation
    ua_taxNumber: ConfidentialInformation
    ua_firstname: Optional[Union[str, Literal["[Член сім'ї не надав інформацію]"]]]
    ua_lastname: Optional[Union[str, Literal["[Член сім'ї не надав інформацію]"]]]
    ua_middlename: Optional[str]

    eng_birthday: ConfidentialInformation
    eng_fullname: Optional[str]
    eng_regAddress: ConfidentialInformation
    eng_taxNumber: ConfidentialInformation
    ukr_actualAddress: ConfidentialInformation
    ukr_fullname: Optional[str]

    ua_company_code: Optional[Union[constr(regex=r'^\d{8,10}$', max_length=10, min_length=8), NotKnownFull]]
    ua_company_name: Optional[str]

    eng_company_address: Optional[str]
    eng_company_code: Optional[Union[str, NotKnown]]
    eng_company_name: Optional[str]
    ukr_company_address: Optional[str]
    ukr_company_name: Optional[str]

    class Config:
        extra = Extra.forbid


class Data(NACPBaseModel):
    iteration: Optional[int]
    country: int
    city: City
    ua_street: ConfidentialInformation
    ua_apartmentsNum: ConfidentialInformation
    ua_houseNum: ConfidentialInformation
    objectType: ObjectType
    ua_buildType: Optional[BuildType]
    otherObjectType: Optional[str]

    owningDate: Union[constr(regex=r'^\d{2}\.\d{2}\.\d{4}$'), Literal["[Член сім'ї не надав інформацію]"]] \
        = Field(title='Дата набуття права, DD.MM.YYYY')
    regNumber: ConfidentialInformation
    cityPath: ConfidentialInformation
    ua_postCode: ConfidentialInformation
    district: ConfidentialInformation
    district: ConfidentialInformation
    rights: Optional[List[Right]]
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


class RealEstateStep(NACPBaseModel):
    data: List[Data]

    class Config:
        extra = Extra.forbid
        title = "Об'єкти нерухомості"
