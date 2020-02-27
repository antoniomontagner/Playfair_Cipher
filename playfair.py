#-*- coding: utf-8 -*-

#chave
k_word = input("key word: ").replace(" ","").upper()
def uni(ch):                    #nao reptir a letra
    s = set()
    for x in ch:
        if x not in s:
           s.add(x)
           yield x

def key(k_word):                #juntar as letras
    k_word = k_word.replace("J","I")
    alfa = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    d = ''.join(uni(k_word+alfa))
    return d

def matrix(d):                  #matriz para a chave
    m = []
    flag=0    
    for i in range(5):
        x = []
        m.append(x)
        for j in range(5):
           x.append(d[flag])
           flag+=1
    return m

#def utilizada na def "enc" e "dec"
def use(st):
    pares=[]
    for i in range(0,len(st),2):
        pares.append(st[i]+st[i+1])
    lis = matrix(key(k_word))         #chave
    linha = []
    coluna = []
    for k in pares:
        for l in k: 
            for i in lis:
                for j in i: 
                    if l == j:
                        linha.append(lis.index(i))
                        coluna.append(i.index(j))
    return pares,linha,lis,coluna       #retorna o index da coluna e linha na matriz

# encriptacao
def enc():
    string = input("text to encrypt: ").replace(" ","").upper().replace(",","").replace("'","")
    for i in range(len(string)-1):      #verifica se tem duas letras iguais seguidas
        if string[i]==string[i+1]:
            string = string[:i+1]+"X"+string[i+1:]
    if (len(string)%2)!=0:              #verifica se o numero de caracteres é impar
        string = string[:]+"X"
    string=string.replace("J","I").replace("É","E").replace("Ã","A").replace("Á","A").replace("Õ","O").replace("Ç","C").replace("."," ")
    pares,linha,lis,coluna = use(string)    #def use()
    cod = []
    linha_cod = []
    coluna_cod = []
    for i in range(0,len(coluna),2):        #verificar se esta na mesma coluna
        if coluna[i]==coluna[i+1]:
            linha[i] = linha[i]+1
            linha[i+1] = linha[i+1]+1
    for i in range(0,len(coluna),2):        #
        coluna_cod.append(coluna[i+1])
        coluna_cod.append(coluna[i])
    cripto = []
    cont = 0
    for i in linha:                         #
        cont_coluna = coluna_cod[cont]
        if i==5:
            a = lis[0][cont_coluna]
            cripto.append(a)
        else:
            a = lis[i][cont_coluna]
            cripto.append(a)
        cont+=1
    cod = []
    for i in range(0,len(cripto),2):        #para retornar os pares
        a = cripto[i]
        b = cripto[i+1]
        cod.append(a+b)
    print("Encryption: ")
    print(cod)

# decriptacao da str / basicamente igual ao enc()
def dec():
    decrypt  =  input("text to decrypt: ").replace(" ","").upper().replace(",","").replace("'","")
    pares,linha,lis,coluna = use(decrypt)
    cod = []
    linha_cod = []
    coluna_cod = []
    for i in range(0,len(coluna),2):        #
        if coluna[i] == coluna[i+1]:
            linha[i] = linha[i]-1
            linha[i+1] = linha[i+1]-1  
    for i in range(0,len(coluna),2):
        coluna_cod.append(coluna[i+1])
        coluna_cod.append(coluna[i])
    cripto = []
    cont = 0
    for i in linha:
        cont_coluna=coluna_cod[cont]
        if i == -1:                         #
            a = lis[4][cont_coluna]
            cripto.append(a)
        else:
            a = lis[i][cont_coluna]
            cripto.append(a)
        cont+=1
    cod = []
    for i in range(0,len(cripto),2):
        a = cripto[i]
        b = cripto[i+1]
        cod.append(a+b)
    print("Decryption: ")
    print(cod)

while(1):
    print("-="*30)
    choice = int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT :"))
    if choice==1:
        enc()
    elif choice==2:
        dec()
    elif choice==3:
        exit()
    else:
        print("Choose correct choice")