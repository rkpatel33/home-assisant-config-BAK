"""
Weather apps
"""
import appdaemon.plugins.hass.hassapi as hass
from constants import CustomEvents, Events, Services, Entities, Keys, Location
from utils import UtilsMixin
from darksky import forecast
import requests
import datetime


class DewPoint(UtilsMixin, hass.Hass):
    def initialize(self):

        mornign = datetime.time(7, 30, 0)
        evening = datetime.time(19, 0, 0)

        self.run_daily(self.report_depoint, mornign)
        self.run_daily(self.report_depoint, evening)

    def report_depoint(self, kwargs):
        weather = forecast(Keys.DARKSKY, Location.latitude, Location.longitude)

        # Twilio forecast
        # url = 'https://api.sunrise-sunset.org/json?lat={lat}&lng={long}&date=tomorrow&formatted=0'.format(
        #     lat=Location.latitude,
        #     long=Location.longitude
        # )
        # r = requests.get(url)
        # data = r.json()
        # first_light = data['results']['civil_twilight_begin']
        # d = datetime.strptime(first_light)
        dew_point = round(weather.daily[0].dewPoint, 1)
        temp_low = round(weather.daily[0].temperatureLow, 1)
        margin = round(temp_low - dew_point, 1)
        self.log(weather.temperature)
        self.log(dew_point)
        self.log(temp_low)

        message = 'Dew Point={dew_point}°, Low={temp_low}°, Margin={margin}°'.format(
            dew_point=dew_point,
            temp_low=temp_low,
            margin=margin,
        )

        self.log(message)
        self.push_bullet(message)




# EOF

