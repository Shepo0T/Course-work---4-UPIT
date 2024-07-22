
def get_vacancies_by_salary(vacancies, salary):
    """
    Функция для сортировки заработной платы
    """
    result = []
    for vacancy in vacancies:

        if vacancy['salary']['from'] is None:
            break
        elif vacancy['salary']['from'] > salary:
            result.append(vacancy)

    return result

def print_vacancies(vacancies):
    """
    Выводит топ вакансии на экран
    """
    for vacancy in vacancies:
        print(f"\n{vacancy}")
def user_interface():
    """
    Интерфейс для ввода параметров пользователем
    """

    keyword = input("Какую профессию вы ищите?\n").lower()
    range_salary = int(input("Введите минимальную желаемую зарплату: например \033[32m100000\033[0m\n"))
    top_n = int(input("Сколько профессий вывести?\n"))

    return keyword, range_salary, top_n