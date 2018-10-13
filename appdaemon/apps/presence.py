"""
Music appss
"""
import appdaemon.plugins.hass.hassapi as hass
from constants import CustomEvents, Events, Services, Entities
from utils import UtilsMixin


class ReportPresence(UtilsMixin, hass.Hass):
    """
    Notifiy on presence change
    """
    def initialize(self):
        # register event callback for on/off
        self.listen_state(
            self.notify_presence_change,
            Entities.DEVICE__HA_IOSAPP,
            attribute="state",
        )

        self.listen_state(
            self.notify_presence_change,
            Entities.DEVICE__NMAPTRACKER,
            attribute="state",
        )

    def notify_presence_change(self, entity, attribute, old, new, kwargs):
        if old != new:
            log_message = 'Device {entity} changed from "{old}"" -> "{new}"'.format(
                entity=entity,
                old=old,
                new=new
            )

        if old != new:
            self.log(log_message)
            self.notify(log_message)


class LightsOnArriveHome(UtilsMixin, hass.Hass):
    """
    Turn on the lights when I get home
    """
    def initialize(self):
        # turn on and off lights
        self.listen_state(
            self.turn_on_light,
            Entities.DEVICE__HA_IOSAPP,
            attribute="state",
        )

        self.listen_state(
            self.turn_on_light,
            Entities.DEVICE__NMAPTRACKER,
            attribute="state"
        )

    def turn_on_light(self, entity, attribute, old, new, kwargs):
        lights_settings = [
            (Entities.LIGHT__LIVINGROOM_LAMP, 50),
        ]

        if old == 'not_home' and new == 'home':
            # turn on after sunset
            if self.sun_down():
                self.log('Turning on lights when you arrive after sunset')
                self.set_lights(lights_settings)
                self.turn_on(Entities.LIGHT__PATIO)


class LightsOnLightsAtSunset(UtilsMixin, hass.Hass):
    """
    Turn on the lights when I get home
    """
    def initialize(self):
        # register event callback for on/off
        self.run_at_sunset(self.turn_on_light, offset=0)

    def turn_on_light(self, kwargs):
        # let me know which it was

        self.log('Turning on lights at sunset')

        lights_settings = [
            (Entities.LIGHT__LIVINGROOM_LAMP, 50),
            (Entities.LIGHT__PATIO, 100),
        ]
        self.set_lights(lights_settings)


# EOF
