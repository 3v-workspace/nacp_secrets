from models.general import *
from models.steps.s03_real_estate import Citizen, OwnershipType


LegalForm = Literal[
    'АДВОКАТСЬКЕ ОБ\'ЄДНАННЯ',
    'Адвокатське об\'єднання',
    'Обслуговуючий житлово-будівельний кооператив',
    'Сильське споживче товариство',
    'Товарна біржа',
    'Громадська організація',
    'власність',
    'Приватна',
    'юридична особа',
    'комунальна',
    'Частна',
    'приватна',
    'споживчий кооператив',
    'громадська організація',
    'ОБСЛУГОВУЮЧИЙ КООПЕРАТИВ',
    'Фермерське господарство',
    'фермерське господарство',
    'фермерське господарство ',
    'ФЕРМЕРСЬКЕ ГОСПОДАРСТВО',
    'ТОВАРИСТВО',
    'товариство',
    'Товариство',
    'товариство з обмеженой відповідальністю',
    'товариство з обмеженою відповідальтністю',
    'товариство з обмеженою відповідальністю ',
    'товарситво з обмеженою відповідальністю',
    'товариство з обмеженою відповідальністю',
    'Товариство з обмеженою відповідальністю',
    'Товариство з обмеженою відповідальнісю',
    'Товариство з обмеженою відповідальністю ',
    'ТОВАРИСТВО З ОБМЕЖЕНОЮ ВІДПОВІДАЛЬНІСТЮ',
    'Селянське фермерське господарство',
    'селянське фермерське господарство',
    'Товариство з додатковою відповідальністю',
    'товариство з додатковою відповідальністю',
    'приватне підприємство',
    'АДВОКАТСЬКЕ ОБЄДНАННЯ',
    'СІЛЬСЬКОГОСПОДАРСЬКИЙ ОБСЛУГОВУЮЧИЙ КООПЕРАТИВ',
    'Благодійна організація',
    'ТОВ',
    'ТОВ ',
    'МПП',
    'ПП',
    'ФГ',
    'ТзОВ',
    'ТДВ',
    'СТОВ',
    'ФОП',
    'ПАТ',
    'Приватне підприємство',
    'Приватне підприємство ',
    'Приватне Підприємство',
    'ПРИВАТНЕ ПІДПРИЄМСТВО',
    'ПРИВАТНИЙ ПІДПРИЄМЕЦЬ',
    'Споживче товариство',
    'політична партія',
    'акціонерне товариство',
    'Закрите акціонерне товариство',
    'ЖИТЛОВО-БУДІВЕЛЬНИЙ КООПЕРАТИВ',
    'приватна ',
    'ІНШІ ОРГАНІЗАЦІЙНО-ПРАВОВІ ФОРМИ',
    'ПСП ім.Шевченка',
    'повне товариство',
    'пай',
    'Фізична особа-підприємець',
    'Сільськогосподарський виробничий кооператив',
    'інші організаційно-правові форми',
    'компанія',
    'Адвокатське бюро',
    'колективна',
    'Приватна організація, установа, заклад',
    'Адвокатське об\'єднання ',
]


class Right(NACPBaseModel):
    rights_id: Optional[PersonInfo]
    ownershipType: OwnershipType
    otherOwnership: Optional[UsefulStr] = Field(description='Заповнено якщо ownershipType = "Інше"')
    rightBelongs: PersonInfo
    percent_ownership: Optional[Union[BrokenFloat, Unknown]] = Field(alias='percent-ownership')
    citizen: Optional[Citizen]

    ua_company_code: Optional[Union[CompanyCode, Unknown]]
    ua_company_name: Optional[Union[UsefulStr, Unknown]]

    ua_firstname: Optional[Union[UsefulStr, Unknown]]
    ua_lastname: Optional[Union[UsefulStr, Unknown]]
    ua_middlename: Optional[Union[UsefulStr, Unknown]]

    ua_sameRegLivingAddress: Optional[YesNoStrNum]

    eng_company_address: Optional[Unknown]
    eng_company_code: Optional[Unknown]
    eng_company_name: Optional[Unknown]
    eng_fullname: Optional[Union[UsefulStr, Unknown]]
    ukr_company_address: Optional[Unknown]
    ukr_company_name: Optional[Unknown]
    ukr_fullname: Optional[UsefulStr]
    ua_city: Optional[Unknown]

    ua_street: ConfidentialInformation
    ua_postCode: ConfidentialInformation
    ua_housePartNum: ConfidentialInformation
    ua_houseNum: ConfidentialInformation
    ua_apartmentsNum: ConfidentialInformation
    eng_birthday: ConfidentialInformation
    eng_regAddress: ConfidentialInformation
    eng_taxNumber: ConfidentialInformation
    ukr_actualAddress: ConfidentialInformation
    ua_birthday: ConfidentialInformation
    ua_livingAddressFull: ConfidentialInformation
    ua_regAddressFull: ConfidentialInformation
    ua_taxNumber: ConfidentialInformation

    class Config:
        extra = Extra.forbid


class Data(NACPBaseModel):
    rights: Optional[List[Right]] = Field(description='Optional for V2')
    iteration: Optional[PositiveInt] = Field(description='Optional only for V2')
    person: Optional[PersonInfo]
    name: Union[UsefulStr, Unknown]
    en_name: Optional[Union[UsefulStr, Unknown]]
    legalForm: Union[LegalForm, UsefulStr, Unknown]
    corporate_rights_company_code: Optional[Union[CompanyCode, Unknown]]
    cost: Union[BrokenFloat, Unknown] = \
        Field(description='Examples: "38.", "38.1", "38", "38,1"')

    cost_percent: Union[BrokenFloat, Unknown]
    is_transferred: Optional[Union[Literal['Передано', 'Не передано'], Unknown]]
    country: Union[PositiveInt, Unknown]
    owningDate: Optional[Union[DateUK, Unknown]]

    regNumber: ConfidentialInformation

    class Config:
        extra = Extra.forbid


class CorporateRightsStep(NACPBaseModel):
    data: List[Data]

    class Config:
        extra = Extra.forbid
        title = "Корпоративні права"
