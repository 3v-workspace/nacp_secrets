from models.general import *
from models.steps.s00_type_of_declaration import TypeOfDeclarationStep
from models.steps.s01_subject_info import SubjectInfoStep
from models.steps.s02_family_members import FamilyMembersStep
from models.steps.s03_real_estate import RealEstateStep
from models.steps.s04_unfinished_constructions import UnfinishedConstructionsStep
from models.steps.s05_movable_property import ValuableMovablePropertyStep
from models.steps.s06_vehicle import VehiclePropertyStep
from models.steps.s07_securities import SecuritiesStep
from models.steps.s08_corporate_rights import CorporateRightsStep
from models.steps.s09_trusts_legal_entity import TrustsLegalEntityStep
from models.steps.s10_intangible_assets import IntangibleAssetsStep
from models.steps.s11_income_and_gifts import IncomeAndGiftsStep
from models.steps.s12_cash_assets import CashAssetsStep


class IsNotApplicable(BaseModel):
    isNotApplicable: Literal[1]

    class Config:
        extra = Extra.forbid


class CorruptionAffected(Enum):
    """
    Чи належить ваша посада до посад, пов'язаних з високим рівнем
    корупційних ризиків, згідно з переліком, затвердженим Національним
    агентством з питань запобігання корупції?

    1 - Так
    2 - Ні
    0 - ???
    """
    TYPE0 = 0
    YES = 1
    NO = 2


class DeclarationType(Enum):
    """
    0 - Звітний рік в ППСЗ ???
    1 - Щорічна
    2 - Перед звільненням
    3 - Після звільнення
    4 - Кандидата на посаду
    """
    TYPE0 = 0  # Звітний рік в ППСЗ (step_9-v3, step_8-v2)
    ANNUAL = 1  # Щорічна  (step_17-v3, step_16-v2)
    BEFORE_RELEASE = 2  # Перед звільненням (step_17-v3, step_16-v2)
    AFTER_RELEASE = 3  # Після звільнення (step_17-v3, step_16-v2)
    CANDIDATE_FOR_POSITION = 4  # Кандидата на посаду (step_17-v3, step_16-v2)


class Type(Enum):
    """
    1 - декларація
    2 - повідомлення про суттєві зміни в майновому стані
    3 - виправлена декларація
    """
    TYPE1 = 1  # декларація
    TYPE2 = 2  # повідомлення про суттєві зміни в майновому стані
    TYPE3 = 3  # виправлена декларація


class PostType(Enum):
    """
    Інформація для поля  postType з листів:

    Посада державної служби, Посада в органах місцевого
    самоврядування, Посадова особа юридичної особи публічного права,
    [Не застосовується].
    """
    TYPE0 = 0
    TYPE1 = 1
    TYPE2 = 2
    TYPE3 = 3
    TYPE4 = 4


class PostCategory(Enum):
    """
    З листів:

    А,Б,В, перша категорія, друга категорія, третя категорія,
    четверта категорія, п’ята категорія,
    шоста категорія, сьома категорія, [Не застосовується].
    """
    TYPE0 = 0
    TYPE1 = 1
    TYPE2 = 2
    TYPE3 = 3
    TYPE4 = 4
    TYPE5 = 5
    TYPE6 = 6
    TYPE7 = 7
    TYPE8 = 8
    TYPE9 = 9
    TYPE10 = 10


class DataV3(BaseModel):
    step_0: TypeOfDeclarationStep
    step_1: SubjectInfoStep
    step_2: Union[FamilyMembersStep, conlist(dict, max_items=0, min_items=0)]
    step_3: Union[RealEstateStep, IsNotApplicable]
    step_4: Union[UnfinishedConstructionsStep, IsNotApplicable]
    step_5: Union[ValuableMovablePropertyStep, IsNotApplicable]
    step_6: Union[VehiclePropertyStep, IsNotApplicable]
    step_7: Union[SecuritiesStep, IsNotApplicable]
    step_8: Union[CorporateRightsStep, IsNotApplicable]
    step_9: Union[TrustsLegalEntityStep, IsNotApplicable]
    step_10: Union[IntangibleAssetsStep, IsNotApplicable]
    step_11: Union[IncomeAndGiftsStep, IsNotApplicable]
    step_12: Union[CashAssetsStep, IsNotApplicable]
    step_13: dict
    step_14: dict
    step_15: dict
    step_16: dict
    step_17: dict

    # class Config:
    #     extra = Extra.forbid


class DataV2(BaseModel):
    step_0: TypeOfDeclarationStep
    step_1: SubjectInfoStep
    step_2: Union[FamilyMembersStep, conlist(dict, max_items=0, min_items=0)]
    step_3: Union[RealEstateStep, IsNotApplicable]
    step_4: Union[UnfinishedConstructionsStep, IsNotApplicable]
    step_5: Union[ValuableMovablePropertyStep, IsNotApplicable]
    step_6: Union[VehiclePropertyStep, IsNotApplicable]
    step_7: Union[SecuritiesStep, IsNotApplicable]
    step_8: Union[CorporateRightsStep, IsNotApplicable]
    step_9: Union[TrustsLegalEntityStep, IsNotApplicable]
    step_10: Union[IntangibleAssetsStep, IsNotApplicable]
    step_11: Union[IncomeAndGiftsStep, IsNotApplicable]
    step_12: Union[CashAssetsStep, IsNotApplicable]
    step_13: dict
    step_14: dict
    step_15: dict
    step_16: dict

    # class Config:
    #     extra = Extra.forbid


class Declaration(BaseModel):
    id: UUID
    corruption_affected: CorruptionAffected
    data: DataV3
    declaration_type: DeclarationType
    declaration_year: int = Field(ge=2015, le=2021, title='Рік декларації')
    post_category: PostCategory
    post_type: PostType
    responsible_position: int
    schema_version: Literal[3, 2]
    type: Type
    user_declarant_id: int
    date: datetime

    class Config:
        extra = Extra.forbid


class AnnualDeclarationSchemaV2(Declaration):
    # data: DataV3
    declaration_type: Literal[1]
    schema_version: Literal[2]

    class Config:
        extra = Extra.forbid
        title = 'Щорічна декларація V2'


class AnnualDeclarationV3(Declaration):
    data: DataV3
    declaration_type: Literal[1]
    schema_version: Literal[3]

    class Config:
        extra = Extra.forbid
        title = 'Щорічна декларація V3'


class AnnualDeclarationV2(Declaration):
    data: DataV2
    declaration_type: Literal[1]
    schema_version: Literal[2]

    class Config:
        extra = Extra.forbid
        title = 'Щорічна декларація V2'
