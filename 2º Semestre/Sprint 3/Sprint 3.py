from operator import ge
import random

#Funções
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

#Listas
contasRecrutadores = []
senhasRecrutadores = []
contasCandidatos = []
senhasCandidatos = []
vagas = []
vaga = ()

#Variaveis
tipoConta = ""
opcaoInicial = 0
usuario = ""
senha = ""

#Sistema
print("---! Bem-vindo(a) !---\n")
while opcaoInicial != 3:
    opcaoCandidato = 0    
    opcaoRecrutador = 0
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
        
        if usuario in contasRecrutadores or usuario in contasCandidatos:
            print("Nome de usuário em uso.")
            read()
        elif recrutadorCandidato == "R":
            contasRecrutadores.append(usuario)
            senhasRecrutadores.append(senha)
            print("Usuário cadastrado com sucesso.")
            read()
        else:
            contasCandidatos.append(usuario)
            senhasCandidatos.append(senha)
            print("Usuário cadastrado com sucesso.")
            read()    
    elif opcaoInicial == 2:
        usuario = input("Digite seu usuário: ")
        senha = input("Digite sua senha: ")
        try:
            contasRecrutadores.index(usuario)
            senhasRecrutadores.index(senha)
            tipoConta = "R"       
        except:
            try:
                contasCandidatos.index(usuario)
                senhasCandidatos.index(senha)
                tipoConta = "C"
            except:
                print("Usuário ou senha inválidos.")
                read()           
        if tipoConta == "R":
            print("\n---! Bem-Vindo(a) ao Menu Recrutador(a) !---")
            read()
            while opcaoRecrutador != 3:
                print("- FUNCIONALIDADES DO RECRUTADOR - \n"+
                "(1) ALTERAR SENHA.\n" +
                "(2) CRIAR VAGA.\n" +
                "(3) SAIR.\n")
                opcaoRecrutador = int(input("Escolha sua funcionalidade: "))
                if opcaoRecrutador == 1:
                    senha = input("\nDigite sua nova senha: ")
                    senhasRecrutadores[contasRecrutadores.index(usuario)] = senha
                    print("Senha atualizada com sucesso!")
                    read()
                elif opcaoRecrutador == 2:    
                    tp_cont = input("Digite o tipo do contrato: ")
                    nv_cargo = input("Digite o nível do cargo: ")
                    ar_vaga = input("Digite a área da vaga: ")
                    vagarec = criarVaga(tp_cont, nv_cargo, ar_vaga)
                    vagas.append(vagarec)
                    print(vagarec)
                    print("Vaga adicionada com sucesso!")
                    read()
        elif tipoConta == "C":
            print("\n---! Bem-Vindo(a) ao Menu Candidato(a) !---")
            read()
            while opcaoCandidato != 4:
                print("- FUNCIONALIDADES DO CANDIDATO - \n"+
                "(1) ALTERAR SENHA.\n" +
                "(2) PESQUISAR VAGAS.\n" +
                "(3) (Exibir vagas criadas no menu recrutador).\n" +
                "(4) SAIR.\n")
                opcaoCandidato = int(input("Escolha sua funcionalidade: "))
                if opcaoCandidato == 1:
                    senha = input("\nDigite sua nova senha: ")
                    senhasCandidatos[contasCandidatos.index(usuario)] = senha
                    print("Senha atualizada com sucesso!")
                    read()
                elif opcaoCandidato == 2:    
                    resp = geradorVagas()
                    print(resp)
                    read()
                elif opcaoCandidato == 3:    
                    print(vagas)
                    read()                     