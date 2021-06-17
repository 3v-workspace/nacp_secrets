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
    rightBelongs: PersonInfo
    percent_ownership: Optional[Union[constr(regex=r'^\d+([,.]\d+)?$'), Unknown]] = Field(
        title='percent-ownership (%)', alias='percent-ownership',
        description='Приклади: "33,58", "33.58", "11"',
    )
    citizen: Optional[Citizen]

    ua_company_code: Optional[constr(regex=r'^(\d{8})$')]
    ua_company_name: Optional[UsefulStr]

    ua_firstname: Optional[UsefulStr]
    ua_lastname: Optional[UsefulStr]
    ua_middlename: Optional[UsefulStr]
    ua_sameRegLivingAddress: Optional[YesNoStrNum]

    ua_birthday: ConfidentialInformation
    ua_livingAddressFull: ConfidentialInformation
    ua_regAddressFull: ConfidentialInformation
    ua_taxNumber: ConfidentialInformation

    class Config:
        extra = Extra.forbid


class Data(NACPBaseModel):
    rights: List[Right]
    iteration: Optional[PositiveInt] = Field(description='Optional for V2')
    person: Optional[PersonInfo]
    costDateOrigin: Union[constr(regex=r'^\d+$'), Unknown]
    descriptionObject: UsefulStr
    objectType: IntangibleAssetsType
    otherObjectType: Optional[UsefulStr] = Field(description='Заповнено якщо objectType = "Інше"')
    owningDate: Union[DateUK, Unknown]
    countObject: Optional[constr(regex=r'^\d+([,]\d+)?$')]

    class Config:
        extra = Extra.forbid


class IntangibleAssetsStep(NACPBaseModel):
    data: List[Data]

    class Config:
        extra = Extra.forbid
        title = "Нематеріальні активи"
