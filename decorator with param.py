from datetime import datetime
import requests
from bs4 import BeautifulSoup

def save_log_with_param(file_name):
    def save_log(func):
        def new_function(*args, **kwargs):
            a = func(*args, **kwargs)
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(f'Function: {func.__name__}\n')
                file.write(f'Date and time: {datetime.now()}\n')
                file.write(f'Arguments: {args}, {kwargs}\n')
                file.write(f'Return value: {a}\n')
            return a
        return new_function
    return save_log
# @save_log
@save_log_with_param('log/log.txt')
def dollar_rate(url):
    response = requests.get(url)
    if not response.ok:
        raise Exception('response not ok')
    soup = BeautifulSoup(response.text, features='html.parser')
    rate = soup.find('span', class_="inline-stocks__value_inner").text
    return rate
dollar_rate('https://yandex.ru/')