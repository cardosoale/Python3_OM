while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+, -, /, *): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os valores digitados não são válidos')
        continue

    # operadores_permitidos = ""
    if operador not in '+/*':
        print('Operador inválido')
        continue
    
    if len(operador) > 1:
        print('Operador inválido')
        continue

    if operador == '+':
        soma = num_1_float + num_2_float
        print(f'A soma dos valores é {soma}')
        
    elif operador == '-':
        sub = num_1_float - num_2_float
        print(f'A subtração dos valores é {sub}')
        
    elif operador == '/':
        div = num_1_float / num_2_float
        print(f'A divisão dos valores é {div}')
        
    elif operador == '*':
        mult = num_1_float * num_2_float
        print(f'A multiplicação dos valores é {mult}') 

    else:
        print('Isso nunca deveria acontecer')

    sair = input('Quer [s]air? ').strip().lower().startswith('s')
    if sair:
        break