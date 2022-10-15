import view

# методs - сверка на соответвсие типа введеных данных
def input_integer(enter, error):
    while True:# ВАЖНО цикл крутит пока е введем число
        try:
            a = int (input(enter))
            return a
        except: 
            view.error_value()

def input_operation(enter, error):
    while True:# ВАЖНО цикл крутит пока е введем символ
        try:
            a = input(enter)
            if a in ['+','-','*','/']:
                return a
        except: 
            view.error_value()