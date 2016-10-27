#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 22:43:58 2016

@author: Noahhhhhh
inspect data
"""
## colum names
dt_train.drop([ID, TARGET], axis = 1, inplace = True)
dt_test.drop([ID], axis = 1, inplace = True)