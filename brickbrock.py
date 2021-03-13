#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 19:42:11 2020

@author: paulbourgoin
"""

def oct2bin14bits(oct):
    return f"{oct:015b}"

def oct2binList(oct):
    listInt = oct2bin14bits(oct)        #Contains the list with str values
    listFin = [int(binaryNumber) for binaryNumber in listInt]
    return listFin

def sampler_sequence(sequence, f_sequence,f_ech):
    len_seq = len(sequence)
    rapp_freq = f_ech/f_sequence
    len_sequence_ech = int(len_seq*rapp_freq)
    #print("longueur ech =",len_sequence_ech)
    sequence_ech = list()
    for i in range(len_sequence_ech):
        div_ent = int(i//rapp_freq)
        sequence_ech.append(sequence[div_ent])
    return sequence_ech



if __name__ == "__main__":
    A=[1,0,1,0]
    B = sampler_sequence(A,1/5,1/2)
    print(B)


