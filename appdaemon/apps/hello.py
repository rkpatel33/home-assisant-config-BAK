import appdaemon.plugins.hass.hassapi as hass
from constants import CustomEvents

class HelloWorld(hass.Hass):
    def initialize(self):
        self.log("Hello from AppDaemon!!!!!!!!!!!!!!!!")

