while True:
    print('--------AGDM CURSOS-------- \n1 - Matrícula \n2 - Atualizar matrícula \n3 - Avaliação \n4 - Apagar dados cadastrais \n5 - Encerrar programa \n---------------------------')
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        print('------Matrícula------ \n1 - Cadastro \n2 - Cursos \n3 - Pagamento \n---------------------')
        opcao1 = int(input('Escolha uma opção: '))
        if opcao1 == 1:
            import insertmatricula
            print('Cadastro realizado.')
        elif opcao1 == 2:
            import insertcursos
            print('Curso selecionado.')
        elif opcao1 == 3:
            import insertpagamento
            print('Pagamento realizado.')
        else:
            print('Insira uma opção de 1 a 3.')
    elif opcao == 2:
        print('------Atualizar dados------ \n1 - E-mail \n2 - Telefone \n3 - Nome \n4 - Turno \n---------------------------')
        opcao2 = int(input('Escolha uma opção: '))
        if opcao2 == 1:
            import updateemail
            print('E-mail atualizado.')
        elif opcao2 == 2:
            import updatetelefone
            print('Telefone atualizado.')
        elif opcao2 == 3:
            import updatenome
            print('Nome atualizado.')
        elif opcao2 == 4:
            import updateturno
            print('Turno atualizado.')
        else:
            print('Insira uma opção de 1 a 4.')
    elif opcao == 3:
        import insertavaliacao
        print('Aluno avaliado.')
    elif opcao == 4:
        import deletematriculas
        print('Apagar cadastro.')
    elif opcao == 5:
        print('Sessão finalizada!')
        break
    else:
        print('Insira uma opção de 1 a 5.')


    