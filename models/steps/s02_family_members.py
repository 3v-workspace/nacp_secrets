from typing import List, Optional, Union, Literal
from enum import Enum, IntEnum
from pydantic import BaseModel, Field, Extra
from models.general import NoDataEnum, CityType, YesNo, NoData, \
    YesNoNumber, ExtendedStatus, City, ConfidentialInformation, \
    NotApplicable, FamilyMemberNotProvideInformation, EmptyString, NACPBaseModel, NotKnownFull

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


class Data(NACPBaseModel):
    id: int

    firstname: Optional[str]
    lastname: Optional[str]
    middlename: Optional[str]
    country: Union[int, NotKnownFull]

    eng_full_name: Optional[str]  # V2
    ukr_full_name: Optional[str]  # V2

    no_taxNumber: Optional[YesNoNumber]
    eng_firstname: Optional[str]
    eng_lastname: Optional[str]
    eng_middlename: Optional[str]
    identificationCode: ConfidentialInformation
    passportCode: ConfidentialInformation

    previous_firstname: Optional[str]
    previous_lastname: Optional[str]
    previous_middlename: Optional[str]
    taxNumber: ConfidentialInformation
    passport: ConfidentialInformation

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
    unzr: ConfidentialInformation = Field(title='Унікальний номер запису в Єдиному державному демографічному реєстрі')
    eng_full_address: ConfidentialInformation
    ukr_full_address: ConfidentialInformation

    subjectRelation: SubjectRelation

    class Config:
        extra = Extra.forbid


class FamilyMembersStep(NACPBaseModel):
    data: List[Data]

    class Config:
        extra = Extra.forbid
        title = "Інформація про членів сім'ї суб'єкта декларування"

