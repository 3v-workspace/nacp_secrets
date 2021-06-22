from models.general import *
from models.steps.s03_real_estate import Citizen, OwnershipType, BuildType
from models.steps.s04_unfinished_constructions import PersonWhoCare
from models.steps.s08_corporate_rights import LegalForm
from models.steps.s16_membership import Organization


class Data(NACPBaseModel):
    iteration: Optional[Union[PositiveInt, Literal['org', 'part_org']]] = Field(description='Optional for V2')

    person_who_care: Optional[List[PersonWhoCare]]

    person_has_account: Optional[Union[PersonInfo, Unknown]]
    person_has_account_type: Optional[Union[Citizen, Unknown]]
    person_has_account_ua_firstname: Optional[UsefulStr]
    person_has_account_ua_lastname: Optional[UsefulStr]
    person_has_account_ua_middlename: Optional[UsefulStr]
    person_has_account_ua_same_reg_actual_address: Optional[YesNoStrNum]
    person_has_account_ua_company_code: Optional[Union[CompanyCode, Unknown]]
    person_has_account_ua_company_name: Optional[UsefulStr]

    person_open_account: Optional[Union[PersonInfo, Unknown]]
    person_open_account_type: Optional[Union[Citizen, Unknown]]
    person_open_account_ua_firstname: Optional[UsefulStr]
    person_open_account_ua_lastname: Optional[UsefulStr]
    person_open_account_ua_middlename: Optional[UsefulStr]
    person_open_account_ukr_fullname: Optional[UsefulStr]
    person_open_account_eng_fullname: Optional[UsefulStr]
    person_open_account_ua_same_reg_actual_address: Optional[YesNoStrNum]

    person_open_account_ua_company_name: Optional[UsefulStr]
    person_open_account_ua_company_code: Optional[Union[CompanyCode, Unknown]]
    person_open_account_ukr_company_name: Optional[UsefulStr]
    person_open_account_ukr_company_address: Optional[UsefulStr]
    person_open_account_eng_company_address: Optional[UsefulStr]
    person_open_account_eng_company_code: Optional[CompanyCode]
    person_open_account_eng_company_name: Optional[UsefulStr]

    bank_name: Optional[Union[UsefulStr, Unknown]]
    establishment_type: Optional[Union[Citizen, Unknown]]
    establishment_ua_company_code: Optional[Union[CompanyCode, Unknown]]
    establishment_ua_company_name: Optional[Union[UsefulStr, Unknown]]
    establishment_eng_company_name: Optional[Union[UsefulStr, Unknown]]
    establishment_eng_company_code: Optional[Union[CompanyCode, Unknown]]
    establishment_ukr_company_name: Optional[Union[UsefulStr, Unknown]]

    account_number: ConfidentialInformation
    account_type: ConfidentialInformation
    other_account_type: ConfidentialInformation
    person_has_account_ua_birthday: ConfidentialInformation
    person_has_account_ua_reg_address: ConfidentialInformation
    person_has_account_ua_taxNumber: ConfidentialInformation
    person_open_account_ua_birthday: ConfidentialInformation
    person_open_account_ua_reg_address: ConfidentialInformation
    person_open_account_ua_taxNumber: ConfidentialInformation
    person_open_account_ua_actual_address: ConfidentialInformation
    person_has_account_ua_actual_address: ConfidentialInformation
    person_open_account_eng_birthday: ConfidentialInformation
    person_open_account_eng_reg_address: ConfidentialInformation
    person_open_account_eng_taxNumber: ConfidentialInformation
    person_open_account_ukr_reg_address: ConfidentialInformation

    class Config:
        extra = Extra.forbid


class BanksStep(NACPBaseModel):
    data: List[Union[Data, Dict[PositiveInt, Organization]]]

    class Config:
        extra = Extra.forbid
        title = "Грошові активи"
