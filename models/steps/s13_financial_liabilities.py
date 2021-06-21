from models.general import *
from models.steps.s03_real_estate import Citizen, OwnershipType, BuildType
from models.steps.s04_unfinished_constructions import PersonWhoCare
from models.steps.s08_corporate_rights import LegalForm


FinancialLiabilitiesTypes = Literal[
    "Кошти, позичені суб'єкту декларування або члену його сім'ї іншими особами",
    'Розмір сплачених коштів в рахунок основної суми позики (кредиту)',
    'Розмір сплачених коштів в рахунок процентів за позикою (кредитом)',
    'Отримані кредити',
    'Отримані позики',
    "Зобов'язання за договорами лізингу",
    "Зобов'язання за договорами страхування",
    "Зобов'язання за договорами недержавного пенсійного забезпечення",
    "Несплачені податкові зобов'язання",
    'Інше',
]


GuarantorRealtyTypes = Literal[
    'Автомобіль легковий',
    'Житловий будинок',
    'Сільськогосподарська техніка',
    'Квартира',
    'Земельна ділянка',
    'житловий будинок',
    'Офіс',
    'Персональні або домашні електронні пристрої',
    'Інше',
]


class Guarantor(NACPBaseModel):
    guarantor_id: Optional[PersonInfo]
    guarantor: PersonInfo
    guarantor_type: Optional[Citizen]
    guarantor_exist: Optional[YesNoStrNum]

    guarantor_ua_firstname: Optional[UsefulStr]
    guarantor_ua_lastname: Optional[UsefulStr]
    guarantor_ua_middlename: Optional[UsefulStr]
    guarantor_eng_fullname: Optional[UsefulStr]
    guarantor_ukr_fullname: Optional[UsefulStr]

    guarantor_ua_company_code: Optional[CompanyCode]
    guarantor_ua_company_name: Optional[UsefulStr]

    guarantor_ua_sameRegLivingAddress: Optional[YesNoStrNum]

    guarantor_ua_actualAddress: ConfidentialInformation
    guarantor_ua_birthday: ConfidentialInformation
    guarantor_ua_regAddress: ConfidentialInformation
    guarantor_ua_taxNumber: ConfidentialInformation
    guarantor_eng_birthday: ConfidentialInformation
    guarantor_eng_regAddress: ConfidentialInformation
    guarantor_eng_taxNumber: ConfidentialInformation
    guarantor_ukr_regAddress: ConfidentialInformation

    class Config:
        extra = Extra.forbid


class GuarantorRealty(NACPBaseModel):
    guarantor_realty_id: Optional[PositiveInt]
    guarantor_realty_exist: Optional[Literal['true', 'false', '1', '0']]
    city: City
    realty_cost: Optional[PositiveInt]
    realty_country: PositiveInt
    realty_objectType: GuarantorRealtyTypes
    realty_otherObjectType: Optional[UsefulStr]
    realty_ua_cityPath: Optional[Union[City, int]]
    realty_ua_cityType: Optional[CityType]
    realty_ua_buildType: Optional[BuildType]

    realty_rights: Optional[PersonInfo]
    realty_rights_type: Optional[Citizen]
    realty_rights_ua_firstname: Optional[UsefulStr]
    realty_rights_ua_lastname: Optional[UsefulStr]
    realty_rights_ua_middlename: Optional[UsefulStr]
    realty_rights_ua_sameRegLivingAddress: Optional[YesNoStrNum]
    realty_rights_ua_company_code: Optional[CompanyCode]
    realty_rights_ua_company_name: Optional[UsefulStr]
    realty_rights_cityPath: City

    realty_rights_ua_taxNumber: ConfidentialInformation
    realty_rights_ua_regAddress: ConfidentialInformation
    realty_rights_ua_birthday: ConfidentialInformation
    realty_rights_ua_actualAddress: ConfidentialInformation
    district: ConfidentialInformation
    realty_ua_apartmentsNum: ConfidentialInformation
    realty_ua_houseNum: ConfidentialInformation
    realty_ua_housePartNum: ConfidentialInformation
    realty_ua_postCode: ConfidentialInformation
    realty_ua_street: Optional[Union[UsefulStr, Literal['[Конфіденційна інформація]', '[Не застосовується]']]]
    realty_ua_streetType: Optional[Union[UsefulStr, Literal['[Конфіденційна інформація]', '[Не застосовується]']]]
    region: ConfidentialInformation
    realty_postCode: ConfidentialInformation

    class Config:
        extra = Extra.forbid


class Data(NACPBaseModel):
    # rights: Optional[List[Right]] = Field(description='Optional for V2')
    person: Optional[PersonInfo]
    iteration: Optional[PositiveInt] = Field(description='Для V2 може бути пустим')
    margin_emitent: Union[PersonInfo, Unknown] = Field(alias='margin-emitent')
    objectType: FinancialLiabilitiesTypes
    otherObjectType: Optional[Union[UsefulStr, Unknown]]
    person_who_care: Optional[List[PersonWhoCare]]
    credit_paid: Optional[Union[int, Unknown]]
    credit_percent_paid: Optional[Union[int, Unknown]]
    credit_rest: Optional[Union[int, Unknown]]
    sizeObligation: Union[PositiveInt, Unknown]
    currency: Union[Currency, Unknown]
    dateOrigin: Union[DateUK, Unknown]
    emitent_citizen: Optional[Citizen]
    emitent_ua_firstname: Optional[UsefulStr]
    emitent_ua_lastname: Optional[UsefulStr]
    emitent_ua_middlename: Optional[UsefulStr]
    emitent_ukr_fullname: Optional[UsefulStr]
    emitent_eng_fullname: Optional[UsefulStr]
    emitent_ua_company_code: Optional[Union[CompanyCode, Unknown]]
    emitent_ua_company_name: Optional[UsefulStr]
    emitent_eng_company_name: Optional[UsefulStr]
    emitent_eng_company_code: Optional[Union[CompanyCode, Unknown]]
    emitent_eng_company_address: Optional[Union[UsefulStr, Unknown]]
    emitent_ukr_company_address: Optional[Union[UsefulStr, Unknown]]
    emitent_ukr_company_name: Optional[UsefulStr]
    emitent_ua_sameRegLivingAddress: Optional[YesNoStrNum]
    guarantor_exist_: Optional[YesNoStrNum]
    guarantor_realty_exist_: Optional[Union[YesNoStrNum]]
    guarantor: Optional[List[Guarantor]]
    guarantor_realty: Optional[List[GuarantorRealty]]

    emitent_ua_actualAddress: ConfidentialInformation
    emitent_ua_birthday: ConfidentialInformation
    emitent_ua_regAddress: ConfidentialInformation
    emitent_ua_taxNumber: ConfidentialInformation
    emitent_eng_birthday: ConfidentialInformation
    emitent_eng_regAddress: ConfidentialInformation
    emitent_eng_taxNumber: ConfidentialInformation
    emitent_ukr_regAddress: ConfidentialInformation

    class Config:
        extra = Extra.forbid


class FinancialLiabilitiesStep(NACPBaseModel):
    data: List[Data]

    class Config:
        extra = Extra.forbid
        title = "Фінансові зобов'язання"
