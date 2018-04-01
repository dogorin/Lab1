import pyowm

print('OpenWeatherMap')

owm = pyowm.OWM('e1a5cb0c92497ac487240e8c1a3820b6')

observation = owm.weather_at_place('Rostov-on-Don,ru')

weather = observation.get_weather()


def WhatIsCloudness():
    if 0 <= weather.get_clouds() <= 10:
        return 'ясная'

    if 10 < weather.get_clouds() <= 30:
        return 'немного облачная'

    if 30 < weather.get_clouds() <=70:
        return 'пасмурная'

    if 70 < weather.get_clouds() <= 70:
        return 'мрачная'

translate = {'Rostov-na-Donu': 'Ростов-на-Дону', 'Moscow': 'Москва'}

print('Погода в городе'   + ' '
+ WhatIsCloudness() + ', температура '
+ str(weather.get_temperature('celsius')['temp']) + '  ' + 'градус цельсия ' +
 ' скорость ветра ' + str(weather.get_wind()['speed']) + 'м/c.' )