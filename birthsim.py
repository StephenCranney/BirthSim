#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:40:30 2019

@author: stephencranney
"""

## birthsim_python: Use Python 3+
# Individuals input their age, etc. to calculate how many months total
import numpy 

#import numpy as np  somehow get this in. If I'm using spyder from anaconda, already in there. 
from datetime import datetime
start_date = datetime.strptime(input('Enter Start date in the format m/d/y:'), '%m/%d/%Y')
end_date = datetime.strptime(input('Enter End date in the format m/d/y:'), '%m/%d/%Y') #Date when you are going to stop trying, not stop being able to have children. 
number_months= (end_date.year-start_date.year)*12+ (end_date.month - start_date.month) + ((end_date.day-start_date.day)*.3) 
children=0
conceptions=0
miscarriages=0
month=1
monthly_conception_probability= .2
pregnancy_miscarriage_probability= .3 
average_miscarriage_duration= 3 # 3 months? Check Michel book.
pregnancy_length= 9
postpartum_infertility=3 
nonconceptionmonth=0


while month <= number_months:
        conception = numpy.random.binomial(1, monthly_conception_probability, size=None)
        if conception==1 and month< number_months: 
            conceptions= conceptions+1
            miscarriage = numpy.random.binomial(1, pregnancy_miscarriage_probability, size=None)
            if miscarriage==1: 
                miscarriages= miscarriages+1
                month=month+ average_miscarriage_duration
            if miscarriage==0:
                month=month+ pregnancy_length+ postpartum_infertility
                children= children+1
        if conception==0:
            nonconceptionmonth= nonconceptionmonth+1
            month= month+1

print(children)