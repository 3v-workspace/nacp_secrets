from models.general import *
from models.steps.s04_unfinished_constructions import PersonWhoCare
from models.steps.s08_corporate_rights import LegalForm


class BaseData(NACPBaseModel):
    person: Optional[PersonInfo]
    legalForm: Union[LegalForm, UsefulStr, Unknown]  # ????
    address_beneficial_owner: Optional[Union[UsefulStr, Unknown]] = \
        Field(description='Example: 57401, Миколаївська область, смт. Березанка, вулиця Степова, буд.18')

    company_name_beneficial_owner: Optional[UsefulStr] = Field(description='Example: МПП "СКБ Салют"')
    fax: Union[constr(regex=r'^\+?\d{6,13}$'), Unknown]
    mail: Union[EmailStr, UsefulStr, Unknown] = \
        Field(description='Може містити невалідні адреси, наприклад: "V ictor@ukr.net"')
    person_who_care: Optional[List[PersonWhoCare]]
    phone: Union[constr(regex=r'^\+?\d{6,13}$'), Unknown]
    ua_company_code_beneficial_owner: Optional[Union[CompanyCode, Unknown]]
    company_code_beneficial_owner: Optional[CompanyCode]
    en_company_address_beneficial_owner: Optional[UsefulStr]
    en_company_name_beneficial_owner: Optional[UsefulStr]
    ua_company_address_beneficial_owner: Optional[UsefulStr]
    ua_company_name_beneficial_owner: Optional[UsefulStr]

    regNumber: ConfidentialInformation

    class Config:
        extra = Extra.forbid


class DataV3(BaseData):
    iteration: PositiveInt
    country_beneficial_owner: PositiveInt


class DataV2(BaseData):
    iteration: Optional[PositiveInt]
    address: Union[UsefulStr, Unknown]
    beneficial_owner_company_code: Optional[Union[CompanyCode, Unknown]]
    country: Union[PositiveInt, Unknown]
    name: Union[UsefulStr, Unknown]
    en_name: Optional[Union[UsefulStr, Unknown]]


class TrustsLegalEntityStep(NACPBaseModel):
    data: List[Union[DataV2, DataV3]]

    class Config:
        extra = Extra.forbid
        title = "Юридичні особи, трасти або інші подібні правові утворення, " \
                "кінцевим бенефіціарним власником (контролером) яких є суб’єкт " \
                "декларування або члени його сім'ї"
