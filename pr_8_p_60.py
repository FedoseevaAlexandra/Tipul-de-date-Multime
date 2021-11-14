A=set(input('dati elementele multimii A :'))
B=set(input('dati elementele multimii B :'))
x=0
for i in A:
    if ord(i) not in range(48,58):
        x+=1

for i in B:
   if ord(i) not in range(48,58):
        x+=1
if x>0:
    print('Mulţimile A şi B trebuie sa fie formate din numere întregi.')
if x==0:
  print('intersecţia mulţimilor A şi B =',A.intersection(B))
  print('reuniunea mulţimilor A şi B =',A.union(B))
  print('diferenţa mulţimilor A şi B =',A.difference(B))
  print('diferenţa mulţimilor B şi A =',B.difference(A))