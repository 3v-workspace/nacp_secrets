from datetime import datetime, date
from typing import List, Optional, Union, Literal
from enum import Enum, IntEnum
from pydantic import BaseModel, Field, Extra
from models.general import NoDataEnum, CityType, YesNo, NoData, \
    YesNoNumber, ExtendedStatus, City, ConfidentialInformation, \
    NotApplicable, FamilyMemberNotProvideInformation, EmptyString, NACPBaseModel

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
    great_granddaughter = 'правнучка'
    grandfather = 'дід'
    under_guardianship = 'особа, яка перебуває під опікою'
    guardian = 'опікун'
    persons_who_live_together = 'особи, які спільно проживають, але не перебувають у шлюбі'


class BaseData(NACPBaseModel):
    id: int

    eng_identification_code: ConfidentialInformation

    birthday: ConfidentialInformation
    cityType: Optional[CityType]
    usage: Optional[List[Union[int, float]]]
    changedName: YesNoNumber
    citizenship: Union[int, NotApplicable]

    district: ConfidentialInformation
    city: City
    cityPath: ConfidentialInformation
    postCode: ConfidentialInformation
    apartmentsNum: ConfidentialInformation
    region: ConfidentialInformation
    street: ConfidentialInformation
    streetType: ConfidentialInformation
    housePartNum: ConfidentialInformation = Field(title='Номер корпусу')
    houseNum: ConfidentialInformation
    unzr: ConfidentialInformation

    subjectRelation: SubjectRelation


    # housePartNum_extendedstatus: ExtendedStatus
    # houseNum_extendedstatus: ExtendedStatus
    # unzr_extendedstatus: ExtendedStatus
    # birthday_extendedstatus: ExtendedStatus
    # eng_identification_code_extendedstatus: ExtendedStatus
    # district_extendedstatus: ExtendedStatus
    # city_extendedstatus: ExtendedStatus
    # citizenship_extendedstatus: ExtendedStatus
    # apartmentsNum_extendedstatus: ExtendedStatus
    # street_extendedstatus: ExtendedStatus
    # postCode_extendedstatus: ExtendedStatus
    # streetType_extendedstatus: ExtendedStatus
    # region_extendedstatus: ExtendedStatus

    class Config:
        extra = Extra.forbid


class BaseDataVariant1(BaseData):
    firstname: str
    lastname: str
    middlename: str

    previous_firstname: Optional[str]
    previous_lastname: Optional[str]
    previous_middlename: Optional[str]
    taxNumber: ConfidentialInformation
    passport: ConfidentialInformation

    # passport_extendedstatus: ExtendedStatus
    # middlename_extendedstatus: ExtendedStatus
    # previous_middlename_extendedstatus: ExtendedStatus
    # country_extendedstatus: ExtendedStatus
    # taxNumber_extendedstatus: ExtendedStatus

    class Config:
        extra = Extra.forbid


class DataV3Variant1(BaseDataVariant1):
    country: Union[int, FamilyMemberNotProvideInformation, NotApplicable]


class DataV3Variant2(BaseData):
    eng_full_name: str
    ukr_full_name: str

    eng_full_address: ConfidentialInformation

    ukr_full_address: ConfidentialInformation

    # ukr_full_address_extendedstatus: ExtendedStatus
    # eng_full_address_extendedstatus: ExtendedStatus

    class Config:
        extra = Extra.forbid


class DataV2(BaseDataVariant1):
    no_taxNumber: Optional[YesNoNumber]
    eng_firstname: Optional[str]
    eng_lastname: Optional[str]
    eng_middlename: Optional[str]
    identificationCode: ConfidentialInformation
    passportCode: ConfidentialInformation

    # identificationCode_extendedstatus: ExtendedStatus
    # eng_middlename_extendedstatus: ExtendedStatus


class FamilyMembersStepV3(NACPBaseModel):
    data: List[Union[DataV3Variant1, DataV3Variant2]]

    class Config:
        extra = Extra.forbid
        title = "Інформація про членів сім'ї суб'єкта декларування"


class FamilyMembersStepV2(NACPBaseModel):
    data: List[DataV2]

    class Config:
        extra = Extra.forbid
        title = "Інформація про членів сім'ї суб'єкта декларування"
