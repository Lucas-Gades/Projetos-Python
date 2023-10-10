windows_server=[]
unix = []
linux = []
netware = []
mac_os = []
outro = []



def menu():
    print ("********** MENU **********")
    print ("Qual o melhor Sistema Operacional para uso em servidores?")
    print ("As possíveis respostas são:")
    print ("1 - WINDOWS SERVER")
    print ("2 - UNIX")
    print ("3 - LINUX")
    print ("4 - NETWARE")
    print ("5 - MAC OS")
    print ("6 - OUTRO")
    print ("0 - TERMINAR VOTAÇÕES")
    print ("Opção: ",end="")


def votacaoWindows():
    cont = + 1
    windows_server.append(cont)

def votacaoUnix():
    cont = + 1
    unix.append(cont)

def votacaoLinux():
    cont = + 1
    linux.append(cont)

def votacaoNetware():
    cont = + 1
    netware.append(cont)

def votacaoMac():
    cont = + 1
    mac_os.append(cont)

def votacaoOutro():
    cont = + 1
    outro.append(cont)
def clear():
    windows_server.clear()
    unix.clear()
    linux.clear()
    netware.clear()
    mac_os.clear()
    outro.clear()


        

codigo = 1

while codigo != 0:
    menu()
    try:
      codigo=int(input())
    except:
       print("Digite somente opções válidas")
       x=input("ENTER para continuar...")
    if codigo==1:
        votacaoWindows()
    elif codigo==2:
        votacaoUnix()
    elif codigo==3:
        votacaoLinux()
    elif codigo==4:
        votacaoNetware()
    elif codigo==5:
        votacaoMac()
    elif codigo==6:
        votacaoOutro()
    elif codigo==0:
        print("Programa Encerrado\n")
        calculoTotal =len(windows_server) + len(unix)+ len(linux) + len(netware)+len(mac_os) + len(outro)
        if calculoTotal !=0:
                porcentagemWindows = len(windows_server)/calculoTotal
                porcentagemUnix = len(unix)/calculoTotal
                porcentagemLinux = len(linux)/calculoTotal
                porcentagemNetware= len(netware)/calculoTotal
                porcentagemMac = len(mac_os)/calculoTotal
                porcentagemOutro = len(outro)/calculoTotal

                print("Sistema Operacional","   Votos  ", " % ""\n-------------------    -----_  ------") 
                print("WINDOWS SERVER          ",len(windows_server),f"    {porcentagemWindows:.2%}")
                print("UNIX                    ",len(unix),f"    {porcentagemUnix:.2%}")
                print("LINUX                   ",len(linux),f"    {porcentagemLinux:.2%}")
                print("NETWARE                 ",len(netware),f"    {porcentagemNetware:.2%}")
                print("MAC OS                  " , len(mac_os),f"    {porcentagemMac:.2%}")
                print("OUTRO                   ",len(outro),f"    {porcentagemOutro:.2%}")
                print("\nTOTAL                   ",calculoTotal)
                if porcentagemWindows > porcentagemUnix and porcentagemWindows > porcentagemLinux and porcentagemWindows > porcentagemNetware and porcentagemWindows >  porcentagemMac and porcentagemWindows >porcentagemOutro:
                    print("O Sistema Operacional mais votado foi  Windows Server com ",len(windows_server)," VOTOS")
                elif porcentagemUnix > porcentagemWindows and porcentagemUnix > porcentagemLinux and porcentagemUnix > porcentagemNetware and porcentagemUnix >  porcentagemMac and porcentagemUnix>porcentagemOutro:
                    print("O Sistema Operacional mais votado foi  Unix  com ",len(unix)," VOTOS")

                elif porcentagemLinux > porcentagemWindows and porcentagemLinux > porcentagemUnix and porcentagemLinux > porcentagemNetware and porcentagemLinux>  porcentagemMac and porcentagemLinux>porcentagemOutro:
                    print("O Sistema Operacional mais votado foi  Linux com ",len(linux)," VOTOS")
                elif porcentagemNetware> porcentagemWindows and porcentagemNetware > porcentagemUnix and porcentagemNetware > porcentagemLinux and porcentagemNetware>  porcentagemMac and porcentagemNetware>porcentagemOutro:
                    print("O Sistema Operacional mais votado foi  Netware com ",len(netware)," VOTOS")
                elif porcentagemMac > porcentagemWindows and porcentagemMac > porcentagemUnix and porcentagemMac > porcentagemLinux and porcentagemMac>  porcentagemNetware and porcentagemMac> porcentagemOutro:
                    print("O Sistema Operacional mais votado foi  Mac Os com ",len(mac_os)," VOTOS")
                elif porcentagemOutro > porcentagemWindows and porcentagemOutro > porcentagemUnix and porcentagemOutro> porcentagemLinux and porcentagemOutro>  porcentagemNetware and porcentagemOutro > porcentagemMac:
                    print("O Sistema Operacional mais votado foi  Outro com ",len(outro)," VOTOS\n")
                else:
                    print("Empate")
             
                prosseguir=int(input("Se você desejar fazer mais uma votação: Digite 1-SIM ou 2-NÃO: "))
                while prosseguir !=1 and prosseguir !=2:
                     print("OPÇÃO ÍNVALIDA\n\nDIGITE UMA OÇÃO VALIDA")
                     prosseguir=int(input("Se você desejar finalizar a votação: Digite 1-SIM ou 2-NÃO: "))
                if prosseguir == 1:
                                    clear()
                                    codigo=1
                elif prosseguir ==2:
                                  print("Programa Encerrado\n")
                else:
                    print("NINGUEM FOI VOTADO")
                    prosseguir=int(input("Se você desejar fazer mais uma votação: Digite 1-SIM ou 2-NÃO: "))
                    while prosseguir !=1 and prosseguir !=2:
                         print("OPÇÃO ÍNVALIDA\n\nDIGITE UMA OÇÃO VALIDA")
                         prosseguir=int(input("Se você desejar finalizar a votação: Digite 1-SIM ou 2-NÃO: "))
                    if prosseguir == 1:
                                clear()
                    elif prosseguir ==2:
                                    print("Programa Encerrado\n")
                    else:
                        print("NINGUEM FOI VOTADO")
                        prosseguir=int(input("Se você desejar fazer mais uma votação: Digite 1-SIM ou 2-NÃO: "))
                        while prosseguir !=1 and prosseguir !=2:
                             print("OPÇÃO ÍNVALIDA\n\nDIGITE UMA OÇÃO VALIDA")
                             prosseguir=int(input("Se você desejar finalizar a votação: Digite 1-SIM ou 2-NÃO: "))
                        if prosseguir == 1:
                                    codigo = 1
                        elif prosseguir ==2:
                                        print("Programa Encerrado\n")

    else:
        print ("Opção válida, escolha outra")






