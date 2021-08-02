import json
from datetime import datetime


class Wiki:

    url = 'https://en.wikipedia.org/wiki/'

    def __init__(self, path, path_link=None):
        self.path = path
        self.path_link = path_link

    def __iter__(self):
        with open(self.path, encoding='utf-8') as file:
            self.countries = json.load(file)
        return self

    def __next__(self):
        if not self.countries:
            raise StopIteration

        country = self.countries.pop()['name']['common']

        if self.path_link is not None:
            with open(self.path_link, "a", encoding="utf-8") as file:
                file.write(country+' - ' + self.get_link(country) + '\n')

        return country

    def save_log_with_param(file_name):
        def save_log(func):
            def new_function(*args, **kwargs):
                a = func(*args, **kwargs)
                with open(file_name, 'a', encoding='utf-8') as file:
                    file.write(f'Function: {func.__name__}\n')
                    file.write(f'Date and time: {datetime.now()}\n')
                    file.write(f'Arguments: {args}, {kwargs}\n')
                    file.write(f'Return value: {a}\n')
                    file.write(f'-' * 30)
                return a

            return new_function

        return save_log

    @save_log_with_param('log/HW with logger.txt')
    def get_link(self, country):
        return self.url + country.replace(' ', '_')


if __name__ == '__main__':
    for el in Wiki('countries.json', 'countries_links.txt'):
        print(el)