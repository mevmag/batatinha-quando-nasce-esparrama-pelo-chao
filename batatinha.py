import numpy as np

######################################################################################################################################

arquivo = input("Insira o nome do arquivo a ser aberto: ")

#####################################################################################################################################

print("Insira as faixas de energias, em eV, que você deseja trabalhar:")
energ_Inicial = float(input("Energia inicial: "))
energ_Final = float(input("Energia final: "))

print("\nInsira a porcentagem que deseja aumentar ou diminuir das seções de choque dessa faixa de energia:")
print("Caso deseja aumentar, insira apenas o número, caso deseje diminuir, insira um sinal menos antes.")
print("Exemplo: \nPara aumentar 1%, digite 1. Para diminuir 1%, digite -1.")

porcentagem = float(input("Insira a porcentagem: "))

#####################################################################################################################################

def num_Dados(arquivo):

  with open(arquivo, "r") as arq: #apenas abrindo o arquivo

    i = 0

    for linha in arq:

      if(i==6): #a sexta linha do arquivo de dados do tipo .ace possui os valores da quantidade de dados de cada tipo que há no arquivo
        valores_energ = linha

      elif(i==10):
        valores_sig = linha
      
      elif(i>10):
        break

      i+=1

    valores_energ = valores_energ.split() #o 3º valor (valores[2]) é a quantidade de dados de energias que possuímos no arquivo
    valores_sig = valores_sig.split() #o 5º valor dividido por 4 é onde começam as seções de choque totais de fissão

    return valores_energ[2], valores_sig[4]

    #depois colocar dentro desse with open o próprio resto do código,
    #pra abrir uma vez só, usando funções

energ, sig = num_Dados(arquivo)

posicao_energia = float(energ)/4 + 12 #onde terminam as energias
posicao_sig_inicial = float(sig)/4 + 12 #onde começam as seções de choque
#é importante definir ela pois o primeiro valor a partir disso não é um dado de seção de choque
#mas sim uma quantidade informativa de quantas seções de choque desse tipo tem no arquivo.

#####################################################################################################################################

#ESSA FUNÇÃO RETORNA A LINHA E A POSIÇÃO NELA DAS ENERGIAS 
#MAIS PRÓXIMAS ÀS QUE O USUÁRIO PEDIU

def posic_prox(arquivo, energ_Inicial, energ_Final, posicao_energia):

  with open(arquivo, "r") as arq: #apenas abrindo o arquivo

    i = 0 #contagem do valor atual da linha

    posicao_ini = [0,0]
    posicao_fim = [0,0]

    for linha in arq:

      if(i<int(posicao_energia) and i>=12): #se for menor que o limite da posição de dados de energia
        #e for maior que a posição onde se inicial os dados (i=12):

        valores = linha.split() #lista com todos os valores da linha

        for j in range(0,4):
          #se a posição ainda é nula (não foi alterada)
          #e o valor da posição atual (j) é maior que o que o usuário quer para começar
          #esse valor deve ser o primeiro, pois todos os anteriores são menores
          #e ficam fora da faixa definida pelo usuário
          if(posicao_ini == [0,0] and float(valores[j])>float(energ_Inicial)):
            posicao_ini = [i,j]

          #se a posição ainda é nula (não foi alterada)
          #e o valor da posição atual (j) é maior que o que o usuário quer para terminar
          #o valor anterior deve ser o último, pois todos os anteriores são menores
          #e ainda estão dentro da faixa definida pelo usuário, e todos
          #os valores depois deste serão maiores
          if(posicao_fim == [0,0] and float(valores[j])>float(energ_Final)):
            posicao_fim = [i,j-1]

            if((j-1)< 0):
              posicao_fim = [i-1, 3] #se j-1 for menor q 0, 
              #quer dizer que queremos o último valor da linha anterior

      i+=1

    if posicao_fim==[0,0] and posicao_ini!=[0,0]: #caso a energia final seja maior que a
      #maior energia disponível no arquivo de dados, pegamos o último valor disponível como energia final
      
      resto = 100*(posicao_energia%1)
      
      if resto == 0: i=0
      elif resto == 25: i=1
      elif resto == 50: i=2
      elif resto == 75: i=3

      posicao_fim=[int(posicao_energia), i]

    return posicao_ini, posicao_fim


posicao_ini, posicao_fim = posic_prox(arquivo, energ_Inicial, energ_Final, posicao_energia)

#Na realidade, o primeiro valor da seção de quando começam as seções de choque é desconsiderado,
#então queremos sempre o próximo do que é inserido, então:

posicao_ini = [posicao_ini[0], posicao_ini[1]+1]

if posicao_ini[1]+1 > 4:
  posicao_ini = [posicao_ini[0]+1, 0]

posicao_fim = [posicao_fim[0], posicao_fim[1]+1]

if posicao_fim[1]+1 > 4:
  posicao_fim = [posicao_fim[0]+1, 0]

#####################################################################################################################################

nome_novo = "resultado_" + arquivo

resp = open(nome_novo, "w") #criando o arquivo
resp.close

with open(arquivo, "r") as arq: #apenas abrindo o arquivo original

  inicio = int(posicao_sig_inicial) + posicao_ini[0] - 12
  fim = int(posicao_sig_inicial) + posicao_fim[0] - 12

  #subtraimos 12 pois ele está somado tanto da posicao_sig_inicial quanto
  #das posicao_ini e posicao_fim

  with open(nome_novo, "a") as resp:
    porc = porcentagem/100

    i = -1

    for linha in arq: #aqui tá só escrevendo no arquivo criado os dados anteriores

      i+=1

      if(i>=inicio and i<=fim): #a faixa dos 10 valores que serão alterados inicialmente
        valores = linha.split()

        for j in range(0,4):

          if(i!=inicio and i!=fim):
          
            valor = '{:.11E}'.format(float(valores[j])*(1+porc))

            valores[j] = str(valor)
            valores[j] = "   " + valores[j]

          elif(i==inicio):
            if(j>=posicao_ini[1]):
              valor = '{:.11E}'.format(float(valores[j])*(1+porc))

              valores[j] = str(valor)
              valores[j] = "   " + valores[j]

          elif(i==fim):
            if(j<=posicao_fim[1]):
              valor = '{:.11E}'.format(float(valores[j])*(1+porc))

              valores[j] = str(valor)
              valores[j] = "   " + valores[j]  


        linha_real = "".join(valores)
        #print(linha_real, i+1) #i+1 pq no arquivo ele começa a contar do 1, mas no código
        #começa do 0, então i=0 é i=1 no arquivo (qnd for ler manualmente)

        linha_real = linha_real + "\n"

      else:
        linha_real = linha

      resp.write(linha_real)

#####################################################################################################################################

