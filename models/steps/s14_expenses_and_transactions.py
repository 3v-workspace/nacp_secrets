from models.general import *
from models.steps.s03_real_estate import Citizen, OwnershipType, BuildType
from models.steps.s04_unfinished_constructions import PersonWhoCare
from models.steps.s08_corporate_rights import LegalForm


SpecExpenses = Literal[
    'Право власності (у тому числі спільної власності), володіння чи користування суб’єкта декларування припинено',
    'Суб’єкт декларування набув право власності (у тому числі спільної власності), володіння чи користування',
    'Виникло фінансове зобов’язання суб’єкта декларування',
    'Оплата послуг',
    'Придбання',
    'Страхові виплати',
    'Оренда',
    'Інше',
]


SpecExpensesSubject = Literal[
    'Нематеріальні активи',
    'Нерухоме майно',
    'Рухоме майно',
    'Нематеріальні активи (зазначте, які саме)',
    'Інше нерухоме майно (зазначте, яке саме)',
    'Інше рухоме майно (зазначте, яке саме)',
    'Інше рухоме майно',
    'Інший (зазначте, який саме)',
    'Інше',
]


SpecResultExpenses = Literal[
    'Суб’єкт декларування набув право власності (у тому числі спільної власності), володіння чи користування',
    'Право власності (у тому числі спільної власності), володіння чи користування суб’єкта декларування припинено',
    'Виникло фінансове зобов’язання суб’єкта декларування',
    'Інше',
]

Types = Literal[
    1,
    2,
]


class Data(NACPBaseModel):
    iteration: Optional[PositiveInt] = Field(description='Для V2 може бути пустим')
    type: Optional[Types] = Field(description='Для V2 може бути пустим')
    costAmount: Optional[PositiveInt]
    country: Optional[PositiveInt]
    date_costAmount: Optional[DateUK]
    specExpenses: Optional[SpecExpenses]
    specOtherExpenses: Optional[UsefulStr]
    specExpensesSubject: SpecExpensesSubject
    specOtherExpensesSubject: Optional[UsefulStr] = Field(description='Examples: "отримання дивідендів"')
    specExpensesRealtySubject: Optional[UsefulStr] = Field(
        description="Examples: 'квартира', 'Квартира', 'Земельна ділянка та будинок',"
                    "'Житловий будинок', 'Земельна ділянка', 'Інше нерухоме майно', 'Садовий (дачний) будинок'"
    )
    specExpensesOtherRealtySubject: Optional[UsefulStr] = Field(description='Examples: "база відпочинку"')
    date_specExpenses: Optional[DateUK]
    specResultExpenses: Optional[SpecResultExpenses]
    specExpensesMovableSubject: Optional[UsefulStr] = Field(
        description='Examples: "автомобіль Форд Фієста", "Транспортний засіб", "Одяг", "Автомобіль", '
                    '"Грошові кошти", "Легковий автомобіль "'
    )
    specExpensesOtherMovableSubject: Optional[UsefulStr]
    specExpensesAssetsSubject: Optional[UsefulStr] = Field(description='Examples: "Акції", "прості акції"')

    class Config:
        extra = Extra.forbid


class ExpensesAndTransactionsStep(NACPBaseModel):
    data: List[Data]

    class Config:
        extra = Extra.forbid
        title = "Видатки та правочини суб'єкта декларування"
