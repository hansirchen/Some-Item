# -*- coding: utf-8 -*-  
import sys,os
homedir=os.getcwd()
sys.path.append(homedir)
import pandas as pd
import pymysql
import json
import re
from xlsxwriter.workbook import Workbook
import csv
from lib import helper
from collections import defaultdict
import codecs
import random
def tree():
    return defaultdict(tree)
def getGCD(a,b):
    return getGCD(b,a%b) if b else a

max_int = 9223372036854775806

for i in range(1,11):
    res,input_list = 1,[]
    num = random.randint(5,10)
    for j in range(1,num+1):
        x = random.randint(2,1000)
        if res * x > max_int:
            break
        input_list.append(x)
        # print(res,x,getGCD(res,x))
        res = res*x //getGCD(res,x)
    input_rows = [[len(input_list)], [' '.join([str(x) for x in input_list])]]
    output_rows = [res]
    print(len(input_list),*input_list)
    print(output_rows)
        
    # with open('D:\Zdata\input\{}'.format(i),'w',newline ='\n') as f:
    #     f_csv = csv.writer(f)
    #     f_csv.writerows(input_rows)

    # with open('D:\Zdata\output\{}'.format(i),'w',newline ='\n') as f:
    #     f_csv = csv.writer(f)
    #     f_csv.writerow(output_rows)

