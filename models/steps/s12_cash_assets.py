from models.general import *
from models.steps.s03_real_estate import Citizen, OwnershipType, BuildType
from models.steps.s04_unfinished_constructions import PersonWhoCare
from models.steps.s08_corporate_rights import LegalForm

CashAssetsType = Literal[
    'Готівкові кошти',
    'Кошти, розміщені на банківських рахунках',
    'Кошти, позичені третім особам',
    'Внески до кредитних спілок та інших небанківських фінансових установ',
    'Активи у дорогоцінних (банківських) металах',
    'Інше',
]

Organization = Literal[
    'j',
    'Інша юридична особа',
    'Інша фізична особа',
]


class Right(NACPBaseModel):
    rights_id: Optional[PersonInfo]
    # # person: Optional[PersonInfo] = Field(description='V2 field')
    ownershipType: OwnershipType
    otherOwnership: Optional[Union[UsefulStr, Unknown]] = Field(description='Заповнено якщо ownershipType = "Інше"')
    rightBelongs: PersonInfo
    percent_ownership: Optional[Union[BrokenFloat, Unknown]] = Field(alias='percent-ownership')
    citizen: Optional[Citizen]
    rights_cityPath: Optional[City]
    ua_company_code: Optional[Union[CompanyCode, Unknown]]
    ua_company_name: Optional[Union[UsefulStr, Unknown]]

    ua_firstname: Optional[Union[UsefulStr, Unknown]]
    ua_lastname: Optional[Union[UsefulStr, Unknown]]
    ua_middlename: Optional[Union[UsefulStr, Unknown]]
    ukr_fullname: Optional[Union[UsefulStr, Unknown]]
    eng_fullname: Optional[Union[UsefulStr, Unknown]]
    ua_buildType: Optional[Union[BuildType, Unknown]]
    ua_city: Optional[CityType]
    ua_sameRegLivingAddress: Optional[YesNoStrNum]

    eng_company_address: Optional[Union[UsefulStr, Unknown]]
    eng_company_code: Optional[Union[CompanyCode, Unknown]]
    eng_company_name: Optional[Union[UsefulStr, Unknown]]
    ukr_company_address: Optional[Union[UsefulStr, Unknown]]
    ukr_company_name: Optional[UsefulStr]

    ua_birthday: ConfidentialInformation
    ua_postCode: ConfidentialInformation
    ua_houseNum: ConfidentialInformation
    ua_housePartNum: ConfidentialInformation
    ua_street: ConfidentialInformation
    ua_streetType: ConfidentialInformation
    ua_livingAddressFull: ConfidentialInformation
    ua_regAddressFull: ConfidentialInformation
    ua_taxNumber: ConfidentialInformation
    ua_apartmentsNum: ConfidentialInformation
    eng_birthday: ConfidentialInformation
    eng_regAddress: ConfidentialInformation
    eng_taxNumber: ConfidentialInformation
    ukr_actualAddress: ConfidentialInformation


    class Config:
        extra = Extra.forbid


class Data(NACPBaseModel):
    rights: Optional[List[Right]] = Field(description='Optional for V2')
    person: Optional[PersonInfo]
    iteration: Optional[PositiveInt] = Field(description='Optional for V2')
    objectType: CashAssetsType
    otherObjectType: Optional[Union[UsefulStr, Unknown]]

    assetsCurrency: Union[Currency, Unknown]
    sizeAssets: Union[int, Unknown]

    organization_type: Optional[Citizen]
    organization_type1: Optional[Union[Citizen, Unknown]]
    organization_type2: Optional[Union[Citizen, Unknown]]
    organization: Optional[Union[Organization, Unknown]]
    organization_eng_company_address: Optional[Union[UsefulStr, Unknown]]
    organization_eng_company_code: Optional[Union[CompanyCode, Unknown]]
    organization_eng_company_name: Optional[Union[UsefulStr, Unknown]]
    organization_ua_company_code: Optional[Union[CompanyCode, Unknown]]
    organization_ua_company_name: Optional[Union[UsefulStr, Unknown]]
    organization_ukr_company_address: Optional[Union[UsefulStr, Unknown]]
    organization_ukr_company_name: Optional[Union[UsefulStr, Unknown]]

    debtor_ua_firstname: Optional[Union[UsefulStr, Unknown]]
    debtor_ua_lastname: Optional[Union[UsefulStr, Unknown]]
    debtor_ua_middlename: Optional[Union[UsefulStr, Unknown]]
    debtor_eng_fullname: Optional[Union[UsefulStr, Unknown]]
    debtor_ukr_fullname: Optional[Union[UsefulStr, Unknown]]
    debtor_ua_sameRegLivingAddress: Optional[YesNoStrNum]

    debtor_ua_regAddress: ConfidentialInformation
    debtor_ua_birthday: ConfidentialInformation
    debtor_ua_taxNumber: ConfidentialInformation
    debtor_ua_actualAddress: ConfidentialInformation
    debtor_eng_birthday: ConfidentialInformation
    debtor_ukr_regAddress: ConfidentialInformation
    debtor_eng_taxNumber: ConfidentialInformation
    debtor_eng_regAddress: ConfidentialInformation

    class Config:
        extra = Extra.forbid


class CashAssetsStep(NACPBaseModel):
    data: List[Data]

    class Config:
        extra = Extra.forbid
        title = "Грошові активи"
