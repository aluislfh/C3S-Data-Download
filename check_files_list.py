#! /usr/bin/python

import sys, glob, os
import time
import multiprocessing
import cdsapi

def main():

    PROCESS_LIMIT = 8

    #--------------

    models = ['cmcc','dwd','eccc','ecmwf','meteofrance','ukmo','ncep','jma']

    wdir = '/home/adrian/NWP/S2S_Forecast/Data_C3S/2021'
    os.chdir(wdir)

    #--------------

    print('\n', 'monthly means... ','\n')

    for yyyy in ['2022','2021','2020','2019','2018']:
        for mm in ['01','02','03','04','05','06','07','08','09','10','11','12']:
            for model in models:

                sysv = datesys(yyyy,mm,model)

                if sysv != 'nan':
                    if not os.path.exists('stat_'+model+'_'+yyyy+mm+'01.grib'):
                        print('falta --> stat_'+model+'_'+yyyy+mm+'01.grib')

    #--------------

    print('\n', 'monthly anomalies ... ','\n')

    for yyyy in ['2022','2021','2020','2019','2018']:
        for mm in ['01','02','03','04','05','06','07','08','09','10','11','12']:
            for model in models:

                sysv = datesys(yyyy,mm,model)

                if sysv != 'nan':
                    if not os.path.exists('anomaly_'+model+'_'+yyyy+mm+'01.grib'):
                        print('falta --> anomaly_'+model+'_'+yyyy+mm+'01.grib')

    #--------------

#    print('\n', 'daily data ... ','\n')

#    for yyyy in ['2022','2021','2020','2019','2018']:
#        for mm in ['01','02','03','04','05','06','07','08','09','10','11','12']:
#            for model in models:

#                sysv = datesys(yyyy,mm,model)

#                if sysv != 'nan':
#                    if not os.path.exists('daily_'+model+'_'+yyyy+mm+'01.grib'):
#                        print('daily_'+model+'_'+yyyy+mm+'01.grib')




def datesys(yyyy,mm,model):

# https://confluence.ecmwf.int/display/CKB/Summary+of+available+data

    if model == 'ecmwf':
        if int(yyyy) >= 2018:
            return '5'
        if int(yyyy) == 2022:
            if int(mm) == 11 or int(mm) == 12:
                return '51'

    if model == 'meteofrance':
        if int(yyyy) == 2018:
            return '5'
        if int(yyyy) == 2018:
            if int(mm) == 11 or int(mm) == 12:
                return '6'
        if int(yyyy) == 2019:
            return '6'
        if int(yyyy) == 2019:
            if int(mm) == 10 or int(mm) == 11 or int(mm) == 12:
                return '7'
        if int(yyyy) == 2020:
            return '7'
        if int(yyyy) == 2021:
            return '7'
        if int(yyyy) == 2021:
            if int(mm) >= 7:
                return '8'
        if int(yyyy) == 2022:
            return '8'

    if model == 'ukmo':
        if int(yyyy) == 2018 and int(mm) == 1:
            return '12'
        if int(yyyy) == 2018 and int(mm) != 1:
            return '13'
        if int(yyyy) == 2019:
            if int(mm) <= 4:
                return '13'
        if int(yyyy) == 2019:
            if int(mm) > 4:
                return '14'
        if int(yyyy) == 2020:
            if int(mm) <= 4:
                return '14'
        if int(yyyy) == 2020:
            if int(mm) > 4:
                return '15'
        if int(yyyy) == 2021:
            if int(mm) <= 2:
                return '15'
        if int(yyyy) == 2021:
            if int(mm) >= 3:
                return '600'
        if int(yyyy) == 2022:
            if int(mm) <= 2:
                return '600'
        if int(yyyy) == 2022:
            if int(mm) >= 3:
                return '601'

    if model == 'dwd':
        if int(yyyy) == 2018:
            if int(mm) > 10:
                return '2'
        elif int(yyyy) == 2019:
            return '2'
        elif int(yyyy) == 2020:
            return '2'
        elif int(yyyy) == 2020:
            if int(mm) >= 11:
                return '21'
        elif int(yyyy) == 2021:
            return '21'
        elif int(yyyy) == 2022:
            return '21'
        else:
            return 'nan'

    if model == 'cmcc':
        if int(yyyy) == 2018:
            if int(mm) > 10:
                return '3'
        elif int(yyyy) == 2019:
            return '3'
        elif int(yyyy) == 2020:
            return '3'
        elif int(yyyy) == 2020:
            if int(mm) <= 11:
                return '3'
        elif int(yyyy) == 2020 and int(mm) == 12:
            return '35'
        elif int(yyyy) == 2021:
            return '35'
        elif int(yyyy) == 2022:
            return '35'
        else:
            return 'nan'


    if model == 'ncep':
        if int(yyyy) == 2019:
            if int(mm) >= 10:
                return '2'
        elif int(yyyy) == 2020:
            return '2'
        elif int(yyyy) == 2021:
            return '2'
        elif int(yyyy) == 2022:
            return '2'
        else:
            return 'nan'


    if model == 'jma':
        if int(yyyy) == 2020 and int(mm) >= 10:
                return '2'
        elif int(yyyy) == 2021:
            return '2'
        elif int(yyyy) == 2022 and int(mm) == 1:
            return '2'
        elif int(yyyy) == 2022 and int(mm) != 1:
            return '3'
        else:
            return 'nan'


    if model == 'eccc':
        if int(yyyy) == 2021 and int(mm) >= 5:
                return '2'
        elif int(yyyy) == 2022:
            return '2'
        else:
            return 'nan'






if __name__ == "__main__":
    main()






