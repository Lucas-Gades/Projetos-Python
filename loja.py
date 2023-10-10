import pandas as pd


codigo=["XXX", "YYY"]

nome=["MOUSE", "TECLADO"]

estoque=[150 , 100]

vendas=[30 , 20]

qtd=[32 , 50]





def menu():
    print ("********** MENU **********")
    print ("Escolha uma opção:")
    print ("1 - incluir um produto")
    print ("2 - Realizar uma Venda ")
    print ("3 - Listar todas as vendas  de um produto")
    print ("4 - Listar todas as vendas")
    print ("5 - Listar estoque de um Produto")
    print ("6 - Listar estoque de todos Produtos")
    print ("9 - fim")
    print ("Opção: ",end="")


def incluir():
    print("@"*15," INCLUIR ","@"*15)  
    sam = 1
    if sam > 0:
        codigoProduto=input("Digite o codigo do produto que deseja incluir no estoque: ").upper()
        while codigoProduto != "" and sam > 0:
            try:
                if codigoProduto not in codigo:
                   nomeProduto=input("Digite o nome do produto que deseja incluir no estoque: ").upper()
                   if nomeProduto not in nome and nomeProduto != "":
                    cont = 1
                    while cont > 0:
                        try:
                            estoqueProduto=int(input("Digite a quantidade de produtos que deseja incluir no estoque: "))
                            if estoqueProduto >0 and estoqueProduto != 0:
                                            nome.append(nomeProduto)
                                            codigo.append(codigoProduto)
                                            estoque.append(estoqueProduto)
                                            vendas.append(0)
                                            qtd.append(0)
                                            codigoProduto=input("Digite o codigo do produto que deseja incluir no estoque: ").upper()
                                            cont = -1
                                            sam = 1
                        except:
                                print("DIGITE NÚMEROS , NÃO DIGITE LETRAS OU CARACTERES!!")
                                cont = 1

                   else:
                         print("NOME DO PRODUTO JA EXITE NO ESTOQUE")
                         cont = -1
                else:
                    print("CODIGO DO PRODUTO JÁ EXITE NA LISTA")
                    codigoProduto=input("Digite o CODIGO do produto que deseja incluir no estoque QUE NÃO ESTEJA NA LISTA: ").upper()
                    sam == 0
            except:
                print ("o número da quantidade de produtos que deseja colocar no estoque , não poderar ser negativo , deve ser um número positivo !!!")
                estoqueProduto=int(input("Digite a quantidade de produtos que deseja incluir no estoque: "))
                sam = 1
        else:
            return
        print("@"*25)
    else:
        sam == 0
def vendaProduto():
    print("@"*15," VENDER ","@"*15)
    print("Todos os codigos dos produtos que estão no estoque:",codigo )
    codigoProduto=input("Digite o codigo do produto que deseja fazer a venda: ").upper()
    while codigoProduto != "":
     if codigoProduto in codigo:
          i=codigo.index(codigoProduto)
          codigoProduto=codigoProduto.title()
          cont= 1
          while cont > 0 :
              try:
                  quantidadeVendida=int(input("Digite a quantidade que deseja vender: "))
                  if quantidadeVendida < estoque[i] and quantidadeVendida > 0:
                        soma = +1
                        r=vendas[i] + soma
                        vendas.append(r)
                        s= estoque[i] - quantidadeVendida
                        estoque[i] = s
                        y=qtd[i]+ quantidadeVendida
                        qtd[i]= y
                        print("PRODUTO VENDIDO COM SUCESSO!!")
                        prosseguir=int(input("Se você deseja vender mais alguns produtos digite : 1 - SIM ou 2 - NÃO: "))
                        while prosseguir !=1 and prosseguir !=2:
                                            print("OPÇÃO INVALIDA !!!")
                                            prosseguir=int(input("Se você deseja vender mais alguns produtos digite : 1 - SIM ou 2 - NÃO: "))
                        if prosseguir == 1:
                            codigoProduto=input("Digite o codigo do produto que deseja fazer a venda: ").upper()
                            if codigoProduto == "":
                                prosseguir ==2
                            elif codigoProduto not in codigo:
                                cont= -1
                            else:
                                cont = 1
                        elif prosseguir == 2:
                            return
                        else:
                            print ("Escolhe uma opção válida")
                  else:
                      print("Quantidade NÃO PODE SER UM NUMERO NEGATIVO OU SUPERIOR AO QUE TEM NO ESTOQUE")
                      quantidadeVendida=int(input("Digite a quantidade que deseja vender: "))
              except:
                    print("DIGITE NÚMEROS , NÃO DIGITE LETRAS OU CARACTERES!!")
                    cont = 1

     else:
        print("Codigo Não Encontrado")
        codigoProduto=input("Digite o codigo do produto que deseja fazer a venda: ").upper()
              
