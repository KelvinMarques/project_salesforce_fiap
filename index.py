#Menu

#Chat de voz
##
#cadastro
##pedir 5 info e retornar que o cadastro foi feito e salvar em uma lista de usuarios
#Login 
##Pedir duas info, verificar na lista de usuario e retornar com login sucesso ou não existe
from typing import get_type_hints

var: str
def getMenu():
    print("====MENU SALESFORCE=====")
    print("1. Cadastro")
    print("2. Login")
    print("3. Chat de voz")
    print("4. Sair")
    print("5. V A S C O")

def Cadastro(listaDeUsuarios):

    nome = input("Digite seu nome:")
    idade = input("Digite seu idade:")
    email = input("Digite seu email:")
    senha = input("Digite seu senha:")
    sexo = input("Digite seu sexo:")

    #Criar dicionario e incluir os dados na lista utilizando o email como . 
    
    usuarios = {
            "nome": nome,
            "idade": idade,
            "email": email,
            "senha": senha,
            "sexo": sexo,
    }
    dictUsuarios = {
    email: usuarios
}
    listaDeUsuarios.append(dictUsuarios)
    

    return listaDeUsuarios

def Login(listaDeUsuarios, isUsuarioOnline):
    emailLogin = input("Digite seu email:")
    senha = input("Digite seu senha:")

    for usuario in listaDeUsuarios:
        for email in usuario:
            if emailLogin in listaDeUsuarios:
                if listaDeUsuarios[emailLogin]['senha'] == senha: 
                    isUsuarioOnline = True
            else:
                isUsuarioOnline = False


    return isUsuarioOnline

def chatzin():

    pass


if __name__ == "__main__":
    vmenu = 1
    isUsuarioOnline = False
    listaDeUsuarios = []
    while vmenu == 1:
        getMenu()

        resposta = input("Selecione uma opção:")
        if resposta== '1':
            #Cadastro
            listaDeUsuarios  = Cadastro(listaDeUsuarios)
            
            print(listaDeUsuarios)
        elif resposta == '2':
            #Login
            if isUsuarioOnline:
                print("Usuario já logado")
            else:    
                isUsuarioOnline = Login(listaDeUsuarios, isUsuarioOnline)
        elif resposta== 3:
            #Chat de voz
            pass
        elif resposta == 4:
            
            print("Selecione uma opção:")
            vmenu = 0
            
            break
        else:
            print("Opção invalida! Digite os valores")

    print("Execução encerrada! Volte sempre!")