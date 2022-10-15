import controller


first = 0
second = 0
ops = ''
total = 0


# метод вводит и хранит
def init ():
    global first
    global second
    first = controller.input_integer("Введите первое число: ", "Ошибка")
    second = controller.input_integer("Введите второе число: ", "Ошибка")

def start(): 
    a = int(input('Введите первое число:  '))
    b = int(input('Введите второе число:  '))

# метод операция 3.10й питон!!
def operation ():
    global first
    global second
    global ops
    global total # return ne nado
    ops = controller.input_operation(('Введите операцию:  '))
    match (ops):
        case '+':
            total = first + second
        case '-':
            total = first - second
        case '*':
            total = first * second
        case '/':
            total = first / second
        case _: # в иных случаях 
            view.error_value()


        


