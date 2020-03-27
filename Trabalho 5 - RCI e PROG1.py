#Trabalho interdisciplinar entre as disciplinas: Redes de Computadores para Internet e Programação I
#Data: dd/11/2017
#Número do grupo: 1
#Membros do grupo:
#Éllen Neves
#Maria Gabriela Tavares
#Pedro Caio Miranda
#Sidenir Junior
#Bibliografia consultada: https://www.youtube.com/watch?v=mrbG8B6Gqfs&feature=youtu.be e professores de programação e redes.

def f_converteDecBi(bi, j): #Função que converte número decimal para binário, usando um valor em decimal e um contador de posições como parâmetros.
	dec = int(bi[j]) #Atribui à variável dec o valor inteiro da posição j do número em decimal 
	oc = "" #Atribui à variável oc uma string vazia
	while dec > 0 : #Cria um loop que tem como condição a variável dec ser maior que 0
		resto = dec % 2 #Atribui à variável resto o resto da divisão inteira de dec por 2
		oc = str(resto) + oc #Atribui à variàvel octeto a string da variável resto concatenada ao valor anterior da variável
		dec = dec // 2 #Atribui a variável dec o valor da divisão inteira de seu valor anterior por dois
	octeto = f_preenchezero(oc) #Invoca função
	return octeto #Retorna o octeto em binário

def f_converteBiDec(bi): #Função que converte um número binário para decimal
	j = 0 #Define uma variável como contador
	decF = [] #Define a variável decF como uma lista vazia
	while j < (len(bi)) : #Cria um loop cuja condição é j ser menor que o tamanho da lista bi (que é um número binário)
		biF = bi[j] #Define biF como a posição j de bi
		exp = 0 #Define o expoente como zero
		i = 7 #Define o índice como 7
		dec = 0 #Define o decimal como 0
		while i >= 0 : #Cria um loop cuja condição é o índice ser maior ou igual à 0
			dec = ((int(biF[i])) * (2**exp)) + dec #Define dec como o valor anterior do mesmo mais o inteiro da posição i de biF vezes 2 elevado à um expoente predeterminado
			exp = exp + 1 #Define expoente como o mesmo mais 1
			i = i - 1 #Define o índice como o mesmo menos 1
		decF = decF + [str(dec)] #Define decF como seu valor anterior concatenado à string de dec
		j = j + 1 #Define j como o mesmo adicionado à 1
	return decF #Retorna o número em decimal

def f_preenchezero(oc): #Função que preenche os "bits" restantes do valor em binário com zeros
	qnt = 8 - len(oc) #Define a variável qnt como a quantidade de "bits" que faltam, definidos por 8 subtraído do tamanho de 1's do octeto
	zeros = qnt * "0" #Define a variável zeros como a quantidade de strings "0" que devem ser adicionadas
	oc = zeros + oc #Acrecenta os zeros aos bits iniciais para conclusão do octeto
	return oc #Retorna o octeto

def f_pontinho(end): #Função que adiciona o ponto entre os octetos dos endereços
	i = 0 #Define o índice como 0
	oc = "" #Define oc como uma string vazia
	while i < (len(end) - 1): #Cria um loop cuja condição é o índice ser menor que o tamanho da lista do endereço menos 1
		oc = oc + str(end[i]) + "." #Define octeto como o mesmo concatenado à string da posição i da lista do endereço
		i  = i + 1 #Adiciona 1 ao índice
	i = len(end) - 1 #Redefine o índice como o tamanho da lista do endereço menos 1
	oc = oc + str(end[i]) #Adiciona o último octeto ao endereço
	return oc #Retorna o endereço

def f_broadcast(masc, sub): #Função que calcula a rede de broadcast
	posicoes = [] #Cria uma lista vazia para as posições
	lista1 = [] #Cria uma lista onde será armazenada todas as posições
	broad = [] #Cria uma lista onde será armazenado o broadcast
	for i in range(len(masc)): #Cria um loop cujo ponto de parada é o tamanho da máscara de subrede
		lista = [] #Cria e reseta uma lista vazia
		for j in range(len(masc[i])) : #Cria um loop cujo ponto de parada é o tamanho da posição i da máscara
			if masc[i][j] == "0" : #Cria uma condição que a posuição j da posição i seja igual a string de zero
				posicoes = [j] #Atribui a lista do valor de j à lista posicoes
			lista = lista + posicoes #Atribui posicoes à lista lista
		lista1 = lista1 + [lista] #Atribui lista à lista1
	for x in range(len(sub)): #Cria um loop cujo ponto de parada é o tamanho da subrede
		broad1 = [] #Atribui à broad1 uma lista vazia
		for y in range(len(sub[x])): #Cria um loop cujo ponto de parada é o tamanho da posição x da subrede
			broad = broad + [sub[x][y]] #Atribui à broad o valor da posição y da posição x da subrede
			if y in lista1[x] : #Cria uma condição na qual y deve estar presente na posição x de lista1
				broad[x*8+y] = "1" #"Liga" o "bit" de broadcast
		broad1 = broad1 + [broad] #Adiciona a lista da variável broad à broad1
	cont = 0 #Zera a variável contador
	octetos = [] #Cria uma lista vazia de octetos
	for e in range(4): #Cria um loop cujo ponto de parada é e igual a 4
		octeto = [] #Inicializa uma lista vazia de bits de octeto
		for s in range(8): #Para cada bit do octeto
			octeto.append (broad1[0][cont]) #Adiciona o bit ao octeto
			cont += 1 #E adiciona 1 ao contador
		octetos.append (octeto) #Adiciona o octeto à lista de octetos
	return octetos #Retorna

