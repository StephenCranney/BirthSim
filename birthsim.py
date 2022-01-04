#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:40:30 2019

@author: stephencranney
"""

def birthsim(monthly_conception_probability=.2, pregnancy_miscarriage_probability=.3,
            average_miscarriage_duration=3, postpartum_infertility=3):

    ## birthsim_python: Use Python 3+
    # Individuals input their age, etc. to calculate how many months total
    import numpy 

    #import numpy as np  somehow get this in. If I'm using spyder from anaconda, already in there. 
    from datetime import datetime
    start_date = datetime.strptime(input('Enter Start date in the format m/d/y:'), '%m/%d/%Y')
    end_date = datetime.strptime(input('Enter End date in the format m/d/y:'), '%m/%d/%Y') #Date when you are going to stop trying, not stop being able to have children. 
    number_months= (end_date.year-start_date.year)*12+ (end_date.month - start_date.month) + ((end_date.day-start_date.day)*.3) 
    _children=0
    _conceptions=0
    _miscarriages=0
    _month=1
    monthly_conception_probability= .2
    pregnancy_miscarriage_probability= .3 
    average_miscarriage_duration= 3 # 3 months? Check Michel book.
    _pregnancy_length= 9
    postpartum_infertility=3 
    _nonconceptionmonth=0
    
    
    while _month <= number_months:
            conception = numpy.random.binomial(1, monthly_conception_probability, size=None)
            if conception==1 and _month< number_months: 
                _conceptions= _conceptions+1
                miscarriage = numpy.random.binomial(1, pregnancy_miscarriage_probability, size=None)
                if miscarriage==1: 
                    _miscarriages= _miscarriages+1
                    _month=_month+ average_miscarriage_duration
                if miscarriage==0:
                    _month=_month+ _pregnancy_length+ postpartum_infertility
                    _children= _children+1
            if conception==0:
                _nonconceptionmonth= _nonconceptionmonth+1
                _month= _month+1
    
    print(_children)
