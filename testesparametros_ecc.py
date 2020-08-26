#Programa para calcular os parâmetros de desemepenho de ECCs

#Parâmetros do desempenho
area = float(input("Digite a área ocupada: "))
potencia = float(input("Digite a potencia consumida: "))
latencia = float(input("Digite a latencia: "))

custo = area*potencia*latencia

#Taxa de custo/benfício por quantidade de erro
erros = int(input("Numero de erros corrigidos: "))
taxacorrecao = float(input("Digite a taxa de correçao: "))
t = taxacorrecao*taxacorrecao
taxacb = t/custo
print("A taxa de custo/beneficio para",erros,"erros é: ",taxacb)