def f_subredebi(bi,masc): #Função que calcula a subrede em binário e tem como parâmetro as variáveis do endereço IP e da máscara do subrede
	lista = [] #Cria uma lista vazia
	for i in range(len(bi)): #Cria um loop cujo ponto de parada é i igual ao tamanho do endereço IP
		sub = "" #Define a variável da subrede como uma string vazia
		for j in range(len(bi[i])): #Cria um loop cujo ponto de parada é o tamanho do octeto i do endereço IP
			if bi[i][j] == masc[i][j] and bi[i][j] == "1": #Usa a operação AND da tabela verdade para o cálculo da subrede
				sub += "1" #Define a subrede como o valor anterior concatenado à string 1
			else:
				sub += "0" #Define a subrede como o valor anterior concatenado à string 0
		lista.append(sub) #Adiciona subrede à lista
	return lista #Retorna a lista

def f_separaip(bi): #Função que separa os endereços de IP e máscara de subrede informados para possibilitar o uso das demais funções 
	posipont = [] #Define a posição dos pontos como uma lista vazia
	ipF = [] #Define o IP final como uma lista vazia
	x = 0 #Define X como zero
	aux = 0 #Define a variável auxiliar como zero
	for j in range(len(bi)): #Cria um loop cujo ponto de parada é j ser o tamanho do endereço informado
		if bi[j] == "." : #Cria uma condição para identificar as strings de ponto
			posipont = posipont + [j] #Define a posição do ponto como o mesmo adicionado à posição do ponto
	posipont = posipont + [len(bi)] #Define a posição do ponto como o mesmo adicionado ao tamanho do endereço
	for i in posipont : #Cria um loop cujo ponto de parada seja a posição de parada é a variável posipont
		aux = int(bi[x:i]) #Define a variável auxiliar como o inteiro da posição x à posição i do endereço
		ipF = ipF + [aux] #Define o IP final como o mesmo adicionado à lista da variável auxiliar
		x = i + 1 #Define X como i somado à 1
	return ipF #Retorna o IP final

def f_concatenaOc(oc): #Função que concatena os bits de um octeto
	junto = ""
	for digito in oc:
		junto = junto + digito
	return junto

def main(args): #Função principal que invoca todas as outras funções e imprime os valores
	bi2 = []
	masc2 = []
	sub = []
	broad = []
	ip = input("Digite o IP: ") #Pede ao usuário o endereço IP em decimal
	masc = input("Digite a máscara de subrede: ") #Pede ao usuário o endereço da máscara de subrede em decimal
	bi = f_separaip(ip) #Invoca a função para separar os octetos
	biP = f_pontinho(bi) #Invoca a função para colocar os pontos entre os octetos
	print ("IP = ", biP) #Imprime o endereço IP em decimal
	for j in range(len(bi)): #Cria um loop cuja condição é o tamanho do endereço IP em decimal
		bi2 = bi2 + [f_converteDecBi(bi, j)] #Define o endereço IP em binário e invoca a função de conversão de decimal para binário
	bi2P = f_pontinho(bi2) #Invoca a função para colocar os pontos entre os octetos
	print ("Binário = ", bi2P) #Imprime o endereço IP em binário
	masc1 = f_separaip(masc) #Invoca a função que separa os endereços IP
	masc1P = f_pontinho(masc1) #Invoca a função para colocar os pontos entre os octetos
	print ("Máscara = ", masc1P) #Imprime a máscara de subrede em deciaml
	for j in range(len(masc1)): #Cria um loop cujo ponto de parada é o tamanho da máscara
		masc2 = masc2 + [f_converteDecBi(masc1, j)] #Define o endereçoda máscara em binário e invoca a função de conversão de decimal para binário
	masc2P = f_pontinho(masc2) #Invoca a função para colocar os pontos entre os octetos
	print ("Binário = ", masc2P) #Imprime a máscara de subrede em binário
	for j in range(len(masc2)): #Cria um loop cujo ponto de parada é o tamanho da máscara de subrede em binário
		sub = f_subredebi(bi2, masc2) #Invoca a função de cálculo de subrede
	subDec = f_converteBiDec(sub) #Define o endereço de subrede de binário para decimal
	subDecP = f_pontinho(subDec) #Invoca a função para colocar os pontos entre os octetos
	subP = f_pontinho(sub) #Invoca a função para colocar os pontos entre os octetos
	print ("Subrede = ", subDecP) #Imprime o endereço de subrede em decimal
	print ("Binário = ", subP) #Imprime o endereço de subrede em binário
	broadcast = f_broadcast(masc2, sub) #Invoca a função de broadcast
	broad = f_converteBiDec(broadcast) #Invoca a função de conversão
	broad2 = f_pontinho(broad) #Invoca a função de colocação de ponto
	print ("Broadcast = ", broad2) #Imprime o broadcast em decimal
	broadcastJunto = [] #Junta os octetos
	for octeto in broadcast: #Cria um loop
		broadcastJunto.append(f_concatenaOc(octeto)) #Concatena os octetos
	broadB = f_pontinho(broadcastJunto) #Invoca a função para junção de pontos
	print ("Binário = ", broadB) #Imprime o broadcast em binário
	return 0

if __name__ == '__main__': #Inicia o programa, invocando a função principal
	import sys
	sys.exit(main(sys.argv))
