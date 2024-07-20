class Vacancies:
    _slots_ = ('name', 'alternative_url', 'salary', 'area_name', 'requirement')

    name: str
    alternative_url: str
    salary: int
    area_name: str
    requirement: str

    def __init__(self, params):
        self.validate_params(params)
        self.name = params.get('name')
        self.__alternative_url = params.get('alternative_url')
        self.validate_salary(params.get('salary'))
        self.area_name = params.get('area_name')
        self.requirement = params.get('requirement')

    def validate_salary(self, salary):
        if salary is None:
            self.salary_from = "Зарплата не указана"
            self.salary_to = None
        else:
            self.salary_from = salary["from"]
            self.salary_to = salary["to"]

    def validate_params(self, params):
        """
        Проверяет что входные данные имеют тип dict
        """
        if not isinstance(params, dict):
            raise Exception('некорректные данные')

    def __str__(self):
        return (f'Название вакансии: {self.name}\n'
                f'Ссылка на вакансию:{self.__alternative_url}\n'
                f'Зарплата: от {self.salary_from} до {self.salary_to}\n'
                f'Место работы: {self.area_name}\n'
                f'Краткое описание вакансии: {self.requirement}'
                )

    def __gt__(self, other):
        if isinstance(other, Vacancies):
            return self.salary_from > other.salary_from
        return False
