time = 15
veh_type = 'грузовик'
color = 'black'

if time >= 21:
    print('парковка открыта до 21:00')
else:
    print("шлакбаум открыт")

    if veh_type == 'грузовик':
        print("проедьте пожалуйста на этаж 2")
    else:
        if color == 'black':
            print("цвет чёрный")
        print("проедьте пожалуйста на этаж 1")

    print("добро пожаловать")
