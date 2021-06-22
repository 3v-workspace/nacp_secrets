from models.general import *
from models.steps.s03_real_estate import Citizen, OwnershipType


VehiclePropertyType = Literal[
    'Водний засіб',
    'Автомобіль вантажний',
    'Сільськогосподарська техніка',
    'Автомобіль легковий',
    'Мотоцикл (мопед)',
    'Повітряний засіб',
    'Інше',
]


class Right(NACPBaseModel):
    rights_id: Optional[PersonInfo]
    ownershipType: OwnershipType
    otherOwnership: Optional[Union[UsefulStr, Unknown]]
    rightBelongs: PersonInfo
    percent_ownership: Optional[Union[BrokenFloat, Unknown]] = Field(alias='percent-ownership')
    citizen: Optional[Citizen]
    ua_firstname: Optional[Union[UsefulStr, Unknown]]
    ua_lastname: Optional[Union[UsefulStr, Unknown]]
    ua_middlename: Optional[Union[UsefulStr, Unknown]]
    eng_fullname: Optional[Union[UsefulStr, Unknown]]
    ukr_fullname: Optional[Union[UsefulStr, Unknown]]
    ua_sameRegLivingAddress: Optional[YesNoStrNum]

    ua_company_code: Optional[Union[CompanyCode, Unknown]]
    ua_company_name: Optional[UsefulStr]

    ua_buildType: Optional[Unknown]
    rights_cityPath: Optional[City]
    ua_city: Optional[Union[CityType, Unknown]]

    ukr_actualAddress: ConfidentialInformation
    ukr_actualAddress: ConfidentialInformation
    eng_regAddress: ConfidentialInformation
    eng_taxNumber: ConfidentialInformation
    eng_birthday: ConfidentialInformation
    ua_streetType: ConfidentialInformation
    ua_street: ConfidentialInformation
    ua_postCode: ConfidentialInformation
    ua_housePartNum: ConfidentialInformation
    ua_houseNum: ConfidentialInformation
    ua_birthday: ConfidentialInformation
    ua_livingAddressFull: ConfidentialInformation
    ua_regAddressFull: ConfidentialInformation
    ua_taxNumber: ConfidentialInformation
    ua_apartmentsNum: ConfidentialInformation

    class Config:
        extra = Extra.forbid


class Data(NACPBaseModel):
    rights: Optional[List[Right]]
    person: Optional[PersonInfo]
    iteration: Optional[PositiveInt]
    brand: Union[UsefulStr, Unknown] = Field(title='Марка')
    model: Union[UsefulStr, Unknown] = Field(title='Модель')
    objectType: VehiclePropertyType = Field(title='Вид майна')
    otherObjectType: Optional[Union[UsefulStr, Unknown]]
    costDate: Union[PositiveInt, Unknown] = Field(
        title='ВАРТІСТЬ НА ДАТУ НАБУТТЯ У ВЛАСНІСТЬ, ВОЛОДІННЯ ЧИ КОРИСТУВАННЯ АБО ЗА ОСТАННЬОЮ ГРОШОВОЮ ОЦІНКОЮ'
    )
    owningDate: Union[DateUK, Unknown] = Field(title='Дата набуття права')
    graduationYear: Union[conint(gt=1811, lt=date.today().year), Unknown] = Field(title='Рік випуску')

    object_identificationNumber: ConfidentialInformation = Field(title='Ідентифікаційний номер (VIN-код, номер шасі)')

    class Config:
        extra = Extra.forbid


class VehiclePropertyStep(NACPBaseModel):
    data: List[Data]

    class Config:
        extra = Extra.forbid
        title = "Цінне рухоме майно - транспортні засоби"
