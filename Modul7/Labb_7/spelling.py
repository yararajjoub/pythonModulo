"""
Läsa ett bokstaveringsalfabet från en JSON-fil
filen ska innehålla en dikt där bokstäverna i (det engelska) alfabetet är nycklar och deras kodord är värden.
Programmet ska fråga användaren efter ett ord och använda det inlästa bokstaveringsalfabet för att bokstavera ordet.
Kodorden ska skiljas åt av bindestreck.

Exempel på körning:
Word? koala
Kilo-Oscar-Alfa-Lima-Alfa

 """

import json

with open('phonetic_alphabet.json', encoding='utf-8') as f:
    alphabet = json.load(f)

word = input('Word? ').lower()
for letter in word:
    print(alphabet[letter], end='-')

