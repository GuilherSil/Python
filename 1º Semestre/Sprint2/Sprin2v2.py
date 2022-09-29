from operator import ge
import random


def read():
    return input("\nPressione 'ENTER' para continuar!")

def geradorVagas():
    rand_numero_vaga = str(random.randint(10000,99999))
    nivel_cargo = ["Júnior", "Pleno", "Sênior"]
    rand_cargo = random.choice(nivel_cargo)
    tipo_contrato = ["CLT", "Trainee", "Estágio", "PJ"]
    rand_contrato = random.choice(tipo_contrato)
    funcao_trabalho = ["Desenvolvimento de Software e TI", "Dados e Analytics", "Cientista de Dados"]
    rand_func_trabalho = random.choice(funcao_trabalho)
    vaga = ""
    vaga += "Vaga #" + rand_numero_vaga + " - " + rand_contrato + " - " + rand_cargo + " em " + rand_func_trabalho
    return vaga

def criarVaga(tipo_contrato, nivel_cargo, area_vaga):
    nm_vaga = str(random.randint(10000,99999))
    vaga = ""
    vaga += "Vaga #" + nm_vaga + " - " + tipo_contrato + " - " + nivel_cargo + " em " + area_vaga
    return vaga

    
opcaoRecrutador = 0
opcaoInicial = 0
usuario = ""
senha = ""
confUsuario = ""
confSenha = ""


print("---! Bem-vindo(a) !---\n")
while opcaoInicial != 3:
    opcaoCandidato = 0
    opcaoRecrutador = 0
    login = ""
    print("- FUNCIONALIDADES DO SISTEMA - \n"+
        "(1) CADASTRO.\n" +
        "(2) LOGIN.\n" +
        "(3) SAIR.")
    opcaoInicial = int(input("Escolha sua funcionalidade: "))
    if opcaoInicial == 1:
        recrutadorCandidato = input("\nVocê é Recrutador(R) ou Candidato(C)?\n" +
        "(R/C): ")
        while recrutadorCandidato != "R" and recrutadorCandidato != "C":
            recrutadorCandidato = input("Por favor, escolha entre Recrutador(R) ou Candidato(C).\n" +
            "(R/C): ")
        usuario = input("Digite seu usuário: ")
        senha = input("Digite sua senha: ")
        if usuario == confUsuario:
            print("Já existe uma conta com este usuário.")    
            read()
        elif usuario != confUsuario:
            confUsuario = usuario
            confSenha = senha
            print("Cadastro efetuado com sucesso! Você já pode acessar sua conta!")    
            read()  
    elif opcaoInicial == 2:
        usuario = input("Digite seu usuário: ")
        senha = input("Digite sua senha: ")
        if usuario == confUsuario and senha == confSenha:
            login = "ok"
            print("Login efetuado com sucesso!")
            read()
        else:
            print("Credenciais não reconhecidas ou incorretas.")    
            read()
    if login == "ok" and recrutadorCandidato == "C":
        print("\n---! Bem-Vindo(a) ao Menu Candidato(a) !---")
        read()
        while opcaoCandidato != 3:
            print("- FUNCIONALIDADES DO CANDIDATO - \n"+
            "(1) ALTERAR SENHA.\n" +
            "(2) PESQUISAR VAGAS.\n" +
            "(3) SAIR.\n")
            opcaoCandidato = int(input("Escolha sua funcionalidade: "))
            if opcaoCandidato == 1:
                confSenha = input("\nDigite sua nova senha: ")
                print("Senha atualizada com sucesso!")
                read()
            elif opcaoCandidato == 2:    
                resp = geradorVagas()
                print(resp)
                read()
    elif login == "ok" and recrutadorCandidato == "R":
        print("\n---! Bem-Vindo(a) ao Menu Recrutador(a) !---")
        read()       
        while opcaoRecrutador != 3:
            print("- FUNCIONALIDADES DO RECRUTADOR - \n"+
            "(1) ALTERAR SENHA.\n" +
            "(2) CRIAR VAGA.\n" +
            "(3) SAIR.\n")
            opcaoRecrutador = int(input("Escolha sua funcionalidade: "))
            if opcaoRecrutador == 1:
                confSenha = input("\nDigite sua nova senha: ")
                print("Senha atualizada com sucesso!")
                read()
            elif opcaoRecrutador == 2:    
                tp_cont = input("Digite o tipo do contrato: ")
                nv_cargo = input("Digite o nível do cargo: ")
                ar_vaga = input("Digite a área da vaga: ")
                vagarec = criarVaga(tp_cont, nv_cargo, ar_vaga)
                print(vagarec)
                print("Vaga adicionada com sucesso!")
                read()       