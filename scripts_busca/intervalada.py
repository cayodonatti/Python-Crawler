#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import codecs
import time

a = raw_input('Digite o primeiro acorde: ').upper()
b = raw_input('Digite o segundo acorde: ').upper()
intervalo = int(raw_input('Digite o espaçamento máximo: '))

start = time.time()

matchs = []

with codecs.open('../cifras_formatadas.json', 'r', 'utf-8') as f:

    for line in f:
        musica = json.loads(line)
        cifra = musica["chords"]

        try:
            index_a = cifra.index(a)
            index_b = cifra.index(b)

            if index_b > index_a and index_b - index_a <= intervalo:
                matchs.append(musica)
        except Exception:
            continue


end = time.time()

for match in matchs:
    print(match["nome"][0].encode("utf-8") + ' - ' + match["artista"][0].encode("utf-8"))

print("Tempo: " + str(end - start))