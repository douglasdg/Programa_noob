nota1 = float(input(' digite a nota 1:'))
nota2 = float(input(' digite a nota 2:'))
nota3 = float(input(' digite a nota 3:'))
nota4 = float(input(' digite a nota 4:'))

soma = nota1 + nota2 + nota3 + nota4

media = soma // 4

if 20 <= soma:
    print("Parabéns, sua nota é: {}, Aluno aprovado!! ".format(media))
else:

    recupera = float(input( ' digite a nota da recuperação'))

    if recupera > 7:
        print(' Parabéns, deu sorte!!')
    else:

        print(' Te vejo ano que vem kkkkkk')
