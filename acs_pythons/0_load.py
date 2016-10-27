#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 22:02:05 2016

@author: Noahhhhhh
load the train, test, and sample submission files
"""

## import the packages
import pandas as pd

## paths of train, test, and sample submission files
path_train = "../../data/Allstate_Claims_Severity/train.csv"
path_test = "../../data/Allstate_Claims_Severity/test.csv"
path_submit = "../../data/Allstate_Claims_Severity/sample_submission.csv"

## load data
dt_train = pd.read_csv(path_train)
dt_test = pd.read_csv(path_test)
dt_sampleSubmit = pd.read_csv(path_submit)

print("{},{}".format(dt_train.shape, dt_test.shape))
dt_train.shape[0]
dt_test.shape[0]
