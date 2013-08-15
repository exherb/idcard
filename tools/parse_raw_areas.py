#!/usr/bin/env python
# coding=utf-8

import sys
import json

if __name__ == '__main__':
    raw_area_file = open(sys.argv[1])
    temp_ares = []
    for line in raw_area_file:
        line_parts = line.split(' ')
        if len(line_parts) < 2:
            continue
        valid_line_parts = []
        for line in line_parts:
            line = line.strip()
            if len(line) == 0:
                continue
            valid_line_parts.append(line)
        if len(valid_line_parts) != 2:
            continue
        code = valid_line_parts[0]
        address = valid_line_parts[1]
        temp_ares.append((code, address))

    ares = {}
    for code, address in temp_ares:
        if len(code) == 2:
            province_name, citys = ares.get(code, ('', {}))
            ares[code] = (address, citys)

    for code, address in temp_ares:
        if len(code) == 4:
            provice_code = code[0:2]
            city_code = code[2:4]

            province_name, citys = ares.get(provice_code, ('', {}))
            if address.find(province_name) == 0:
                address = address[len(province_name):]
            city_name, towns = citys.get(city_code, ('', {}))
            citys[city_code] = (address, towns)

    for code, address in temp_ares:
        if len(code) == 6:
            provice_code = code[0:2]
            city_code = code[2:4]
            town_code = code[4:6]

            province_name, citys = ares.get(provice_code, ('', {}))
            city_name, towns = citys.get(city_code, ('', {}))
            if address.find(province_name) == 0:
                address = address[len(province_name):]
            if address.find(city_name) == 0:
                address = address[len(city_name):]
            towns[town_code] = address

    area_file = open(sys.argv[2], 'wb')
    area_file.write(json.dumps(ares, encoding = "utf-8", ensure_ascii = False))

