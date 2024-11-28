#!/usr/bin/env python3

def return_evens(num_list):
    if len(num_list) > 0:
        return [i for i in num_list if i % 2 == 0]
    else:
        return []

def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]