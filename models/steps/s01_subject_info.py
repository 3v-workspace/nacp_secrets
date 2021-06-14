from models.general import *


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


class Data(NACPBaseModel):
    firstname: UsefulStr
    lastname: UsefulStr
    middlename: Optional[UsefulStr]
    changedName: YesNoStrNum
    previous_firstname: Optional[UsefulStr]
    previous_lastname: Optional[UsefulStr]
    previous_middlename: Optional[Union[UsefulStr, Unknown]]
    public_person: Optional[PublicPerson]
    responsiblePosition: Optional[UsefulStr]
    corruptionAffected: Optional[YesNo]
    postType: Optional[Union[UsefulStr, Unknown]]
    postCategory: Optional[Union[PostCategory, Unknown]]
    sameRegLivingAddress: YesNoStrNum
    workPlace: UsefulStr
    workPost: UsefulStr
    actual_cityType: Optional[CityType]
    actual_country: Optional[int]
    city: City
    country: int
    cityType: CityType

    taxNumber: ConfidentialInformation
    passport: ConfidentialInformation
    birthday: ConfidentialInformation
    unzr: ConfidentialInformation = Field(title='Унікальний номер запису в Єдиному державному демографічному реєстрі')
    postCode: ConfidentialInformation
    actual_housePartNum: ConfidentialInformation
    actual_apartmentsNum: ConfidentialInformation
    actual_city: ConfidentialInformation
    actual_cityPath: ConfidentialInformation
    actual_district: ConfidentialInformation
    actual_street: ConfidentialInformation
    actual_postCode: ConfidentialInformation
    actual_region: ConfidentialInformation
    actual_streetType: ConfidentialInformation
    actual_houseNum: ConfidentialInformation
    eng_actualAddress: ConfidentialInformation
    eng_actualPostCode: ConfidentialInformation
    ukr_actualAddress: ConfidentialInformation
    region: ConfidentialInformation
    streetType: ConfidentialInformation
    street: ConfidentialInformation
    district: ConfidentialInformation
    housePartNum: ConfidentialInformation = Field(title='Номер корпусу')
    apartmentsNum: ConfidentialInformation
    cityPath: ConfidentialInformation
    houseNum: ConfidentialInformation

    class Config:
        extra = Extra.forbid


class SubjectInfoStep(NACPBaseModel):
    data: Data

    class Config:
        extra = Extra.forbid
        title = "Інформація про суб'єкта декларування"
