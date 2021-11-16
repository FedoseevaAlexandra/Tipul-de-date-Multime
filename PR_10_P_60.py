M={1, 2, 3, 4}
print('submultimile posibile sunt:')
print(M)
doua=set()
for a in M:
      for b in M:
         if b>a:
                       doua.update({a,b})
                       print(doua)
                       doua.clear()
         for c in M:
                   if c>b and b>a:
                       doua.update({a,b,c})
                       print(doua)
                       doua.clear()
      for d in M:
                   if c>b and b>a and d>c:
                       doua.update({a,b,c,d})
                       print(doua)
                       doua.clear()
for a in M:
    doua.add(a)
    print(doua)
    doua.clear()

