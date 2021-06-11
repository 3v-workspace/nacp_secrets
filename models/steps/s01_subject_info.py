from datetime import datetime, date
from typing import List, Optional, Union, TypeVar, Literal
from enum import Enum, IntEnum
from pydantic import BaseModel, Field, Extra, constr
from models.general import NoDataEnum, CityType, YesNo, NoData, YesNoNumber, ExtendedStatus, City, \
    ConfidentialInformation, NotApplicable, EmptyString, NACPBaseModel


class PostCategory(str, Enum):
    CAT_A = 'А'  # кирилиця
    CAT_B = 'Б'  # кирилиця
    CAT_C = 'В'  # кирилиця
    CAT_1 = 'перша категорія'
    CAT_2 = 'друга категорія'
    CAT_3 = 'третя категорія'
    CAT_4 = 'четверта категорія'
    CAT_5 = "п'ята категорія"
    CAT_6 = 'шоста категорія'
    CAT_7 = 'сьома категорія'


class PublicPerson(str, Enum):
    YES = 'Так'
    NO = 'Ні'
    DEPUTY = 'Народні депутати України'
    NOT_APPLICABLE = '[Не застосовується]'
    CATEGORY_A = "Державні службовці, посади яких належать до категорії 'А'"
    HEAD = 'Керівники органів прокуратури, керівники обласних територіальних ' \
           'органів Служби безпеки України, голови та судді апеляційних судів'
    COURT_HEAD = 'Голови та судді Конституційного Суду України, ' \
                 'Верховного Суду, вищих спеціалізованих судів'
    HEAD2 = 'Керівники адміністративних, управлінських чи наглядових органів ' \
            'державних та казенних підприємств, господарських товариств, ' \
            'державна частка у статутному капіталі яких прямо чи опосередковано ' \
            'перевищує 50 відсотків'
    HEAD3 = 'Президент України, Прем’єр-міністр України, члени Кабінету Міністрів України та їх заступники'


class BaseData(NACPBaseModel):
    firstname: str
    lastname: str
    middlename: Optional[str]

    changedName: YesNoNumber
    previous_firstname: Optional[str]
    previous_lastname: Optional[str]
    previous_middlename: Optional[str]

    taxNumber: ConfidentialInformation
    passport: ConfidentialInformation
    birthday: ConfidentialInformation
    sameRegLivingAddress: YesNoNumber
    workPlace: str
    workPost: str
    unzr: ConfidentialInformation = Field(title='Унікальний номер запису в Єдиному державному демографічному реєстрі')


    postCode: ConfidentialInformation

    actual_apartmentsNum: ConfidentialInformation
    actual_city: ConfidentialInformation
    actual_cityPath: ConfidentialInformation
    actual_cityType: Optional[CityType]
    actual_district: ConfidentialInformation
    actual_street: ConfidentialInformation
    actual_postCode: ConfidentialInformation
    actual_region: ConfidentialInformation
    actual_streetType: ConfidentialInformation
    actual_houseNum: ConfidentialInformation
    actual_country: Optional[int]
    actual_housePartNum: ConfidentialInformation

    eng_actualAddress: ConfidentialInformation
    eng_actualPostCode: ConfidentialInformation
    ukr_actualAddress: ConfidentialInformation

    region: ConfidentialInformation
    streetType: ConfidentialInformation
    street: ConfidentialInformation
    district: ConfidentialInformation
    city: City
    country: int
    cityType: CityType
    housePartNum: ConfidentialInformation = Field(title='Номер корпусу')
    apartmentsNum: ConfidentialInformation
    cityPath: ConfidentialInformation
    houseNum: ConfidentialInformation

    # streetType_extendedstatus: ExtendedStatus
    # city_extendedstatus: ExtendedStatus
    # housePartNum_extendedstatus: ExtendedStatus
    # apartmentsNum_extendedstatus: ExtendedStatus
    # houseNum_extendedstatus: ExtendedStatus
    # previous_middlename_extendedstatus: ExtendedStatus
    # public_person_extendedstatus: ExtendedStatus
    # unzr_extendedstatus: ExtendedStatus
    # # passport_extendedstatus: ExtendedStatus
    # postCategory_extendedstatus: ExtendedStatus
    # postType_extendedstatus: ExtendedStatus
    # actual_street_extendedstatus: ExtendedStatus
    # actual_streetType_extendedstatus: ExtendedStatus
    # actual_houseNum_extendedstatus: ExtendedStatus
    # actual_housePartNum_extendedstatus: ExtendedStatus
    # actual_apartmentsNum_extendedstatus: ExtendedStatus

    class Config:
        extra = Extra.forbid


class DataV3(BaseData):
    public_person: PublicPerson
    responsiblePosition: str
    corruptionAffected: YesNo
    postType: Union[str, NotApplicable]
    postCategory: Union[PostCategory, NotApplicable]


class DataV2(BaseData):
    public_person: Optional[PublicPerson]
    responsiblePosition: Optional[str]
    corruptionAffected: Optional[YesNo]
    postType: Optional[Union[str, NotApplicable]]
    postCategory: Optional[Union[PostCategory, NotApplicable]]


class SubjectInfoStepV3(NACPBaseModel):
    data: DataV3

    class Config:
        extra = Extra.forbid
        title = "Інформація про суб'єкта декларування"


class SubjectInfoStepV2(NACPBaseModel):
    data: DataV2

    class Config:
        extra = Extra.forbid
        title = "Інформація про суб'єкта декларування"