def listarVenda():
    print("@"*15," LISTAS DE VENDAS DE UM PRODUTO SELECIONADO ","@"*15)
    print("Todos os codigos dos produtos que estão no estoque:",codigo )
    codigoProduto=input("Digite o codigo do produto que deseja verificar todas as vendas: ").upper()
    while codigoProduto != "":
        if codigoProduto in codigo:
                try:
                    i=codigo.index(codigoProduto)
                    df3= pd.DataFrame(zip(codigo , nome , qtd),columns =['CODIGO', 'NOME', 'QUANTIDADE VENDIDA'])
                    lin = df3.loc[i]
                    print(lin.to_string())
                    break
                except:
                    print("Produto Não Existe")
                    codigoProduto=input("Digite o codigo do produto que deseja verificar o estoque: ").upper()
                    break
        else:
            print("PRODUTO NÃO ENCONTRADO")
            codigoProduto=input("Digite o codigo do produto que deseja verificar o estoque: ").upper()

        
def listarTodasVendas():
    print("@"*15," LISTAR TODAS AS VENDAS ","@"*15)
    print("TOTAL DE VENDAS = ",len(vendas))
    dt= pd.DataFrame(zip(codigo , nome , qtd),columns =['CODIGO', 'NOME', 'QUANTIDADE VENDIDA'])
    print(dt)



def listarEstoque():
    print("@"*15," LISTAS DE ESTOQUE DE UM PRODUTO SELECIONADO ","@"*15)
    print("Todos os codigos dos produtos que estão no estoque:",codigo )
    codigoProduto=input("Digite o codigo do produto que deseja verificar o estoque: ").upper()
    while codigoProduto != "":
        if codigoProduto in codigo:
                try:
                    i=codigo.index(codigoProduto)
                    df4= pd.DataFrame(zip(codigo , nome , estoque),columns =['CODIGO', 'NOME', 'QUANTIDADE NO ESTOQUE'])
                    lin = df4.loc[i]
                    print(lin.to_string())
                    break
                except:
                    print("Não conseguimos encontrar...")
                    codigoProduto=input("Digite o codigo do produto que deseja verificar o estoque: ").upper()
        else:
            print("PRODUTO NÃO ENCONTRADO")
            codigoProduto=input("Digite o codigo do produto que deseja verificar o estoque: ").upper()        
        

def listarTodoEstoque():
    print("@"*15," LISTAR TODOS OS PRODUTOS DO ESTOQUE ","@"*15)
    print("TOTAL DE PRODUTOS NO ESTOQUE = ",len(estoque))
    df= pd.DataFrame(zip(codigo , nome , estoque),columns =['CODIGO', 'NOME', 'ESTOQUE'])
    print(df)


op=0
while op!=9:
    menu()
    try:
      op=int(input())
    except:
       print("Digite somente opções válidas")
       x=input("ENTER para continuar...")
    if op==1:
        incluir()
    elif op==2:
        vendaProduto()
    elif op==3:
        listarVenda()
    elif op==4:
        listarTodasVendas()
    elif op==5:
        listarEstoque()
    elif op==6:
        listarTodoEstoque()
    elif op ==9:
        print("Encerra o programa")
    else:
        print ("PÔ MEU escolhe uma opção válida")
print("FIM")
