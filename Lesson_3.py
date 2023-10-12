print('Hello itProger')
good_boy = True  # Мальчик-то неплохой

if not good_boy:
    print('Этот в грязь полез')
    print('и рад,')
    print('что грязна рубаха.')
    print('Про такого говорят:')
    print('он плохой, неряха.')
else:
    print('Этот чистит валенки,')
    print('моет сам галоши.')
    print('Он хотя и маленький,')
    print('но вполне хороший.')


### Задача

mobile_devices = {
    'cucuPhone': 2010,
    'cucuBlet': 2013,
    'cucuClock': 2015,
    'cucuEar': 2018,
    'cuCube': 2015,
}

home_devices = {
    'cucuLot': 2011,
    'cucuBlock': 2010,
    'cucuWall': 2010,
    'cucuMonitor': 2020,
    'cucuLamp': 2015,
    'cucuTable': 2016,
    'cucuTV': 2017,
}

not_supported_devices = {'cucuBlock', 'cucuBlet', 'cucuWall'}

result_catalog = {}



# Допишите функцию выборки поддерживаемого девайса из словаря
def get_supported_catalog(dict_devices, device):
    supported_catalog = {}
    if device in dict_devices:
        ...
    return supported_catalog


all_devices = ...
supported_devices = ...

for device in ...:
    supported_mob_dev = get_supported_catalog(mobile_devices, device)
    # Добавьте значение в словарь result_catalog
    ...
    supported_home_dev = get_supported_catalog(home_devices, device)
    # Добавьте значение в словарь result_catalog
    ...


print('Каталог поддерживаемых девайсов: ')
print(result_catalog)