from models.general import *
from models.steps.s03_real_estate import Citizen, OwnershipType


SecuritiesType = Literal[
    'Похідні цінні папери (деривативи)',
    'Приватизаційні цінні папери (ваучери тощо)',
    'Боргові цінні папери',
    'Іпотечні цінні папери',
    'Інвестиційні сертифікати',
    'Акції',
    'Акції',
    'Інше',
]


class Right(NACPBaseModel):
    rights_id: Optional[PersonInfo]
    ownershipType: OwnershipType
    rightBelongs: PersonInfo
    percent_ownership: Optional[Union[constr(regex=r'^\d+([,.]\d+)?$'), Unknown]] = Field(
        title='percent-ownership (%)', alias='percent-ownership',
        description='Приклади: "33,58", "33.58", "11"',
    )
    citizen: Optional[Citizen]

    ua_company_code: Optional[constr(regex=r'^(\d{5})$')]
    ua_company_name: Optional[UsefulStr]

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
    persons_ua_company_code: Optional[constr(regex=r'^(\d{8})$')]
    persons_ua_company_name: Optional[UsefulStr]

    persons_eng_company_address: Optional[UsefulStr]
    persons_eng_company_code: Optional[Unknown]
    persons_eng_company_name: Optional[UsefulStr]
    persons_ukr_company_address: Optional[UsefulStr]
    persons_ukr_company_name: Optional[UsefulStr]

    iteration: Optional[PositiveInt] = Field(description='Optional only for V2')
    person: Optional[PersonInfo]
    typeProperty: SecuritiesType
    subTypeProperty1: Optional[Literal['Облігації підприємств', 'Державні облігації України']]
    subTypeProperty2: Optional[Literal['Іпотечні заставні', 'Іпотечні облігації']]
    otherObjectType: Optional[Union[UsefulStr, Unknown]]
    amount: Optional[Union[PositiveInt, Unknown]]
    cost: Union[constr(regex=r'^\d+([,.]\d+)?$'), Unknown]
    owningDate: Optional[Union[DateUK, Unknown]]

    emitent: Union[PersonInfo, Unknown]
    emitent_type: Optional[Citizen]
    emitent_ukr_fullname: Optional[Unknown]
    emitent_ua_company_code: Optional[Union[constr(regex=r'^(\d{8,9}|\d{5})$', max_length=9, min_length=5), Unknown]]
    emitent_ua_company_name: Optional[Union[UsefulStr, Unknown]]
    emitent_ukr_company_name: Optional[UsefulStr]
    emitent_ukr_company_address: Optional[Union[UsefulStr, Unknown]]

    emitent_eng_fullname: Optional[Unknown]
    emitent_eng_company_address: Optional[Union[UsefulStr, Unknown]]
    emitent_eng_company_code: Optional[Union[UsefulStr, Unknown]]
    emitent_eng_company_name: Optional[UsefulStr]

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
