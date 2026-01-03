# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 11:43:07 2025

@author: Wajid_Arshad_Abbasi
"""
import random
from propy.PyPro import GetProDes
import numpy as np
def get_features_proPy_list_Full_des(seq):
        """
        This function takes protein sequence and generate features using
        proPy packege. IN this a search is implemented to get dictionary of all
        terms to get same feature lenght. Normalized fatures will
        be saved at given path with prot id.
        """
        AA=["A", "R", "N", "D", "C", "E", "Q", "G", "H", "I","L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"]
        keyList=np.load('key_list_proPy.npy')
        keyList = np.char.decode(keyList, encoding='utf-8')
        feature=[]
        seq=seq.replace('X',AA[random.randint(0,len(AA)-1)])
        seq=seq.replace('B',AA[random.randint(0,len(AA)-1)])
        seq=seq.replace('U',AA[random.randint(0,len(AA)-1)])
        seq=seq.replace('Z',AA[random.randint(0,len(AA)-1)])
        des=GetProDes(seq)
        propy_FD=des.GetALL()
        for key in keyList:
            try:
                feature.append(propy_FD[key])
            except KeyError:
                feature.append(0.0)
                #feat=feat/np.linalg.norm(feat)
                #print final_feat_dict,features
                #pdb.set_trace()
        return feature   

