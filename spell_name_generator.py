import names
from wonderwords import RandomWord
import random
import sys

def generate_spell_name(caster_name=80, adj_vs_verb=80, noun_vs_verb=80):
    spell_name_parts = []
    r = RandomWord()

    # Caster Name
    caster = True if random.randint(1,100) <= caster_name else False
    if caster == True:
        name = names.get_last_name()
        spell_name_parts.append(f"{name.title()}'s")

    # 1st non-name word
    if random.randint(1,100) <= adj_vs_verb:
        adj = r.word(include_parts_of_speech=["adjectives"])
        spell_name_parts.append(f"{adj.title()}")
    else:
        if caster:
            verb = r.word(include_parts_of_speech=["verbs"], ends_with="ing")
        else:
            verb = r.word(include_parts_of_speech=["verbs"])
        spell_name_parts.append(f"{verb.title()}")

    # 2nd non-name word
    if random.randint(1,100) <= noun_vs_verb:
        noun = r.word(include_parts_of_speech=["nouns"])
        spell_name_parts.append(f"{noun.title()}")
    else:
        verb_2 = r.word(include_parts_of_speech=["verbs"])
        spell_name_parts.append(f"{verb_2.title()}")

    return " ".join(spell_name_parts)

def print_spell_names(number=10):
    for i in range(0, number):
        print(generate_spell_name())

print_spell_names(int(sys.argv[1]))