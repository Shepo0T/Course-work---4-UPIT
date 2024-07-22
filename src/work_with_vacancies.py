from accessify import private


class Vacancies:
    """
    Класс обрабатывающий входные данные по вакансиям из API hh
    """
    _slots_ = ('name', 'alternate_url', 'salary', 'metro', 'requirement', 'address', 'city')

    name: str  # Название вакансии
    alternate_url: str  # Ссылка на вакансию
    salary: int  # Зарплата
    metro: str  # Название станции метро
    requirement: str  # Краткое описание вакансии
    address: str  # Адрес места работы
    city: str  # Название города, где находится место работы

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
        """
        Возвращает url объекта класса Vacancy
        """
        return self.__alternate_url

    @private
    def validate_params(self, params):
        """
        Проверяет что входные данные имеют тип dict
        """
        if not isinstance(params, dict):
            raise Exception('некорректные данные')

    @private
    def validate_metro(self, address):
        """
        Проверяет входные данные по наличию станции метро
        """
        if address == 'null':
            self.metro = 'метро не указано'
        elif address is None:
            self.metro = 'метро не указано'
        elif address.get("metro") is None:
            self.metro = 'метро не указано'

        else:
            self.metro = address.get('metro').get('station_name')

    @private
    def validate_address(self, address):
        """
        Проверяет входные данные по адресам
        """
        if address is None:
            self.address = 'Адрес не указан'
        else:
            self.address = address['raw']

    @private
    def validate_salary(self, salary):
        """
        Проверяет входные данные по зарплате
        """
        if salary is None:
            self.salary = "Зарплата не указана"

        elif salary['to'] is None:
            self.salary = salary["from"]
        else:
            self.salary = f'{salary["from"]} до {salary["to"]}'

    @classmethod
    def new_vacancy(cls, params):
        """
        Возвращает объект класса Vacancy
        """
        return cls(params)

    @classmethod
    def add_vacancy(cls, vacancies):
        """
        Добавляет новые вакансии
        """
        for vacancy in vacancies:
            cls.vacancies.append(cls.new_vacancy(vacancy))

    @classmethod
    def object_list(cls, vacancies):
        """
        Возвращает список инициализированных объектов класса Vacancies
        """
        cls.vacancies = []
        for vacancy in vacancies:
            cls.vacancies.append(cls.new_vacancy(vacancy))
        return cls.vacancies

    def __str__(self):
        """
        Строковое представление объекта
        """
        return (f'Название вакансии:\t\t{self.name}\n'
                f'Ссылка на вакансию:\t\t{self.__alternate_url}\n'
                f'Зарплата: \t\tот {self.salary}\n'
                f'Город:\t\t{self.city}\n'
                f'Место работы:\t\t{self.address}\n'
                f'Метро:\t\tстанция {self.metro}\n'
                f'Краткое описание:\t\t{self.requirement}\n\n'
                )

    def __gt__(self, other):
        """
        Определение поведения для оператора '>'. Сравнивает вакансии по зарплате
        """
        return self.salary > other.salary
