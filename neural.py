#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 17:46:52 2022

@author: yabsera
"""

def gender_layer(input_lst):
    weight=[1,0]
    bias=[0,1]
    result=[0,0]
    i=0
    while i<len(input_lst):
        result[i]+=(input_lst[i]*weight[i])+bias[i]
        #print(result[i])
        i+=1
    print(result)
    return result


def lunch_layer(gender_input_lst):
    weight=[1,0]
    bias=[0,1]
    result=[0,0]
    i=0
    while i<len(gender_input_lst):
        result[i]+=(gender_input_lst[i]*weight[i])+bias[i]
        i+=1
    print(result)
    return result


def pa_ed_layer(lunch_input_lst):
    weight=[1,2,3,4,5,6]
    bias=[0,1]
    result=[0,0,0,0,0,0]
    i=0
    while i<len(lunch_input_lst):
        j=0
        while j<len(weight):
            result[j]+=(weight[j]*lunch_input_lst[i])+bias[i]
           # print(result[j])
            j+=1
        i+=1
    print(result)
    return result

def out_put_layer(pa_ed_layer):
    weight=[1,0]
    bias=[0,1]
    result=[0,0]
    i=0
    while i<len(weight):
        j=0
        while j<len(pa_ed_layer):
            result[i]+=(weight[i]*pa_ed_layer[j])+bias[i]
            j+=1
        i+=1
    return result

numbers=[1,0]
output1=gender_layer(numbers)
output2=lunch_layer(output1)
output3=pa_ed_layer(output2)
output4=out_put_layer(output3)

print(output4)











