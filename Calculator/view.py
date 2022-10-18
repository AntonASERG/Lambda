import logger
import model

# метод - выдать ошибка ввода
def error_value():
    logger.logger('Ошибка ввода данных')
    return print('Ошибка ввода данных')


# метод - выдать результа
def print_total():
    return print(f'{model.strA}  = {model.total}')