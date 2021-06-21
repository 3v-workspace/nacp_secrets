from models.general import *
from models.steps.s03_real_estate import Citizen, OwnershipType
from models.steps.s04_unfinished_constructions import PersonWhoCare
from models.steps.s08_corporate_rights import LegalForm


IntangibleAssetsType = Literal[
    'Торгова марка чи комерційне найменування',
    'Криптовалюта',
    'Корисна модель',
    'Авторське право',
    'Винахід',
    'Промисловий зразок',
    'Інше',
]


class Right(NACPBaseModel):
    rights_id: Optional[PersonInfo]
    person: Optional[PersonInfo] = Field(description='V2 field')
    ownershipType: OwnershipType
    otherOwnership: Optional[UsefulStr]
    rightBelongs: PersonInfo
    percent_ownership: Optional[Union[BrokenFloat, Unknown]] = Field(alias='percent-ownership')
    citizen: Optional[Citizen]
    rights_cityPath: City
    ua_city: Optional[CityType]
    ua_company_code: Optional[Union[CompanyCode, Unknown]]
    ua_company_name: Optional[UsefulStr]

    ua_firstname: Optional[UsefulStr]
    ua_lastname: Optional[UsefulStr]
    ua_middlename: Optional[UsefulStr]
    ua_sameRegLivingAddress: Optional[YesNoStrNum]
    ukr_fullname: Optional[UsefulStr]
    eng_fullname: Optional[UsefulStr]

    ua_apartmentsNum: ConfidentialInformation
    ua_houseNum: ConfidentialInformation
    ua_postCode: ConfidentialInformation
    ua_streetType: ConfidentialInformation
    ua_birthday: ConfidentialInformation
    ua_street: ConfidentialInformation
    ua_livingAddressFull: ConfidentialInformation
    ua_regAddressFull: ConfidentialInformation
    ua_taxNumber: ConfidentialInformation
    eng_birthday: ConfidentialInformation
    eng_regAddress: ConfidentialInformation
    eng_taxNumber: ConfidentialInformation
    ukr_actualAddress: ConfidentialInformation

    class Config:
        extra = Extra.forbid


class Data(NACPBaseModel):
    rights: List[Right]
    iteration: Optional[PositiveInt] = Field(description='Optional for V2')
    person: Optional[PersonInfo]
    costDateOrigin: Union[BrokenFloat, Unknown]
    descriptionObject: UsefulStr
    objectType: IntangibleAssetsType
    otherObjectType: Optional[UsefulStr] = Field(description='Заповнено якщо objectType = "Інше"')
    owningDate: Union[DateUK, Unknown]
    countObject: Optional[BrokenFloat]

    class Config:
        extra = Extra.forbid


class IntangibleAssetsStep(NACPBaseModel):
    data: List[Data]

    class Config:
        extra = Extra.forbid
        title = "Нематеріальні активи"
