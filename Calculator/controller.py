import logger
import model
import view


# метод - сверка на соответвсие типа введеных данных - операцию
def input_buf():
    bufStr = ''
    for i in range (len(model.buf)):
        bufStr += str(model.buf[i])
    if bufStr.isdigit():
        return model.buf
    else:
        view.error_value()
   
   
   
# # метод операция 3.10й питон!!
def operation_total():
    model.total = eval(model.strA)
    logger.logger(f'{model.strA}  = {model.total}')