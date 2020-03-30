# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 12:08:14 2020

@author: pkzr3
"""
from statistics import mode
times_list_list=[['11:00', '2:00', '3:00'], ['2:00']]
opt_time = mode([item for sublist in times_list_list for item in sublist])
