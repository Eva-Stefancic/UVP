PYTHON.py
https://zalozba.fri.uni-lj.si/moskon2020.pdf

nov file: command + n / ctrl + n

interaktivna konzola na macbooku:
command+shift+p
run task
python3 -i
continue without scanning


potenciranje: **
celostevilsko deljenje: //
deljenje po modulu: % (uporabno za definiranje npr sodosti/lihosti)
cela stevila (integer): int
decimalna stevila: floatf5f5
absolutna vrednost: abs(-1) .... dobimo 1


struktura in ime: niz = str (string)
prazen niz: ""
dodaj 1 element: niz += znak
dodaj vec elementov: niz += niz2
sestevanje na nizih: 'niz1' + 'niz2' ... dobimo niz1niz2 , temu pravimo lepljenje nizov oz konkatenacija
mnozenje na nizih: 'niz1' * 3 .... dobimo niz1niz1niz1 (ni pa mozno mnoziti dveh nizov npr. 'niz1'*'niz2' ... Error)
stevila kot nizi: '3' + '5' ... dobimo 35 (tega ni mozno mnoziti, saj sta oba niza, ne pa stevili)

FUNKCIJE
ime_funkcije ( argument_1 , argument_2 , ... , argument_n )

Ce bi zeleli izvedeti, kateremu podatkovnemu tipu pripada nek podatek, bi lahko npr. poklicali funkcijo type:
>>> type (1)                 
< class ’ int ’ >          (vse to pisemo v interaktivno konzolo)
>>> type (1.0)
< class ’ float ’ >
>>> type ( ’ niz ’)
< class ’ str ’ >

FUNKCIJA print:
Funkcija print nam omogoca izpisovanje vrednosti znotraj programov. Poklicemo
jo tako, da ji kot argumente naötejemo vrednosti, ki jih zelimo izpisati in funkcija
print bo vednosti izpisala, vmes bo dala presledke, na koncu izpisa pa bo skocila
v novo vrstico.

FUNKCIJA input:
Funkcija input prav tako kot print na zaslon izpise podan argument. Za razliko
od funkcije print, funkcija input sprejema samo en argument tipa str. Preko
tega argumenta bomo funkciji input podali navodilo za uporabnika. Na primer
takole:
>>> input ( " Vnesi svoje ime : " ) # Funkcija input caka na uporabnikov vnos in pritisk tipke Enter.
>>> ime = input ( " Vnesi svoje ime : " )  # Tako pa uporabnikov vnos shranimo v spremenljivko ime i jo po potrebi kasneje uporabimo.

# 1 T_C = input ( " Vnesi temperaturo v¶ C : " )
# 2 T_F = T_C * 1.8 + 32
# 3 print ( T_C , "¶ C je enako " , T_F , "¶ F . " )
# Program pa v tej obliki zal se ne bo deloval. Funkcija input namrec vedno vrne niz, saj je to podatkovni tip, v katerega lahko zapise karkoli bo pac uporabnik vnesel.
# Tudi ce bo uporabnik vnesel stevilo, bo to predstavljeno kot niz oziroma podatkovni tip str. Kakor se spomnimo od prej pa nizov ne moremo mnoziti z decimalnimi
# stevili pa tudi sestevanje je denifinirano tokrat za nas nekoliko neugodno. Prebrano stevilo, ki je zapisano kot niz, moramo torej pred nadaljnjo obdelavo pretvoriti v
# nekaj, s cimer lahko racunamo, npr. float.

PRETVARJANJE MED PODATKOVNIMI TIPI:
nekaj v niz:
>>> niz = str (20) # stevilo (integer) 20 pretvori v niz (str)
nekaj v celo stevilo:
>>> niz = int (20)              # omejitve: >>> int(6.9) = 6
nekaj v decimalno stevilo:
>>> niz = float (20)

# primer:
# >>> x = 5.4
# >>> str (x)
# ’ 5.4 ’
# >>> int (x)
# 5
# primer:
# 1 niz = input ( " Vnesi temperaturo v C : " )  uporabnik vpiše število
# 2 T_C = float ( niz )                          pretvorba v decimalno število
# 3 T_F = T_C * 1.8 + 32                         enačba, po kateri naj pretvori stopinje v fahrenheite
# 4 print ( T_C , "C je enako " , T_F , "F . " ) - nujne so vejice med deli, saj jih obravnava kot niz.




POGOJNI STAVKI:
