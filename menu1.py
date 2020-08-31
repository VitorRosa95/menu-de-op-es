opcao = input('Escolha a opção:\n'
              '1 - Soma de 2 números.\n'
              '2 - Diferença entre 2 números.\n'
              '3 - Produto entre 2 números.\n'
              '4 - Divisão entre 2 números.\n')

if opcao == '1':
    num1 = float(input('Digite o primeiro número\n'))
    num2 = float(input('Digite o segundo número\n'))

    soma = num1 +num2
    print('o resultado da soma foi: ',soma)

if opcao == '2':
    num1 = float(input('Digite o primeiro número\n'))
    num2 = float(input('Digite o segundo número\n'))
    if num2 > num1:
        soma = num2 - num1
        #print('o resultado da soma foi: ', soma)
    soma = num1 - num2
    print('o resultado da soma foi: ', -soma)

if opcao == '3':
    num1 = float(input('Digite o primeiro número\n'))
    num2 = float(input('Digite o segundo número\n'))
    produto = num1 * num2
    print('O produto dos 2 números é de: ',produto)

if opcao == '4':
    num1 = float(input('Digite o numerador\n'))
    num2 = float(input('Digite o denominador\n'))
    if num2 == 0:
        num2 = float(input('denominador igual a 0, digite um número valido.\n'))
    divisao = num1/num2
    print('O resultado da divisão foi: ',divisao)