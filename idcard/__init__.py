#!/usr/bin/env python
# coding=utf-8

import os
import sys
import json

from datetime import datetime

__areas__ = json.loads(open(os.path.join(os.path.dirname(__file__),
                            'areas.json')).read())
__verification_code_map__ = {
    0: '1',
    1: '0',
    2: 'X',
    3: '9',
    4: '8',
    5: '7',
    6: '6',
    7: '5',
    8: '4',
    9: '3',
    10: '2'
}


def parse(id_card_no):
    results = {}

    if len(id_card_no) >= 2:
        provice_code = id_card_no[0:2]
        provice = __areas__.get(provice_code, None)
        if provice:
            results['province'] = provice['text']
            citys = provice['cities']
            if len(id_card_no) >= 4:
                city_code = id_card_no[0:4]
                city = citys.get(city_code, None)
                results['city'] = city['text']
                districts = city['districts']
                if len(id_card_no) >= 6:
                    district_code = id_card_no[0:6]
                    district = districts.get(district_code, None)
                    results['district'] = district['text']

    birthday_year = -1
    birthday_month = -1
    birthday_day = -1
    if len(id_card_no) >= 10:
        try:
            birthday_year = int(id_card_no[6:10])
        except Exception:
            pass
    if len(id_card_no) >= 12:
        try:
            birthday_month = int(id_card_no[10:12])
        except Exception:
            pass
    if len(id_card_no) >= 14:
        try:
            birthday_day = int(id_card_no[12:14])
        except Exception:
            pass
    if birthday_year >= 0 and birthday_month >= 0 and\
       birthday_day >= 0:
        results['birthday'] = datetime(birthday_year, birthday_month,
                                       birthday_day)

    if len(id_card_no) >= 16:
        results['police_station_code'] = id_card_no[14:16]

    if len(id_card_no) >= 17:
        try:
            is_male = int(id_card_no[16:17]) % 2 != 0
            results['gender'] = 'male' if is_male else 'female'
        except Exception:
            pass

    is_valid = len(id_card_no) == 15
    if len(id_card_no) == 18:
        total = 0
        exception = None
        for i in range(1, 18):
            try:
                number = int(id_card_no[i-1])
            except Exception as e:
                exception = e
                break
            efficient = pow(2, 18 - i) % 11
            total += number*efficient
        if not exception:
            is_valid = __verification_code_map__[total % 11] ==\
                id_card_no[17:18]
    results['valid'] = is_valid

    return results

if __name__ == '__main__':
    results = parse(sys.argv[1])
    for key, value in results.iteritems():
        print(u'{0}: {1}'.format(key, value))
