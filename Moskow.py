import pyowm

print("OpenWeatherMap")

owm = pyowm.OWM('e1a5cb0c92497ac487240e8c1a3820b6')  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)
observation = owm.weather_at_place('Moscow,ru')
weather = observation.get_weather()
location = observation.get_location()

print(owm)                      # <Weather - reference time=2013-12-18 09:20,
print(observation)
print(weather)
print(location)# status=Clouds>

print('Страна '+ location.get_country() )
print('Город ' + location.get_name())
print('Долгота ' + str(location.get_lon()))
print('Широта ' + str(location.get_lat()))
print('Облачность ' + str(weather.get_clouds()))
print('Статус ' + str(weather.get_detailed_status()))
print('Давление ' + str(weather.get_pressure()))
print('Дождь ' + str(weather.get_rain()))
print('Снег ' + str(weather.get_snow()))
print('Время '+ str(weather.get_reference_time('iso')))
print('Статус ' + str(weather.get_status()))
print('Восход ' + str(weather.get_sunrise_time('iso')))
print('Закат ' + str(weather.get_sunset_time('iso')))
print('Температура ' + str(weather.get_temperature('celsius')))
print('Видимость ' + str(weather.get_visibility_distance()))
print('Изображение ' + weather.get_weather_icon_name())
print('Ветер ' + str(weather.get_wind()))

translate = ('Moscow')
