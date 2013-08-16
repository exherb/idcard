idcard
======

get info from id card number

install
-------

```bash
pip install idcard
```

usage
------

```python
import idcard
print(idcard.parse('1234567890'))
```

```bash
{'province': u'湖南', 'city': '长沙', 'gender': 'male', 'police_station_code': '62', 'town': '雨花区', 'birthday': '2000-01-01', 'valid': True}
```
