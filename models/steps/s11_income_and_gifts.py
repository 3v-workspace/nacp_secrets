from models.general import *
from models.steps.s03_real_estate import Citizen, OwnershipType
from models.steps.s04_unfinished_constructions import PersonWhoCare


IncomeType = Literal[
    'Заробітна плата отримана за основним місцем роботи',
    'Дохід від надання майна в оренду',
    'Благодійна допомога',
    'Гонорари та інші виплати згідно з цивільно-правовим правочинами',
    'Страхові виплати',
    'Дохід від відчуження цінних паперів та корпоративних прав',
    'Роялті',
    'Спадщина',
    'Дохід від зайняття незалежною професійною діяльністю',
    'Дохід від відчуження нерухомого майна',
    'Подарунок у грошовій формі',
    'Дохід від відчуження рухомого майна (крім цінних паперів та корпоративних прав)',
    'Дохід від відчуження рухомого майна ( крім цінних паперів та корпоративних прав)',
    'Проценти',
    'Пенсія',
    'Дохід від зайняття підприємницькою діяльністю',
    'Подарунок у негрошовій формі',
    'Дивіденди',
    'Заробітна плата отримана за сумісництвом',
    'Приз',
    'Інше',
]


class RevenueSource(NACPBaseModel):
    revenue_source: PersonInfo
    revenue_source_type: Citizen
    revenue_source_ua_company_code: Unknown
    revenue_source_ua_company_name: UsefulStr

    class Config:
        extra = Extra.forbid


class Right(NACPBaseModel):
    rights_id: Optional[PersonInfo]
    ownershipType: OwnershipType
    otherOwnership: Optional[Union[UsefulStr, Unknown]] = Field(description='Заповнено якщо ownershipType = "Інше"')
    rightBelongs: PersonInfo
    percent_ownership: Optional[Union[BrokenFloat, Unknown]] = Field(alias='percent-ownership')
    citizen: Optional[Citizen]

    ua_company_code: Optional[Union[CompanyCode, Unknown]]
    ua_company_name: Optional[Union[UsefulStr, Unknown]]

    ua_firstname: Optional[Union[UsefulStr, Unknown]]
    ua_lastname: Optional[Union[UsefulStr, Unknown]]
    ua_middlename: Optional[Union[UsefulStr, Unknown]]
    ua_sameRegLivingAddress: Optional[YesNoStrNum]
    ukr_fullname: Optional[Union[UsefulStr, Unknown]]
    eng_fullname: Optional[Union[UsefulStr, Unknown]]

    ua_birthday: ConfidentialInformation
    ua_livingAddressFull: ConfidentialInformation
    ua_regAddressFull: ConfidentialInformation
    ua_taxNumber: ConfidentialInformation

    eng_company_address: Optional[Union[UsefulStr, Unknown]]
    eng_company_code: Optional[Union[CompanyCode, Unknown]]
    eng_company_name: Optional[Union[UsefulStr, Unknown]]
    ukr_company_address: Optional[Union[UsefulStr, Unknown]]
    ukr_company_name: Optional[UsefulStr]

    eng_birthday: ConfidentialInformation
    eng_regAddress: ConfidentialInformation
    eng_taxNumber: ConfidentialInformation
    ukr_actualAddress: ConfidentialInformation

    class Config:
        extra = Extra.forbid


class Data(NACPBaseModel):
    rights: Optional[List[Right]]
    revenue_source: Optional[Dict[conint(gt=2), RevenueSource]]
    incomeSource: Optional[Union[PersonInfo, Unknown]]
    iteration: Optional[PositiveInt] = Field(description='Optional only for V2')
    objectType: Union[IncomeType, Unknown]
    otherObjectType: Optional[Union[UsefulStr, Unknown]] = Field(description='Заповнено якщо objectType = "Інше"')
    person: Optional[PersonInfo]
    person_who_care: Optional[List[PersonWhoCare]]
    sizeIncome: Union[conint(ge=0), Unknown]

    source_citizen: Optional[Union[Citizen, Unknown]]
    source_ua_firstname: Optional[Union[UsefulStr, Unknown]]
    source_ua_lastname: Optional[Union[UsefulStr, Unknown]]
    source_ua_middlename: Optional[Union[UsefulStr, Unknown]]
    source_ukr_fullname: Optional[Union[UsefulStr, Unknown]]
    source_eng_fullname: Optional[Union[UsefulStr, Unknown]]
    source_ua_sameRegLivingAddress: Optional[YesNoStrNum]

    source_ua_company_code: Optional[Union[CompanyCode, Unknown]]
    source_ua_company_name: Optional[Union[UsefulStr, Unknown]]
    source_ukr_company_name: Optional[Union[UsefulStr, Unknown]]
    source_eng_company_address: Optional[Union[UsefulStr, Unknown]]
    source_ukr_company_address: Optional[Union[UsefulStr, Unknown]]
    source_eng_company_code: Optional[Union[CompanyCode, Unknown]]
    source_eng_company_name: Optional[Union[UsefulStr, Unknown]]

    source_ua_actualAddress: ConfidentialInformation
    source_ua_birthday: ConfidentialInformation
    source_ua_regAddress: ConfidentialInformation
    source_ua_taxNumber: ConfidentialInformation

    source_eng_birthday: ConfidentialInformation
    source_eng_regAddress: ConfidentialInformation
    source_eng_taxNumber: ConfidentialInformation
    source_ukr_regAddress: ConfidentialInformation

    class Config:
        extra = Extra.forbid


class IncomeAndGiftsStep(NACPBaseModel):
    data: List[Data]

    class Config:
        extra = Extra.forbid
        title = "Доходи, у тому числі подарунки"
