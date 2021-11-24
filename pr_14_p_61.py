''' Elaboraţi un program care citeşte de la tastatură două şiruri de caractere şi
afişează pe ecran:
a) caracterele care se întâlnesc cel puţin în unul dintre şiruri;
b) caracterele care apar în ambele şiruri;
c) caracterele care apar în primul şi nu apar în şirul al doilea.'''
a=set(input('dati primul sir :'))
b=set(input('dati al doilea sir sir :'))
print('a) caracterele care se întâlnesc cel puţin în unul dintre şiruri :',a.union(b))
print('b) caracterele care apar în ambele şiruri :',a.intersection(b))
print('c) caracterele care apar în primul şi nu apar în şirul al doilea :',a.difference(b))
