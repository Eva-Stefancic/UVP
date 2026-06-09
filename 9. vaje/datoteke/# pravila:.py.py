# pravila:
with open (ime, način, encoding = "utf-8") as f:
# način: "r" / "w" / "a".  (read, write, append)
# možnosti, kaj vse lahko delamo na datotekah:
f.read().        \n
f.readlines()
f.readline()

for vrstica in f: 

f.write(niz)
print (vr1, vr2, ...., file = f)

sep = ","  # separator - pri printu 
end = ""  # \n ti zamenja s presledkom

s.strip()             # odstranimo vse bele znake (znak za novo vrstico, presledek, tabulator)
s.split(ločilo)       # niz s razsekamo na podnize glede na neko ločilo
ločilo.join(seznam)   # nize združujemo glede na neko ločilo