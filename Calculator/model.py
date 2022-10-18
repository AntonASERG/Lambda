import controller
import view
import re


total = 0
buf = []
strA = ''


def string_init ():
    global strA
    global buf
    strA = input ('введите выражение:  ')
    for i in strA:
        if i == ' ':
            strA = strA.replace (' ', '')
    buf = re.split('\*|\-|\+|\/',strA)
    buf = controller.input_buf()
 

def total_init ():
    
    total = controller.operation_total()
    return total
