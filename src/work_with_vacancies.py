from accessify import private


class Vacancies:
    _slots_ = ('name', 'alternate_url', 'salary', 'metro', 'requirement', 'address', 'city')

    name: str
    alternate_url: str
    salary: int
    metro: str
    requirement: str
    address: str
    city: str

    vacancies = []

    def __init__(self, params):
        self.validate_params(params)
        self.name = params.get('name')
        self.__alternate_url = params.get('alternate_url')
        self.validate_salary(params.get('salary'))
        self.city = params.get('area').get('name')
        self.validate_metro(params.get('address'))
        self.requirement = params.get('snippet').get('requirement')
        self.validate_address(params.get('address'))

    @property
    def url(self):
        '''
        возвращает url объекта класса Vacancy
        '''
        return self.__alternate_url

    @private
    def validate_params(self, params):
        '''
        проверяет что входные данные имеют тип dict
        '''
        if not isinstance(params, dict):
            raise Exception('некорректные данные')

    @private
    def validate_metro(self, address):
        if address is None:
            self.metro = 'метро не указано'
        else:
            self.metro = address['metro']['station_name']

    @private
    def validate_address(self, address):
        if address is None:
            self.address = 'Адрес не указан'
        else:
            self.address = address['raw']

    @private
    def validate_salary(self, salary):
        if salary is None:
            self.salary = "Зарплата не указана"

        elif salary['to'] is None:
            self.salary = salary["from"]
        else:
            self.salary = f'{salary["from"]} до {salary["to"]}'

    @classmethod
    def new_vacancy(cls, params):
        '''
        возвращает объект класса Vacancy
        '''
        return cls(params)

    @classmethod
    def add_vacancy(cls, vacancies):
        '''
        добавляет новые вакансии
        '''
        for vacancy in vacancies:
            cls.vacancies.append(cls.new_vacancy(vacancy))

    @classmethod
    def object_list(cls, vacancies):

        cls.vacancies = []
        for vacancy in vacancies:
            cls.vacancies.append(cls.new_vacancy(vacancy))
        return cls.vacancies

    def __str__(self):
        return (f'Название вакансии:\t\t{self.name}\n'
                f'Ссылка на вакансию:\t\t{self.__alternate_url}\n'
                f'Зарплата: \t\tот {self.salary}\n'
                f'Город:\t\t{self.city}\n'
                f'Место работы:\t\t{self.address}\n'
                f'Метро:\t\tстанция {self.metro}\n'
                f'Краткое описание:\t\t{self.requirement}\n\n'
                )

    def __gt__(self, other):
        '''
        Определение поведения для оператора '>'. Сравнивает вакансии по зарплате
        '''
        return self.salary > other.salary
