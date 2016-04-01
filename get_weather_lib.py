# -*- coding: utf-8 -*-
import json
import ConfigParser
import urllib2

sample_data = u'''{
	"coord": {
		"lon": 34.98,
		"lat": 48.45
	},
	"weather": [{
		"id": 701,
		"main": "Mist",
		"description": "туман",
		"icon": "50d"
	}],
	"base": "cmc stations",
	"main": {
		"temp": 7,
		"pressure": 1015,
		"humidity": 100,
		"temp_min": 7,
		"temp_max": 7
	},
	"wind": {
		"speed": 5,
		"deg": 220
	},
	"clouds": {
		"all": 90
	},
	"dt": 1459488600,
	"sys": {
		"type": 1,
		"id": 7351,
		"message": 0.0027,
		"country": "UA",
		"sunrise": 1459480627,
		"sunset": 1459527078
	},
	"id": 709930,
	"name": "Dnipropetrovsk",
	"cod": 200
}'''


class cur_weather:
    def get_weather(self):
        conf = ConfigParser.RawConfigParser()
        conf.read('conf.cfg')
        city = conf.get('general', 'city').strip()
        secret_key = conf.get('general', 'secret_key').strip()
        lang = conf.get('general', 'lang').strip()
        units = conf.get('general', 'units').strip()

        c_url = r'http://api.openweathermap.org/data/2.5/weather?' + 'id=' + city + '&' + \
                'APPID=' + secret_key + '&' + \
                'lang=' + lang  + '&' + \
                'units=' + units

        response = urllib2.urlopen(c_url)

        self.raw_weather = json.loads(response.read(), encoding='utf-8')

    def get_temp(self):
        return float(self.raw_weather['main']['temp'])

    def get_hum(self):
        return float(self.raw_weather['main']['humidity'])

    def get_pres(self):
        return float(self.raw_weather['main']['pressure'])

    def get_weather_text(self):
        return self.raw_weather['weather'][0]['main'], self.raw_weather['weather'][0]['description']

    def get_wind_text(self):
        return str(self.raw_weather['wind']['speed']), str(self.raw_weather['wind']['deg'])

    def get_clouds(self):
        return str(self.raw_weather['clouds']['all'])

    def get_timestamp(self):
        return self.raw_weather['dt']