import psycopg2

from src.DBCreate_module import DBConnection


class DBManager(DBConnection):
    """Класс для взаимодействия с базой данных"""

    def __init__(self):
        super().__init__()

    def connect_to_db(self, query, params=None):
        conn = psycopg2.connect(
            host=self._host,
            database=self._database,
            user=self._username,
            port=self._port,
            password=self._password,
        )
        cur = conn.cursor()
        conn.autocommit = True
        cur.execute(query, params)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result

    def get_companies_and_vacancies_count(self):
        """Метод для получения из базы данных названия компании и количества вакансий этой компании"""
        execute_message = """SELECT employers.company_name, COUNT(vacancies.employer_id)
        FROM employers JOIN vacancies USING (employer_id) GROUP BY employer_id"""
        return self.connect_to_db(execute_message)

    def get_all_vacancies(self):
        """Метод для получения информации по вакансии и названию компании"""
        execute_message = """SELECT employers.company_name, vacancies.vacancy_name, 
        ((vacancies.salary_from + vacancies.salary_to) / 2), vacancies.url
        FROM vacancies JOIN employers USING(employer_id)"""
        return self.connect_to_db(execute_message)

    def get_avg_salary(self):
        """Метод для получения средней зарплаты по вакансиям"""
        execute_message = """SELECT AVG((vacancies.salary_from + vacancies.salary_to) / 2) FROM vacancies"""
        return self.connect_to_db(execute_message)

    def get_vacancies_with_higher_salary(self):
        """Метод для получения вакансий с зарплатой выше среднего"""
        execute_message = """SELECT * FROM vacancies WHERE ((vacancies.salary_from + vacancies.salary_to) / 2) > 
(SELECT (AVG((vacancies.salary_from + vacancies.salary_to) / 2)) FROM vacancies)"""
        return self.connect_to_db(execute_message)

    def get_vacancies_with_keyword(self, keyword: str):
        """Метод для получения вакансий по ключевому слову"""
        execute_message = f"""SELECT * FROM vacancies WHERE vacancy_name ILIKE '%{keyword}%'"""
        return self.connect_to_db(execute_message)
