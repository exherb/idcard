import json


def main():
    areas = json.load(open('raw_areas.json'))

    provinces = areas['province']
    structed_provinces = {}
    for province in provinces:
        id = province['id']
        text = province['text']
        province_id = int(id[0:2])
        structed_provinces[province_id] = {
            'id': id,
            'text': text,
            'cities': {}
        }

    cities = areas['city']
    for city in cities:
        id = city['id']
        text = city['text']
        province_id = int(id[0:2])
        city_id = int(id[0:4])
        structed_province = structed_provinces[province_id]
        structed_province['cities'][city_id] = {
            'id': id,
            'text': text,
            'districts': {}
        }

    districts = areas['district']
    for district in districts:
        id = district['id']
        text = district['text']
        province_id = int(id[0:2])
        city_id = int(id[0:4])
        district_id = int(id)
        structed_province = structed_provinces[province_id]
        structed_city = structed_province['cities'][city_id]
        structed_city['districts'][district_id] = {
            'id': id,
            'text': text
        }
    to_file = open('../idcard/areas.json', 'w')
    to_file.write(json.dumps(structed_provinces))

if __name__ == '__main__':
    main()
