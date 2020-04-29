#!/usr/bin/python3
"""reducer.py"""

import sys
import json
dizionario = {}
for line in sys.stdin:
    #Costruiamo un dizionario con chiave il simbolo dell'azione e
    # valore l'azione che comprende quindi tutti i campi
    line = line.split('\t')
    simbolo = line[0]
    azione = json.loads(line[1])
    """
    formato dell'oggetto caricato:
    {
        "ticker" : "GDR",
        "open" : "9.46724, 
        "close" : "9.743632",
        "low" : "9.141",
        "high" : "10.287228",
        "volume" : "57393",
        "date" : "2017-04-27"
    }
    """
    #Riempimento del dizionario
    if dizionario.get(simbolo):
       dizionario[simbolo].append(azione)
    else:
        dizionario[simbolo] = [azione]

#Iterarazione sul dizionario per calcolare i vari campi richiesti
for k in dizionario:
    price_min = [] 
    price_max = []
    sum_volums = 0
    for a in dizionario[k]:
        price_min.append(float(a['low']))
        price_max.append(float(a['high']))
        sum_volums+=(int(a['volume']))

    lowest_price = min(price_min)
    hieght_price = max(price_max)
    average_volume = sum_volums/len(dizionario[k])
   
    #calcolo variazione percentuale di prezzo
    dizionario[k] = sorted(dizionario[k], key=lambda a: a['date']) #ordino per data
    initial_price = float(dizionario[k][0]['close'])
    final_price = float(dizionario[k][len(dizionario[k])-1]['close'])
    x_cent_dif = 100 * (initial_price-final_price) / initial_price

    #TODO: RESTITUIRE IL RISULTATO IN ORDINE DECRESCENTE PER VARIAZIONE PERCENTUALE
    print(f'{{\nsimbolo:{k}\nvariazone_percentuale:{x_cent_dif}%\nprezzo_min:{lowest_price}\nprezzo_massimo:{hieght_price}\nvolume_medio:{average_volume}\n}}')