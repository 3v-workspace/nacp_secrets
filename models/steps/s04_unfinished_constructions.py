from models.general import *
from models.steps.s03_real_estate import RealEstateType, Citizen, OwnershipType, BuildType


class PersonWhoCare(NACPBaseModel):
    person: PersonInfo
    person_id: Optional[int]

    citizen: Optional[Citizen]

    ua_firstname: Optional[Union[UsefulStr, Unknown]]
    ua_lastname: Optional[Union[UsefulStr, Unknown]]
    ua_middlename: Optional[Union[UsefulStr, Unknown]]

    ua_sameRegLivingAddress: Optional[YesNoStrNum]
    ua_company_code: Optional[Union[constr(regex=r'^\d{8}$', max_length=10, min_length=8), Unknown]]
    ua_company_name: Optional[UsefulStr]

    ua_regAddressFull: ConfidentialInformation
    ua_livingAddressFull: ConfidentialInformation
    ua_taxNumber: ConfidentialInformation
    ua_birthday: ConfidentialInformation

    class Config:
        extra = Extra.forbid


class Right(NACPBaseModel):
    ownershipType: OwnershipType
    otherOwnership: Optional[Union[UsefulStr, Unknown]]
    rightBelongs: Union[PersonInfo, Unknown]
    rights_id: Optional[int]
    percent_ownership: Optional[Union[constr(regex=r'^\d+([,.]\d+)?$'), Unknown]] = Field(
        title='percent-ownership (%)', alias='percent-ownership',
        description='Приклади: "33,58", "33.58", "11"',
    )

    citizen: Optional[Citizen]
    ua_company_code: Optional[Union[constr(regex=r'^\d{8}$', max_length=10, min_length=8), Unknown]]
    ua_company_name: Optional[UsefulStr]

    ua_firstname: Optional[Union[UsefulStr, Unknown]]
    ua_lastname: Optional[Union[UsefulStr, Unknown]]
    ua_middlename: Optional[Union[UsefulStr, Unknown]]
    ua_sameRegLivingAddress: Optional[YesNoStrNum]

    ukr_fullname: Optional[Union[UsefulStr, Unknown]]
    eng_fullname: Optional[UsefulStr]

    eng_birthday: ConfidentialInformation
    eng_regAddress: ConfidentialInformation
    eng_taxNumber: ConfidentialInformation
    ukr_actualAddress: ConfidentialInformation
    ua_regAddressFull: ConfidentialInformation
    ua_livingAddressFull: ConfidentialInformation
    ua_taxNumber: ConfidentialInformation
    ua_birthday: ConfidentialInformation

    class Config:
        extra = Extra.forbid


class Data(NACPBaseModel):
    rights: Optional[List[Right]] = Field(description='Може не бути в схемі V2')
    iteration: Optional[int] = Field(description='Для V2 може бути пустим')
    person: Optional[PersonInfo]
    person_who_care: Optional[List[PersonWhoCare]]

    belongsSubjectOfDeclaration: YesNoStrNum
    country: int
    city: City
    objectType: RealEstateType
    otherObjectType: Optional[Union[UsefulStr, Unknown]] = \
        Field(description='Заповнюється якщо objectType=Інше')
    exploitation: YesNoStrNum
    ua_cityType: Optional[CityType]
    unfinishConstruct: YesNoStrNum
    dontRegistered: YesNoStrNum
    builtMaterialsOrFunds: YesNoStrNum
    totalArea: Union[constr(regex=r'^\d+([,.]\d+)?$'), Unknown] = Field(
        title='Загальна площа М2', description='Приклади: "109,8", "109.8", "1523"'
    )
    ua_buildType: Optional[BuildType]
    addition_company_code: Optional[Union[constr(regex=r'^\d{8}$'), Unknown]]
    addition_company_name: Optional[UsefulStr]
    thirdOwner_citizen: Optional[Citizen]

    # Optional
    eng_regNumber: ConfidentialInformation
    loc_engLivingAddress: ConfidentialInformation
    loc_ukrLivingAddress: ConfidentialInformation
    postCode: ConfidentialInformation
    builtOnTerritoryOrRent: Optional[YesNoStrNum]
    flag_thirdOwner: Optional[YesNoInt]
    isThirdOwner: Optional[YesNoStrNum]
    actualAddressEqualRegAddress: Optional[YesNoStrNum]
    addition_eng_fullName: Optional[UsefulStr]
    addition_ua_fullName: Optional[UsefulStr]

    # ConfidentialInformation
    addition_actualAddress: ConfidentialInformation
    addition_birthday: ConfidentialInformation
    addition_firstname: Optional[Union[UsefulStr, Unknown]]
    addition_lastname: Optional[Union[UsefulStr, Unknown]]
    addition_middlename: Optional[Union[UsefulStr, Unknown]]
    addition_regAddress: ConfidentialInformation
    addition_taxNumber: ConfidentialInformation
    addition_eng_actualAddress: ConfidentialInformation
    addition_eng_taxNumber: ConfidentialInformation
    addition_ua_actualAddress: ConfidentialInformation
    addition_eng_birthday: ConfidentialInformation

    ua_street: ConfidentialInformation
    ua_apartmentsNum: ConfidentialInformation
    ua_postCode: ConfidentialInformation
    ua_houseNum: ConfidentialInformation
    ua_housePartNum: ConfidentialInformation
    ua_streetType: ConfidentialInformation
    cadNumber: ConfidentialInformation
    regNumber: ConfidentialInformation
    cityPath: ConfidentialInformation
    district: ConfidentialInformation
    region: ConfidentialInformation


    class Config:
        extra = Extra.forbid


class UnfinishedConstructionsStep(NACPBaseModel):
    data: List[Data]

    class Config:
        extra = Extra.forbid
        title = "Об'єкти незавершеного будівництва"
