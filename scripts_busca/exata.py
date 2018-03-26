#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import codecs
import time

sequencia = raw_input('Digite a sequencia de acordes: ').upper()

start = time.time()

matchs = []

acordes = sequencia.split(' ')

with codecs.open('../cifras_formatadas.json', 'r', 'utf-8') as f:

    for line in f:
        musica = json.loads(line)
        cifra = ' '.join([x for x in musica["chords"]])

        if sequencia in cifra:
            matchs.append(musica)


end = time.time()

for match in matchs:
    print(match.encode("utf-8"))

print("Tempo: " + str(end - start))