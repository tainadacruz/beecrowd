# -*- coding: utf-8 -*-
#URI 3058 - Supermercado

n = int(input()) #entrada do número de supermercados próximos de Maria
precos = []*n #inicialização do vetor que guardará os preços
gramas = []*n #inicialização do vetor que guardará as gramas
result = [None]*n #inicialização do vetor que guardará o resultado dos cálculos.
#o None serve para preencher o vetor com espaços vazios, para que seja possível inserir dados com o operando "="

#laço que vai preencher os vetores precos e gramas
for i in range(n): #para cada supermercado próximo, faça...
    p,g = input().split() #entrada das variáveis que recebem o preço e a grama de cada supermercado
    #definição do tipo de variável:
    p = float(p)
    g = int(g)
    
    precos.insert(i,p) #insere p na posição i do vetor
    gramas.insert(i,g) #insere g na posição i do vetor

#laço que realizará o cálculo do preço para cada supermercado
for j in range(n): #para cada supermercado próximo, faça
    
    #regra de três que calcula o preço da carne para 1kg (1000 gramas), dependendo da posição de cada valor
    result[j] = (1000 * precos[j]) / gramas[j]
 
#variável que recebe o menor valor dentro do vetor result
final = min(result)
print("%.2f"%(final)) #saída que mostra o menor preço, arredondando duas casas após a vírgula