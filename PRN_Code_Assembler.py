#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 19:34:39 2020

@author: paulbourgoin
"""

import ICD_datas
import pylfsr
from pylfsr import LFSR
import brickbrock
import numpy as np
import matplotlib.pyplot as plt


class PRN_Code :
    """ Class defining the sequence of a PRN code with respect to the generation of primary and secondary code."""
    
    def __init__(self,subband,channel,PRN_number,f_ech):
        self.subband = subband
        self.channel = channel
        self.PRN_number = PRN_number
        self.code_freq = ICD_datas.ICD_specifications["code_frequency"]
        self.PrimCode = PrimaryCode(subband,channel,PRN_number)
        self.SecCode = SecondaryCode(subband,channel,PRN_number)
        self.f_ech = f_ech
        self.ech_code_sequences()



    def ech_code_sequences(self):
        self.sequence_prim_code = brickbrock.sampler_sequence(self.PrimCode.sequence,
                                                        self.code_freq,
                                                        self.f_ech)
        secondary_code_freq = self.code_freq/ICD_datas.ICD_specifications[self.subband][self.channel]["primary_code_lenght"]
        self.sequence_sec_code = brickbrock.sampler_sequence(self.SecCode.sequence,
                                                        secondary_code_freq,
                                                        self.f_ech)
        print(self.PrimCode.sequence)
        A=np.fft.fft(np.append(self.sequence_prim_code,self.sequence_prim_code))
        Time=np.arange(0,2*10230*self.f_ech,self.f_ech)
        freqs=np.fft.fftfreq(int(2*10230*self.f_ech/self.code_freq),d=1/self.f_ech)
        
        #plt.plot(self.sequence_prim_code)
        #plt.show()

        
        

        
        
class PrimaryCode :
    """ Class defining the primary code sequence. """
    
    def __init__(self, subband, channel, PRN_number):
        self.sub_band = subband
        self.channel = channel
        self.PRN_number = PRN_number
        self.feedback_tap_R1 = ICD_datas.ICD_specifications[self.sub_band][self.channel]["feedback_tap"]["register_1"]
        self.feedback_tap_R2 = ICD_datas.ICD_specifications[self.sub_band][self.channel]["feedback_tap"]["register_2"]
        self.primary_code_lenght = ICD_datas.ICD_specifications[self.sub_band][self.channel]["primary_code_lenght"]
        self.primaryCodeFrequency = ICD_datas.ICD_specifications["code_frequency"]
        self.start_value_R1 = brickbrock.oct2binList(ICD_datas.ICD_start_value_R1)
        self.start_value_R1.reverse()
        self.start_value_R2 = brickbrock.oct2binList(ICD_datas.ICD_start_value_R2[self.sub_band][self.channel][self.PRN_number])
        self.start_value_R2.reverse()
        self.create_LFSR_register_1()
        self.create_LFSR_register_2()
        self.assemble_prime_code()
        self.codeFrequency = ICD_datas.ICD_specifications["code_frequency"]

    def convert_feedback_tap(self,octal_feedback_tap):
        """ Feedback taps of ICD are octals, need to transform into a list of binaries, and then to create polynoms """
        binary_feedback_tap = list(bin(octal_feedback_tap)[2:-1])
        feedback_tap_polynome = list()
        L = len(binary_feedback_tap)
        for indice in range (L):
            if binary_feedback_tap[indice] == '1' :
                feedback_tap_polynome.append(L-indice)
        return feedback_tap_polynome   

    def create_LFSR_register_1(self):
        feedback_tap_polynome_R1 = self.convert_feedback_tap(self.feedback_tap_R1)
        L1=LFSR(fpoly=feedback_tap_polynome_R1,initstate=self.start_value_R1,verbose=False)
        tempseq=L1.runKCycle(self.primary_code_lenght)
        self.primCodeR1=L1.seq

    def create_LFSR_register_2(self):
        feedback_tap_polynome_R2 = self.convert_feedback_tap(self.feedback_tap_R2)
        L2=LFSR(fpoly=feedback_tap_polynome_R2,initstate=self.start_value_R2,verbose=False)
        tempSeq = L2.runKCycle(self.primary_code_lenght)
        self.primCodeR2=L2.seq

    def assemble_prime_code(self):
        self.sequence = [int(self.primCodeR1[i]^self.primCodeR2[i]) for i in range(self.primary_code_lenght)]


class SecondaryCode :
    """ Class defining the secondary code sequence for a given SVID, channel and sub band """
    
    def __init__(self, subband, channel, PRNnumber):
        self.subband = subband
        self.channel = channel
        self.PRNnumber = PRNnumber
        self.sequence = ICD_datas.ICD_secondary_code_choice[self.subband][self.channel][self.PRNnumber]
        self.chipRate = ICD_datas.ICD_specifications["code_frequency"]/ICD_datas.ICD_specifications[self.subband][self.channel]["primary_code_lenght"]


    
if __name__ == "__main__":
    #P=PrimaryCode("E5a", "I", "1")
    #S=SecondaryCode("E5a", "I", "1")

    #print("\n CODE PRIMAIRE")
    #print("Sequence",P.sequence[:20],"...")
    #print("Frequence",P.codeFrequency)
    #print("Longueur",len(P.sequence))

   # print("\n CODE SECONDAIRE")
   # print("Sequence",S.sequence)
   # print("Frequence",S.chipRate)
   # print("Longueur",len(S.sequence))

   PRN=PRN_Code("E5a","I","1",20e6)
   print(len(PRN.PrimCode.sequence))
   xf=np.fft.fftfreq(len(PRN.sequence_prim_code),PRN.f_ech)
   
   Z=PRN.sequence_prim_code
   A=np.append(Z,Z[0])
   print(A)
   print(len(A))
   A2=np.fft.fft(A)
   print(len(A2))
   B=np.append(A2,A2[0])
   plt.plot(xf,np.real(B[0:-2]))
   plt.show()
   

        
            
