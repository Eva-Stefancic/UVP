re.findall(vzorec,niz) ta vzorec bo poiskal vse nize, dobimo seznam
re.finditer(vzorec, niz) ta pa za razliko od prejsnje ne vrne seznama vseh zadetkov, vendar generira posamezne zadeve - primerna za for zanke. ne vraca nizo, pac pa vrne neke objekte, ki vrnejo nize
re.sub(vzorec, zamenjava, niz) kot neka metoda replace na nizu