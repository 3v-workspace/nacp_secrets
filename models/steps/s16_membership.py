from models.general import *
from models.steps.s03_real_estate import Citizen, OwnershipType, BuildType
from models.steps.s04_unfinished_constructions import PersonWhoCare
from models.steps.s08_corporate_rights import LegalForm


OrganizationType = Literal[
    'Громадське об’єднання',
    'Благодійна організація',
    'Саморегулівне чи самоврядне професійне об’єднання',
]

UnitType = Literal[
    'Наглядові органи',
    'Керівні органи',
    'Ревізійні органи',
]


class Organization(NACPBaseModel):
    iteration: Optional[int] = Field(description='Для V2 може бути пустим')
    objectName: UsefulStr
    objectType: OrganizationType
    reestrCode: Union[CompanyCode, Unknown]

    unitType: Optional[UnitType]
    unitName: Optional[UsefulStr]

    class Config:
        extra = Extra.forbid


class Data(NACPBaseModel):
    org: Optional[List[Organization]]
    part_org: Optional[List[Organization]]

    class Config:
        extra = Extra.forbid


class MembershipStep(NACPBaseModel):
    data: Data

    class Config:
        extra = Extra.forbid
        title = "Членство суб’єкта декларування в організаціях та їх органах"
