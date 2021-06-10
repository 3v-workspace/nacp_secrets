from datetime import datetime, date
from typing import List, Optional, Union
from enum import Enum, IntEnum
from pydantic import BaseModel, Field, Extra
from models.general import NoDataEnum, CityType, YesNo, NoData, \
    YesNoNumber, ExtendedStatus, City, ConfidentialInformation, \
    NotApplicable, FamilyMemberNotProvideInformation, EmptyString


PEP_RELATIONSHIPS_TYPES_TO_EN = {
    "ділові зв'язки": 'business relationship',
    "особисті зв'язки": 'personal connections',
    'особи, які спільно проживають': 'persons who live together',
    "пов'язані спільним побутом і мають взаємні права та обов'язки": 'are connected by common constructions and have common rights and responsibilities',
    'усиновлювач': 'adopter',
    'падчерка': 'stepdaughter',
    'дід': 'grandfather',
    'рідний брат': 'brother',
    'мати': 'mother',
    'син': 'son',
    'невістка': 'daughter-in-law',
    'внук': 'grandson',
    'мачуха': 'stepmother',
    'особа, яка перебуває під опікою або піклуванням': 'a person under guardianship or custody',
    'усиновлений': 'adopted',
    'внучка': 'granddaughter',
    'батько': 'father',
    'рідна сестра': 'sister',
    'зять': 'son-in-law',
    'чоловік': 'husband',
    'опікун чи піклувальник': 'guardian or trustee',
    'дочка': 'daughter',
    'свекор': 'father-in-law',
    'тесть': 'father-in-law',
    'теща': 'mother-in-law',
    'баба': 'grandmother',
    'пасинок': 'stepson',
    'вітчим': 'stepfather',
    'дружина': 'wife',
    'свекруха': 'mother-in-laws',
}


class SubjectRelation(str, Enum):
    WIFE = 'дружина'
    SON = 'син'
    DAUGHTER = 'дочка'
    HUSBAND = 'чоловік'
    GRANDSON = 'онук'
    MOTHER = 'мати'
    MOTHER_IN_LAWS = 'свекруха'
    FATHER_IN_LAWS = 'свекор'
    FATHER = 'батько'
    MOTHER_IN_LAW = 'теща'
    brother = 'рідний брат'
    grandmother = 'баба'
    stepdaughter = 'падчерка'
    stepson = 'пасинок'
    sister = 'рідна сестра'
    custody = 'особа, яка перебуває під піклуванням згаданого суб’єкта'
    granddaughter = 'онучка'
    stepfather = 'вітчим'
    son_in_law = 'зять'
    daughter_in_law = 'невістка'
    other = "інший зв'язок"
    father_in_law = 'тесть'
    adopted = 'усиновлений'
    grandfather = 'дід'
    under_guardianship = 'особа, яка перебуває під опікою'
    persons_who_live_together = 'особи, які спільно проживають, але не перебувають у шлюбі'


class BaseData(BaseModel):
    id: int

    eng_identification_code: Optional[ConfidentialInformation]
    eng_identification_code_extendedstatus: ExtendedStatus

    birthday: ConfidentialInformation
    birthday_extendedstatus: ExtendedStatus
    cityType: Optional[CityType]
    usage: Optional[List[Union[int, float]]]
    changedName: YesNoNumber
    citizenship: int

    district: Optional[Union[ConfidentialInformation, EmptyString]]
    district_extendedstatus: ExtendedStatus
    city: City
    city_extendedstatus: ExtendedStatus
    cityPath: Optional[ConfidentialInformation]
    postCode: Optional[Union[ConfidentialInformation, EmptyString]]
    postCode_extendedstatus: ExtendedStatus
    apartmentsNum: Optional[Union[ConfidentialInformation, EmptyString]]
    apartmentsNum_extendedstatus: ExtendedStatus
    region: Optional[ConfidentialInformation]
    region_extendedstatus: ExtendedStatus
    street: Optional[Union[ConfidentialInformation, EmptyString]]
    street_extendedstatus: ExtendedStatus
    streetType: Optional[Union[ConfidentialInformation, EmptyString]]
    streetType_extendedstatus: ExtendedStatus
    housePartNum: Optional[ConfidentialInformation] = Field(title='Номер корпусу')
    housePartNum_extendedstatus: ExtendedStatus
    houseNum: Optional[Union[ConfidentialInformation, EmptyString]]
    houseNum_extendedstatus: ExtendedStatus

    subjectRelation: SubjectRelation

    class Config:
        extra = Extra.forbid


class DataVariant1(BaseData):
    firstname: str
    lastname: str
    middlename: str
    middlename_extendedstatus: ExtendedStatus

    previous_firstname: Optional[str]
    previous_lastname: Optional[str]
    previous_middlename: Optional[str]
    previous_middlename_extendedstatus: ExtendedStatus

    country: Union[int, FamilyMemberNotProvideInformation, NotApplicable]
    country_extendedstatus: ExtendedStatus

    taxNumber: ConfidentialInformation
    taxNumber_extendedstatus: ExtendedStatus

    unzr: ConfidentialInformation
    unzr_extendedstatus: ExtendedStatus

    passport: ConfidentialInformation
    passport_extendedstatus: ExtendedStatus

    class Config:
        extra = Extra.forbid


class DataVariant2(BaseData):
    eng_full_name: str
    ukr_full_name: str

    eng_full_address: ConfidentialInformation
    eng_full_address_extendedstatus: ExtendedStatus

    ukr_full_address: ConfidentialInformation
    ukr_full_address_extendedstatus: ExtendedStatus

    class Config:
        extra = Extra.forbid


class FamilyMembersStep(BaseModel):
    data: Union[List[DataVariant1], List[DataVariant2]]

    class Config:
        extra = Extra.forbid
        title = "Інформація про членів сім'ї суб'єкта декларування"
