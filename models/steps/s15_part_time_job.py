from models.general import *
from models.steps.s03_real_estate import Citizen, OwnershipType, BuildType
from models.steps.s04_unfinished_constructions import PersonWhoCare
from models.steps.s08_corporate_rights import LegalForm


Paid = Literal[
    'Оплачувана',
    'Не оплачувана',
]


class Data(NACPBaseModel):
    iteration: Optional[PositiveInt] = Field(description='Для V2 може бути пустим')
    paid: Paid
    description: UsefulStr = Field(
        description='Examples: `Молодший науковий співробітник`, `Художній керівник`, `Укладчик-пакувальник`,'
                    '`Електрик`, `Ведучий спеціаліст`, `Голова правління`, `військова служба`, '
                    '`Старший оператор ЕО та ОМ`'
    )

    margin_emitent: Union[PersonInfo] = Field(alias='margin-emitent')
    emitent_citizen: Optional[Citizen]
    emitent_ua_company_code: Optional[Union[CompanyCode, Unknown]]
    emitent_ua_company_name: Optional[Union[UsefulStr, Unknown]]
    emitent_eng_company_code: Optional[Union[CompanyCode, Unknown]]
    emitent_eng_company_name: Optional[UsefulStr]
    emitent_ukr_company_name: Optional[UsefulStr]
    emitent_ukr_company_address: Optional[Union[UsefulStr, Unknown]]
    emitent_eng_company_address: Optional[Union[UsefulStr, Unknown]]

    emitent_ua_firstname: Optional[UsefulStr]
    emitent_ua_lastname: Optional[UsefulStr]
    emitent_ua_middlename: Optional[UsefulStr]
    emitent_eng_fullname: Optional[Union[UsefulStr, Unknown]]
    emitent_ukr_fullname: Optional[Union[UsefulStr, Unknown]]
    emitent_ua_sameRegLivingAddress: Optional[YesNoStrNum]

    emitent_ua_actualAddress: ConfidentialInformation
    emitent_ua_birthday: ConfidentialInformation
    emitent_ua_regAddress: ConfidentialInformation
    emitent_ua_taxNumber: ConfidentialInformation
    emitent_eng_birthday: ConfidentialInformation
    emitent_eng_regAddress: ConfidentialInformation
    emitent_eng_taxNumber: ConfidentialInformation
    emitent_ukr_regAddress: ConfidentialInformation


    class Config:
        extra = Extra.forbid


class PartTimeJobStep(NACPBaseModel):
    data: List[Data]

    class Config:
        extra = Extra.forbid
        title = "Робота за сумісництвом суб’єкта декларування"
