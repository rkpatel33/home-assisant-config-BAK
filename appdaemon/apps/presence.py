"""
Music appss
"""
import appdaemon.plugins.hass.hassapi as hass
from constants import CustomEvents, Events, Services, Entities
from utils import UtilsMixin


class LightsOnArriveHome(UtilsMixin, hass.Hass):
    """
    Turn on the lights when I get home
    """
    def initialize(self):
        # register event callback for on/off
        self.listen_state(
            self.turn_on_light,
            Entities.DEVICE__HA_IOSAPP,
            new="state"
        )
        self.listen_state(
            self.turn_on_light,
            Entities.DEVICE__NMAPTRACKER,
            new="state"
        )

    def turn_on_light(self, entity, attribute, old, new, kwargs):
        # let me know which it was
        lights_settings = [
            (Entities.LIGHT__LIVINGROOM_LAMP, 50),
        ]

        if entity == Entities.DEVICE__NMAPTRACKER:
            self.notify('Presence={} based on router'.format(new))
            self.push_bullet('Presence={} based on router'.format(new))
        if entity == Entities.DEVICE__HA_IOSAPP:
            self.notify('Presence={} based on HA iOS App'.format(new))
            self.push_bullet('Presence={} based on HA iOS App'.format(new))

        # turn on after sunset
        if self.sun_down():
            self.set_lights(lights_settings)
            self.turn_on(Entities.SWITCH__PATIO_LIGHTS)


class LightsOnLightsAtSunset(UtilsMixin, hass.Hass):
    """
    Turn on the lights when I get home
    """
    def initialize(self):
        # register event callback for on/off
        self.run_at_sunset(self.turn_on_light, offset=0)

    def turn_on_light(self, entity, attribute, old, new, kwargs):
        # let me know which it was
        lights_settings = [
            (Entities.LIGHT__LIVINGROOM_LAMP, 50),
        ]
        self.set_lights(lights_settings)
        self.turn_on(Entities.SWITCH__PATIO_LIGHTS)

# EOF
