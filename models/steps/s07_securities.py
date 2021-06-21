from models.general import *
from models.steps.s03_real_estate import Citizen, OwnershipType


SecuritiesType = Literal[
    'Похідні цінні папери (деривативи)',
    'Приватизаційні цінні папери (ваучери тощо)',
    'Боргові цінні папери',
    'Іпотечні цінні папери',
    'Інвестиційні сертифікати',
    'Акції',
    'Інше',
]


class Right(NACPBaseModel):
    rights_id: Optional[PersonInfo]
    ownershipType: OwnershipType
    otherOwnership: Optional[UsefulStr]
    rightBelongs: PersonInfo
    percent_ownership: Optional[Union[BrokenFloat, Unknown]] = Field(alias='percent-ownership')
    citizen: Optional[Citizen]

    ua_company_code: Optional[Union[CompanyCode, Unknown]]
    ua_company_name: Optional[UsefulStr]

    ua_firstname: Optional[UsefulStr]
    ua_lastname: Optional[UsefulStr]
    ua_middlename: Optional[UsefulStr]
    ua_sameRegLivingAddress: Optional[YesNoStrNum]

    ua_birthday: ConfidentialInformation
    ua_regAddressFull: ConfidentialInformation
    ua_taxNumber: ConfidentialInformation

    class Config:
        extra = Extra.forbid


class Data(NACPBaseModel):
    rights: Optional[List[Right]] = Field(description='Optional for V2')
    persons: Optional[Union[PersonInfo, Unknown]]
    persons_date: Optional[Union[DateUK, Unknown]]
    persons_type: Optional[Citizen]
    persons_ua_firstname: Optional[UsefulStr]
    persons_ua_lastname: Optional[UsefulStr]
    persons_ua_middlename: Optional[UsefulStr]
    persons_ua_same_address: Optional[YesNoStrNum]
    persons_ua_company_code: Optional[CompanyCode]
    persons_ua_company_name: Optional[UsefulStr]

    persons_eng_company_address: Optional[UsefulStr]
    persons_eng_company_code: Optional[Unknown]
    persons_eng_company_name: Optional[UsefulStr]
    persons_ukr_company_address: Optional[UsefulStr]
    persons_ukr_company_name: Optional[UsefulStr]

    iteration: Optional[PositiveInt] = Field(description='Optional only for V2')
    person: Optional[PersonInfo]
    typeProperty: SecuritiesType
    subTypeProperty1: Optional[Literal['Облігації підприємств',
                                       'Державні облігації України',
                                       'Ощадні (депозитні) сертифікати']]
    subTypeProperty2: Optional[Literal['Іпотечні заставні', 'Іпотечні облігації']]
    otherObjectType: Optional[Union[UsefulStr, Unknown]]
    amount: Optional[Union[PositiveInt, Unknown]]
    cost: Union[BrokenFloat, Unknown]
    owningDate: Optional[Union[DateUK, Unknown]]

    emitent: Union[PersonInfo, Unknown]
    emitent_type: Optional[Citizen]
    emitent_ukr_fullname: Optional[Unknown]
    emitent_ua_firstname: Optional[UsefulStr]
    emitent_ua_lastname: Optional[UsefulStr]
    emitent_ua_middlename: Optional[UsefulStr]
    emitent_ua_company_code: Optional[Union[CompanyCode, Unknown]]
    emitent_ua_company_name: Optional[Union[UsefulStr, Unknown]]
    emitent_ukr_company_name: Optional[UsefulStr]
    emitent_ukr_company_address: Optional[Union[UsefulStr, Unknown]]
    emitent_ua_sameRegLivingAddress: Optional[YesNoStrNum]

    emitent_ua_actualAddress: Optional[Unknown]
    emitent_eng_fullname: Optional[Unknown]
    emitent_eng_company_address: Optional[Union[UsefulStr, Unknown]]
    emitent_eng_company_code: Optional[Union[CompanyCode, Unknown]]
    emitent_eng_company_name: Optional[UsefulStr]

    emitent_ua_taxNumber: ConfidentialInformation
    emitent_ua_regAddress: ConfidentialInformation
    emitent_ua_birthday: ConfidentialInformation
    persons_ua_birthday: ConfidentialInformation
    persons_ua_reg_address: ConfidentialInformation
    persons_ua_taxNumber: ConfidentialInformation

    class Config:
        extra = Extra.forbid


class SecuritiesStep(NACPBaseModel):
    data: List[Data]

    class Config:
        extra = Extra.forbid
        title = "Цінні папери"
