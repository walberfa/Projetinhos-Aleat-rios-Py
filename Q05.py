hs=0
mn=0
s=0
n=0
lista=[]
print("Sexo:\n 1-Masculino\n 2-Feminino\nVocê gostou do produto?\n 1-Sim\n 2-Não")
for i in range(10):
  lista.append(input("Digite separado por vírgula:"))
  if(lista[i]=="1,1"): #Homens que votaram sim
    hs=hs+1
    s=s+1
  elif(lista[i]=="1,2"): #Homens que votaram não
    n=n+1
  elif(lista[i]=="2,1"): #Mulheres que votaram sim
    s=s+1
  elif(lista[i]=="2,2"): #Mulheres que votaram não
    mn=mn+1
    n=n+1
print("O número de pessoas que respondeu sim foi: ",s)
print("O número de pessoas que respondeu não foi: ",n)
print("O número de homens que respondeu sim foi: ",hs)
print("O número de mulheres que respondeu não foi: ",mn)