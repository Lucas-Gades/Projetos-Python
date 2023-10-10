from pandas import pandas as pd
from collections import defaultdict

nomes = ["LUCAS", "JESSICA", "ROBERTO"]
idades= [22 , 22 ,25]
pesos = ["69 KG", "70.5 KG","55.6 KG"]
alturas = [1.47 , 1.73, 1.82]
imc = [31.3 , 22.7, 42.2]
classificacaos=["OBSIDADE", "NORMAL", "OBSIDADE GRAVE"]
obsidades =[3, 0, 2]

def menu():
    print ("********** MENU **********")
    print ("1 - INCLUIR ALUNO")
    print ("2 - LISTAR TODOS ALUNOS E SEUS DADOS")
    print ("3 - LISTAR OS DADOS DE UM ALUNO")
    print ("4 - LISTAR DADOS DOS ALUNOS DE UMA DETERMINADA IDADE")
    print ("9- FIM")
    print ("Opção: ",end="")

def incluir():
    cont = 1
    while cont > 0:
        nome = input("Digite o nome do aluno que deseja incluir: ").upper()
        while nome not in nomes :
            try:
                idade= int(input("Digite a idade do aluno: "))
                while idade > 0:
                    try:
                        peso = int(input("Digite o peso do aluno: "))
                        while peso > 0:
                            try:
                                altura = input("Digite a altura do aluno: ")
                                y = altura.replace("," , ".")
                                a = float(y)
                                while a > 0.9:
                                    calculoImc= round(peso / (a* a), 1)
                                    nomes.append(nome)
                                    idades.append(idade)
                                    gt = str(peso)
                                    gf = (gt +" KG")
                                    pesos.append(gf)
                                    alturas.append(a)
                                    imc.append(calculoImc)
                                    print("\nALUNO INCLUIDO\n")
                                    return
                                else:
                                    print("ALTURA INVALIDA")
                                    altura = input("Digite outra altura do aluno: ")
                            except:
                                print("ERRO NA ALTURA")
                                print("VERIFIQUE SE COLOCOU '.' NO LUGAR DA ,")
                        else:
                            print("PESO INVALIDO")
                            peso = int(input("Digite outro peso do aluno: "))
                    except:
                        print("ERRO NO PESO")
                else:
                    print("IDADE MENOR QUE 1")
                    idade= int(input("Digite outra idade do aluno: "))
            except:
                print("ERRO NA IDADE")
        else:
            print("NOME JÁ ESTA INCLUIDO NA LISTA")
            cont = 1
    else:
        print("\nABA DE INCLUSÃO FINALIZADA\n")
        return

def mediaImc():

    for i in imc:
        ids= imc.index(i)
        if imc[ids] < 18.5:
            classificacaos.insert(ids , "MAGREZA")
            obsidades.insert(ids , 0)
        elif imc[ids] >= 18.5 and imc[ids] <= 24.9:
            classificacaos.insert(ids , "NORMAL")
            obsidades.insert(ids , 0)
        elif imc[ids] >= 25.0 and imc[ids] <= 29.9:
            classificacaos.insert(ids , "SOBREPESO")
            obsidades.insert(ids , 1)
        elif imc[ids] >= 30.0 and imc[ids] <= 39.9:
            classificacaos.insert(ids , "OBSIDADE")
            obsidades.insert(ids , 2)
        else:
            classificacaos.insert(ids , "OBSIDADE GRAVE")
            obsidades.insert(ids , 3)


def listarDadosDeTodosOsAlunos():
    print("DADOS DOS ALUNOS:\n")
    if  nomes:
        mediaImc()
        df= pd.DataFrame(zip(nomes , idades , pesos , alturas , imc,classificacaos, obsidades),columns =['NOME', 'IDADE', 'PESO(KG)','ALTURA', 'SEU IMC', 'CLASSIFICAÇÃO', 'NIVEL-OBSIDADE'])
        df = df.sort_values(by='NIVEL-OBSIDADE',  ascending=False)
        df = df.sort_values(by='SEU IMC',  ascending=False)
        semIndice= df.to_string(index=False)
        print("\n",semIndice,"\n\n")
    else:
        print("-------LISTAS ESTÃO VAZIAS---------\n\n")

def listarDadosDeUmAluno():
    cont = 1
    while cont > 0:
        nome = input("Digite o nome do aluno que você deseja saber seus dados: ").upper()
        while nome in nomes :
            i = nomes.index(nome)
            df= pd.DataFrame(zip(nomes , idades , pesos , alturas , imc,classificacaos, obsidades),columns =['NOME', 'IDADE', 'PESO(KG)','ALTURA', 'SEU IMC', 'CLASSIFICAÇÃO', 'NIVEL-OBSIDADE'])
            df = df.sort_values(by='NIVEL-OBSIDADE',  ascending=False)
            df = df.sort_values(by='SEU IMC',  ascending=False)
            lin = df.loc[i]
            print("\n")
            print(lin.to_string(),"\n")
            break
        if nome == "":
            return

        else:
            print("NOME NÃO ENCONTRADO")
            cont = 1

def listarTodosOsAlunosDeUmaIdadeEspecifica():
    cont = 1
    while cont > 0:
        try:
            idade = int(input("Digite a idade que você que buscar de seus alunos: "))
            while idade in idades:
                    keys = defaultdict(list);
                    for key, value in enumerate(idades):
                        keys[value].append(key)
                        df= pd.DataFrame(zip(nomes , idades , pesos , alturas , imc,classificacaos, obsidades),columns =['NOME', 'IDADE', 'PESO(KG)','ALTURA', 'SEU IMC', 'CLASSIFICAÇÃO', 'NIVEL-OBSIDADE'])
                        df = df.sort_values(by='NIVEL-OBSIDADE',  ascending=False)
                        df = df.sort_values(by='SEU IMC',  ascending=False)
                    for i in keys[idade] :
                        lin = df.loc[i]
                        print("\n")
                        print(lin.to_string(),"\n")
                    break
            else:
                print("IDADE NÃO ENCONTRADA")
                cont =1
        except :
                print("IDADE INVALIDA")
                sam = 1
                while sam > 0 :
                    prosseguir = int(input("Deseja continuar procurando? 1- SIM ou 2- NÃO: "))
                    if prosseguir == 1:
                         return listarTodosOsAlunosDeUmaIdadeEspecifica()
                    elif prosseguir == 2:
                        return 
                    else:
                        print("Escolha uma opção valida!!")
                        sam = 1



codigo = 1


while codigo != 9:
    menu()
    try:
        codigo=int(input())
    except:
        print("\nDigite somente opções válidas\n")
        codigo = 10
    if codigo==1:
        incluir()
    elif codigo==2:
       listarDadosDeTodosOsAlunos()
    elif codigo==3:
       listarDadosDeUmAluno()
    elif codigo==4:
       listarTodosOsAlunosDeUmaIdadeEspecifica()
    elif codigo== 9:
        print("ENCERRA O PROGRAMA")
    else:
        print ("Escolhe uma opção válida")
        
print("FIM")
