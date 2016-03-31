import json

sample_data = r'{"coord":{"lon":34.98,"lat":48.45},"weather":[{"id":741,"main":"Fog","description":"fog","icon":"50d"}],"base":"cmc stations","main":{"temp":275.15,"pressure":1020,"humidity":100,"temp_min":275.15,"temp_max":275.15},"wind":{"speed":3,"deg":150},"clouds":{"all":8},"dt":1459402200,"sys":{"type":1,"id":7351,"message":0.0068,"country":"UA","sunrise":1459394350,"sunset":1459440591},"id":709930,"name":"Dnipropetrovsk","cod":200}'


class cur_weather:
    def get_weather(self):
        self.raw_weather = json.loads(sample_data)

    def get_temp(self):
        return float(self.raw_weather['main']['temp']) - 273.15

    def get_hum(self):
        return float(self.raw_weather['main']['humidity'])

    def get_pres(self):
        return float(self.raw_weather['main']['pressure'])

    def get_weather_text(self):
        return str(self.raw_weather['weather'][0]['main']), str(self.raw_weather['weather'][0]['description'])

    def get_wind_text(self):
        return str(self.raw_weather['wind']['speed']), str(self.raw_weather['wind']['deg'])

    def get_clouds(self):
        return str(self.raw_weather['clouds']['all'])