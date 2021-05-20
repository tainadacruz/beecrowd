# -*- coding: utf-8 -*-
#URI 2947 - Gabarito

k = int(input()) #entrada da quantidade de questões da prova
resposta = list(input()) #entrada das respostas de Desafortunato

todas = [] #inicialização da variável que armazenará as respostas dos colegas de desafortunato
count = 0 #inicialização da variável acumuladora

n = int(input()) #entrada da quantidade de colegas

for i in range(n): #para cada colega, faça
    alunos = list(input()) #recebe as respostas do colega, separadas pela função list()
    
    for j in range(len(alunos)):#para cada resposta, vetor todas a armazenará em uma posição
        todas.append(alunos[j])
            
    
for i in range(k):#para cada questão, faça
    
    repetida = 0 #variável que vai contar as respostas repetidas em uma questão, excluíndo as de Desafortunato
    vetorRepetidas = [] #vetor que armazenará a quantidade de respostas repetidas
    corretas = [] #vetor que armazenará as possíveis respostas corrretas
    
    #para cada resposta dos alunos, o laço vai pular de k em k questões na varredura, assim comparando a mesma questão para todos os alunos
    for p in range(0, len(todas), (k)):
        #se a resposta atual não for igual a resposta de Desafortunato, ela pode ser uma resposta correta
        if todas[p+i] not in resposta[i]: #todas[p+i] porque não é sempre o mesmo aluno a ser verificado
            corretas.append(todas[p+i])
    
    #para cada resposta correta de uma questão, verifica se possui uma resposta equivalente com outro aluno
    for l in range(len(corretas)):
        for j in corretas:
            if j == corretas[l]:
                repetida += 1 #se possui, há mais chance desta resposta ser a correta
        vetorRepetidas.append(repetida) #vetor armazena quantas vezes a alternativa foi marcada pelos alunos
        repetida = 0 #zera a variável para a próxima varredura do laço
            
    maior = 0 #incialização da variável que verifica a maior pontuação possível na turma
    for l in range(len(vetorRepetidas)): #para cada valor inserido no vetor, faça
        if vetorRepetidas[l] > maior: #se o valor é maior do que zero, substitui na variável
            maior = vetorRepetidas[l]
    count += maior #variável armazena o valor provável de maior pontuação na questão
    
print(count) #saída com a resposta



