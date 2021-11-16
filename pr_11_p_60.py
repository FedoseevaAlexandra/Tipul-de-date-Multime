M={'A','B' , 'C', 'D'}
print('submultimile posibile sunt:')
print(M)
m=set()
for a in M:
      for b in M:
         if ord(b)>ord(a):
                       m.update({a,b})
                       print(m)
                       m.clear()
         for c in M:
                   if ord(c)>ord(b) and ord(b)>ord(a):
                       m.update({a,b,c})
                       print(m)
                       m.clear()
      for d in M:
                   if ord(c)>ord(b) and ord(b)>ord(a) and ord(d)>ord(c):
                       m.update({a,b,c,d})
                       print(m)
                       m.clear()
for a in M:
    m.add(a)
    print(m)
    m.clear()
