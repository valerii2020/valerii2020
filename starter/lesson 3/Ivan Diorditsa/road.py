number = 1234
BAD_NUMBER1 = 9876
BAD_NUMBER2 = 5432

vehicle_type = 'грузовик'

if number == BAD_NUMBER1 or number == BAD_NUMBER2:
    print("номер принадлежит угнанному авто")
# без отступов
    print("ГИБДД выехали")
    #print("10")
elif vehicle_type == 'грузовик':
    print('потолки на парковке слишком низкие для грузовых автомобилей')
else:
    print("открываем шлакбаум")
