from models.general import *


RealEstateType = Literal[
    'Кімната',
    'Земельна ділянка',
    'Квартира',
    'Житловий будинок',
    'Гараж',
    'Садовий (дачний) будинок',
    'Офіс',
    'Інше',
]

OwnershipType = Literal[
    'Спільна власність',
    'Власність',
    'Інше право користування',
    'Спільна сумісна власність',
    'Оренда',
    'Власником є третя особа',
    'Право власності третьої особи, але наявні ознаки відповідно до частини 3 статті 46 ЗУ «Про запобігання корупції»',
    "[Член сім'ї не надав інформацію]",
    '[Не застосовується]',
]


Citizen = Literal[
    'Громадянин України',
    'Юридична особа, зареєстрована в Україні',
    'Іноземний громадянин',
    'Юридична особа, зареєстрована за кордоном',
]

BuildType = Literal[
    'багатоквартирний будинок',
    'житловий будинок',
]


class Right(NACPBaseModel):
    rightBelongs: PersonInfo

    citizen: Optional[Citizen]
    ownershipType: OwnershipType
    otherOwnership: Optional[Union[UsefulStr, Unknown]] = Field(description='Заповнено якщо ownershipType = "Інше"')
    percent_ownership: Optional[Union[BrokenFloat, Unknown]] = Field(alias='percent-ownership')
    rights_id: Optional[constr(regex=r'^[a-f0-9]+$')]
    ua_buildType: Optional[BuildType]
    ua_city: Optional[Union[City, CityType]]
    rights_cityPath: Optional[City]
    ua_sameRegLivingAddress: Optional[YesNoStrNum]
    ua_firstname: Optional[Union[UsefulStr, Unknown]]
    ua_lastname: Optional[Union[UsefulStr, Unknown]]
    ua_middlename: Optional[Union[UsefulStr, Unknown]]

    eng_fullname: Optional[Union[UsefulStr, Unknown]]
    ukr_fullname: Optional[Union[UsefulStr, Unknown]]

    ua_company_code: Optional[Union[CompanyCode, Unknown]]
    ua_company_name: Optional[Union[UsefulStr, Unknown]]

    eng_company_address: Optional[UsefulStr]
    eng_company_code: Optional[Union[CompanyCode, Unknown]]
    eng_company_name: Optional[Union[UsefulStr, Unknown]]
    ukr_company_address: Optional[UsefulStr]
    ukr_company_name: Optional[Union[UsefulStr, Unknown]]

    ua_houseNum: ConfidentialInformation
    ua_postCode: ConfidentialInformation
    ua_street: ConfidentialInformation
    ua_streetType: ConfidentialInformation
    ua_apartmentsNum: ConfidentialInformation
    ua_housePartNum: ConfidentialInformation
    ua_livingAddressFull: ConfidentialInformation
    ua_regAddressFull: ConfidentialInformation
    ua_birthday: ConfidentialInformation
    ua_taxNumber: ConfidentialInformation
    eng_birthday: ConfidentialInformation
    eng_regAddress: ConfidentialInformation
    eng_taxNumber: ConfidentialInformation
    ukr_actualAddress: ConfidentialInformation

    class Config:
        extra = Extra.forbid


class Data(NACPBaseModel):
    rights: Optional[List[Right]]
    iteration: Optional[int]
    country: int
    city: City
    objectType: RealEstateType
    otherObjectType: Optional[UsefulStr] = Field(description='Заповнюється якщо objectType=Інше')
    ua_buildType: Optional[BuildType]

    totalArea: Union[BrokenFloat, Unknown] = Field(title='Загальна площа М2')
    owningDate: Union[DateUK, Unknown] \
        = Field(title='Дата набуття права, DD.MM.YYYY')
    ua_cityType: Optional[CityType]
    cost_date_assessment: Optional[Union[int, Unknown]]

    costAssessment: Optional[Union[int, Unknown]]
    costDate: Optional[Union[int, Unknown]]
    person: Optional[PersonInfo]


    ua_street: ConfidentialInformation
    ua_apartmentsNum: ConfidentialInformation
    ua_houseNum: ConfidentialInformation
    ua_housePartNum: ConfidentialInformation
    region: ConfidentialInformation
    ua_streetType: ConfidentialInformation
    loc_engLivingAddress: ConfidentialInformation
    loc_ukrLivingAddress: ConfidentialInformation
    postCode: ConfidentialInformation
    regNumber: ConfidentialInformation
    cityPath: ConfidentialInformation
    ua_postCode: ConfidentialInformation
    district: ConfidentialInformation
    district: ConfidentialInformation

    class Config:
        extra = Extra.forbid


class RealEstateStep(NACPBaseModel):
    data: List[Data]

    class Config:
        extra = Extra.forbid
        title = "Об'єкти нерухомості"
