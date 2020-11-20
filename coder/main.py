


def coding(symbol, operation_type, indent=3):
    if operation_type == 'c':
        symbol_number = ord(symbol) + indent  # 'A' -> 65 + 3
    elif operation_type == 'e':
        symbol_number = ord(symbol) - indent  # 'D' -> 68 - 3
    new_symbol = chr(symbol_number)  # 68 -> 'D'
    return new_symbol

def translator(operation, text):
    translation = ''
    for symbol in text:
        if operation == 'code':
            translation += coding(symbol, 'c')
        elif operation == 'encode':
            translation += coding(symbol, 'e')
    
    return translation

while True:
    print(translator(input('Что делаем? code/encode\n'), input('Введи текст\n')))






