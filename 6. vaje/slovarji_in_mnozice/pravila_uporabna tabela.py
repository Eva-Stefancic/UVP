# ključi so nespremenljivega tipa.
# Kateri tip podatkov je nespremenljiv? Niz, števila, nabori, logične vrednosti
# ključi znotraj enega slovarja morajo biti vsi različni, gesla so pa lahko karkoli
# množice so primer slovarjev, imaj {}, so nespremenljivega tipa, nimajo gesla
# prazen slovar: {}
# prazna množica: set()
# kličemo slovarje: slovar [ključ] = vrednost
# kako pogledamo kakšno vrednost ima ključ? x = slovar[ključ]
# vrednost lahko pogledamo tudi s pomočjo metode get: slovar.get(ključ) .... None
# privzeta vrednost za ključe, ki jih ni v slovarju: slovar.get(ključ, vrednost)

# zanka po vseh ključih v slovarju: for k in s ali pa: for k in s.keys()
# zanka po vseh vrednostih: for v in s.values()
#lahko gremo tudi po parih: for k, v in s.items()

# imena funkcij, ki jih lahko uporabljamo za strukture:

# struktura / ime / prazen / dodaj 1 element / dodaj več elementov
# niz / str / "" / niz += znak / niz += niz2
# nabor / tuple / () / (se ne da) / (se ne da)
# seznam / list / [] / s.append(elt) ali s +=[elt] / s.extend(s2) ali s += s2
# slovar / dict / {} / s[k] = v / s.update(s2)
# množica / set / set() / s.add(elt) / s.update(s2)
