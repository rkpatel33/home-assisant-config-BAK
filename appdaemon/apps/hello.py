import appdaemon.plugins.hass.hassapi as hass
from events import CustomEvents

class HelloWorld(hass.Hass):
    def initialize(self):
        self.log("Hello from AppDaemon!!!!!!!!!!!!!!!!")

class YoWorld(hass.Hass):
    def initialize(self):
        self.log("Heyyyyyyyyy?????????? from AppDaemon")

class Debug(hass.Hass):
    def initialize(self):
        # register callback
        self.listen_event(
            self.handle_test_event,
            CustomEvents.APP_TEST
        )

    def handle_test_event(self, event_name, data, kwargs):
        """
        Receive event and print log.
        """
        self.log('------------------------------------------------')
        self.log(event_name)
        self.log(data)
        self.log(kwargs)
        self.log('------------------------------------------------')

class BedtimeLights(hass.Hass):
    def initialize(self):
        # register callback
        self.listen_event(
            self.set_lights_to_bedtime,
            CustomEvents.BEDTIME_LIGHTS2
        )


    def set_lights_to_bedtime(self, event_name, data, kwargs):
        """
        Receive event and print log.
        """
        self.log('Setting bedtime lights')
        self.call_service("notify/notify", title = "Hello", message = "Hello World")

