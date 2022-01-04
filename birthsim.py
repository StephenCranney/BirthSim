#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:40:30 2019

@author: stephencranney
"""

def birthsim(monthly_conception_probability=.2, 
             pregnancy_miscarriage_probability=.3, 
             average_miscarriage_duration=3, 
             postpartum_infertility=3):
    
            '''Simulate births, duration in months

    '''
            import numpy
            from datetime import datetime
            
            start_date = datetime.strptime(input('Enter Start date in the format m/d/y:'), '%m/%d/%Y')
            end_date = datetime.strptime(input('Enter End date in the format m/d/y:'), '%m/%d/%Y') #Date when you are going to stop trying, not stop being able to have children. 
            number_months= (end_date.year-start_date.year)*12+ (end_date.month - start_date.month) + ((end_date.day-start_date.day)*.3) 
            #initialize counters
            _children=0
            _conceptions=0
            _miscarriages=0
            _month=1
            monthly_conception_probability= .2
            pregnancy_miscarriage_probability= .3 
            average_miscarriage_duration= 3 # 3 months? Check Guilot book.
            _pregnancy_length= 9
            postpartum_infertility=3 
            _nonconceptionmonth=0
            
            #Simulate each month of pregnancy risk, start at month 1
            while _month <= number_months:
            #Simulate probability of conception for that month
                    conception = numpy.random.binomial(1, monthly_conception_probability, size=None)
            #If a conception is drawn and it is not the last month then iterate number of conceptions
                    if conception==1 and _month< number_months: 
                        _conceptions+=1 
#Randomly draw miscarriage if conception. If the miscarriage is drawn then iterate number of miscarriages
#            and increase month by average miscarriage amount. If no miscarriage then iterature by 
#            pregnancy_length + postpartum infertility. Increase child counter '''
            
                        miscarriage = numpy.random.binomial(1, pregnancy_miscarriage_probability, size=None)
                        if miscarriage==1: 
                            _miscarriages+=1
                            _month=_month+ average_miscarriage_duration
                        if miscarriage==0:
                            _month=_month+ _pregnancy_length+ postpartum_infertility
                            _children= _children+1
            #If conception is 0 then simply iterate to next month.
                    if conception==0:
                        _nonconceptionmonth= _nonconceptionmonth+1
                        _month= _month+1
            
            print(_children)
