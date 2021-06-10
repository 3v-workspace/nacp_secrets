from datetime import datetime, date
from typing import List, Optional, Union, TypeVar, Literal
from enum import Enum, IntEnum
from pydantic import BaseModel, Field, Extra, constr
from models.general import NoDataEnum, CityType, YesNo, NoData, YesNoNumber, ExtendedStatus, City, \
    ConfidentialInformation, NotApplicable, EmptyString


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


class Data(BaseModel):
    firstname: str
    lastname: str
    middlename: str

    changedName: YesNoNumber
    previous_firstname: Optional[str]
    previous_lastname: Optional[str]
    previous_middlename: Optional[str]
    previous_middlename_extendedstatus: ExtendedStatus

    taxNumber: ConfidentialInformation
    passport: ConfidentialInformation
    passport_extendedstatus: ExtendedStatus
    birthday: ConfidentialInformation
    responsiblePosition: str
    public_person: PublicPerson
    public_person_extendedstatus: ExtendedStatus
    sameRegLivingAddress: YesNoNumber
    workPlace: str
    workPost: str
    unzr: ConfidentialInformation
    unzr_extendedstatus: ExtendedStatus
    corruptionAffected: YesNo

    postCategory: Union[PostCategory, NotApplicable]
    postCategory_extendedstatus: ExtendedStatus
    postType: Union[str, NotApplicable]
    postType_extendedstatus: ExtendedStatus
    postCode: ConfidentialInformation

    actual_apartmentsNum: Optional[Union[ConfidentialInformation, EmptyString]]
    actual_apartmentsNum_extendedstatus: ExtendedStatus
    actual_city: Optional[ConfidentialInformation]
    actual_cityPath: Optional[ConfidentialInformation]
    actual_cityType: Optional[CityType]
    actual_district: Optional[ConfidentialInformation]
    actual_street: Optional[ConfidentialInformation]
    actual_street_extendedstatus: ExtendedStatus
    actual_postCode: Optional[ConfidentialInformation]
    actual_region: Optional[ConfidentialInformation]
    actual_streetType: Optional[ConfidentialInformation]
    actual_streetType_extendedstatus: ExtendedStatus
    actual_houseNum: Optional[ConfidentialInformation]
    actual_houseNum_extendedstatus: ExtendedStatus
    actual_country: Optional[int]
    actual_housePartNum: Optional[Union[ConfidentialInformation, Literal['']]]
    actual_housePartNum_extendedstatus: ExtendedStatus

    eng_actualAddress: Optional[ConfidentialInformation]
    eng_actualPostCode: Optional[ConfidentialInformation]
    ukr_actualAddress: Optional[ConfidentialInformation]

    region: ConfidentialInformation
    streetType: ConfidentialInformation
    streetType_extendedstatus: ExtendedStatus
    street: ConfidentialInformation
    district: Optional[ConfidentialInformation]
    city: City
    city_extendedstatus: ExtendedStatus
    country: int
    cityType: CityType
    housePartNum: ConfidentialInformation = Field(title='Номер корпусу')
    housePartNum_extendedstatus: ExtendedStatus
    apartmentsNum: ConfidentialInformation
    apartmentsNum_extendedstatus: ExtendedStatus
    cityPath: ConfidentialInformation
    houseNum: ConfidentialInformation
    houseNum_extendedstatus: ExtendedStatus

    class Config:
        extra = Extra.forbid


class SubjectInfoStep(BaseModel):
    data: Data

    class Config:
        extra = Extra.forbid
        title = "Інформація про суб'єкта декларування"
