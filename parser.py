import json
from operator import add

cifras_only = []

w = open('cifras_formatadas.json', 'w')

with open('cifras.json', 'r') as f:
    for line in f:
        if line[:1] == '[' or line[:1] == ']':
            continue

        if line[-2] == ',':
            musica = json.loads(line[:-2])
        else:
            musica = json.loads(line[:-1])

        if len(musica['chords']) < 1:
            continue

        cifra = {
            'nome': musica['music_name'],
            'artista': musica['artist_name'],
            'chords': reduce(add, musica['chords'])
        }

        if len(cifra['chords']) > 0:
            print(json.dumps(cifra))
            w.write(json.dumps(cifra) + '\n')