#   метод - выдать ошибка ввода
from pyexpat import model


def error_value():
    return print ('ошибка ввода') 

def print_total():
    return print (f'Результат: {model.total}')