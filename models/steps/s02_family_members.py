from models.general import *

PEP_RELATIONSHIPS_TYPES_TO_EN = {
    "ділові зв'язки": 'business relationship',
    "особисті зв'язки": 'personal connections',
    'особи, які спільно проживають': 'persons who live together',
    "пов'язані спільним побутом і мають взаємні права та обов'язки": 'are connected by common constructions and have common rights and responsibilities',
    'усиновлювач': 'adopter',
    'падчерка': 'stepdaughter',
    'дід': 'grandfather',
    'рідний брат': 'brother',
    'мати': 'mother',
    'син': 'son',
    'невістка': 'daughter-in-law',
    'внук': 'grandson',
    'мачуха': 'stepmother',
    'особа, яка перебуває під опікою або піклуванням': 'a person under guardianship or custody',
    'усиновлений': 'adopted',
    'внучка': 'granddaughter',
    'батько': 'father',
    'рідна сестра': 'sister',
    'зять': 'son-in-law',
    'чоловік': 'husband',
    'опікун чи піклувальник': 'guardian or trustee',
    'дочка': 'daughter',
    'свекор': 'father-in-law',
    'тесть': 'father-in-law',
    'теща': 'mother-in-law',
    'баба': 'grandmother',
    'пасинок': 'stepson',
    'вітчим': 'stepfather',
    'дружина': 'wife',
    'свекруха': 'mother-in-laws',
}

SubjectRelation = Literal[
    'дружина',
    'син',
    'дочка',
    'чоловік',
    'онук',
    'мати',
    'свекруха',
    'свекор',
    'батько',
    'теща',
    'рідний брат',
    'баба',
    'падчерка',
    'пасинок',
    'рідна сестра',
    'особа, яка перебуває під піклуванням згаданого суб’єкта',
    'онучка',
    'вітчим',
    'зять',
    'невістка',
    'тесть',
    'усиновлений',
    'правнучка',
    'дід',
    'особа, яка перебуває під опікою',
    'опікун',
    'прабаба',
    'піклувальник',
    'мачуха',
    'особи, які спільно проживають, але не перебувають у шлюбі',
    "інший зв'язок",
]


class Data(NACPBaseModel):
    id: int

    firstname: Optional[UsefulStr]
    lastname: Optional[UsefulStr]
    middlename: Optional[Union[UsefulStr, Unknown]]
    country: Optional[Union[int, Unknown]]

    eng_full_name: Optional[UsefulStr]  # V2
    ukr_full_name: Optional[UsefulStr]  # V2

    no_taxNumber: Optional[YesNoStrNum]
    eng_firstname: Optional[UsefulStr]
    eng_lastname: Optional[UsefulStr]
    eng_middlename: Optional[Union[UsefulStr, Unknown]]

    previous_firstname: Optional[UsefulStr]
    previous_lastname: Optional[UsefulStr]
    previous_middlename: Optional[Union[UsefulStr, Unknown]]
    cityType: Optional[CityType]
    usage: Optional[List[Union[int, float]]]
    changedName: YesNoStrNum
    citizenship: Union[int, Unknown]
    city: City

    identificationCode: ConfidentialInformation
    passportCode: ConfidentialInformation
    taxNumber: ConfidentialInformation
    passport: ConfidentialInformation
    eng_identification_code: ConfidentialInformation
    birthday: ConfidentialInformation
    district: ConfidentialInformation
    cityPath: ConfidentialInformation
    postCode: ConfidentialInformation
    apartmentsNum: ConfidentialInformation
    region: ConfidentialInformation
    street: ConfidentialInformation
    streetType: ConfidentialInformation
    housePartNum: ConfidentialInformation = Field(title='Номер корпусу')
    houseNum: ConfidentialInformation
    unzr: ConfidentialInformation = Field(title='Унікальний номер запису в Єдиному державному демографічному реєстрі')
    eng_full_address: ConfidentialInformation
    ukr_full_address: ConfidentialInformation

    subjectRelation: SubjectRelation

    class Config:
        extra = Extra.forbid


class FamilyMembersStep(NACPBaseModel):
    data: List[Data]

    class Config:
        extra = Extra.forbid
        title = "Інформація про членів сім'ї суб'єкта декларування"
