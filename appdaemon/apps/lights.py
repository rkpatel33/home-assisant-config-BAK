"""
Lights apps
"""
import datetime
import appdaemon.plugins.hass.hassapi as hass

from constants import CustomEvents, Entities, Services
from utils import UtilsMixin

class MorningLights(UtilsMixin, hass.Hass):
    """
    Lights controls
    """
    def initialize(self):
        # register event callback
        self.listen_event(
            self.handle_event,
            CustomEvents.MORNING_LIGHTS
        )

    def handle_event(self, event_name, data, kwargs):
        """
        only turn on bedroom lamp if before sunrise
        """
        bedroom_lights_settings = [
            (Entities.LIGHT__BEDROOM_LAMP_LEFT, 60),
        ]

        downstairs_lights_settings = [
            (Entities.LIGHT__KITCHEN_LIGHTS, 40),
            (Entities.LIGHT__LIVINGROOM_LAMP, 60),
            (Entities.LIGHT__LIVING_ROOM_CEILING_LIGHTS, 60),
            (Entities.LIGHT__BACK_ROOM, 60),
            # (Entities.LIGHT__STAIRWAY_DOWNSTAIRS, 50),
            # (Entities.LIGHT__STAIRWAY_UPSTAIRS, 50),
        ]
        self.set_lights(downstairs_lights_settings)

        # only turn them on before sunrise
        if self.datetime() < self.sunrise():
            self.set_lights(bedroom_lights_settings)

        self.notify("Turned on morning lights", title="Lights")


class EveningLights(UtilsMixin, hass.Hass):
    def initialize(self):
        # register event callback
        self.listen_event(
            self.handle_event,
            CustomEvents.EVENING_LIGHTS
        )

    def handle_event(self, event_name, data, kwargs):
        """
        Receive event and print log.
        """
        lights_settings = [
            (Entities.LIGHT__LIVINGROOM_LAMP, 35),
            (Entities.LIGHT__LIVING_ROOM_CEILING_LIGHTS, 35),
            (Entities.LIGHT__KITCHEN_LIGHTS, 15),
            (Entities.LIGHT__BACK_ROOM, 35),
            (Entities.LIGHT__STAIRWAY_DOWNSTAIRS, 30),
            (Entities.LIGHT__STAIRWAY_UPSTAIRS, 30),
            (Entities.LIGHT__BEDROOM_LAMP_LEFT, 50),
            (Entities.LIGHT__BEDROOM_LAMP_RIGHT, 50),
            (Entities.LIGHT__PATIO, 100),
        ]

        self.set_lights(lights_settings)
        self.notify("Turned on evening lights", title="Lights")


class BedtimeLights(UtilsMixin, hass.Hass):
    def initialize(self):
        # register event callback
        self.listen_event(
            self.handle_event,
            CustomEvents.BEDTIME_LIGHTS
        )

    def handle_event(self, event_name, data, kwargs):
        """
        Receive event and print log.
        """
        lights_settings = [
            (Entities.LIGHT__KITCHEN_LIGHTS, 9),
            (Entities.LIGHT__LIVINGROOM_LAMP, 35),
            (Entities.LIGHT__LIVING_ROOM_CEILING_LIGHTS, 25),
            (Entities.LIGHT__BACK_ROOM, 25),
            (Entities.LIGHT__STAIRWAY_DOWNSTAIRS, 30),
            (Entities.LIGHT__STAIRWAY_UPSTAIRS, 30),
            (Entities.LIGHT__BEDROOM_LAMP_LEFT, 35),
            (Entities.LIGHT__BEDROOM_LAMP_RIGHT, 35),
            (Entities.LIGHT__PATIO, 100),
        ]

        self.set_lights(lights_settings)
        self.notify("Turned on bedtime lights", title="Lights")


class EverythingOff(UtilsMixin, hass.Hass):
    def initialize(self):
        # register event callback
        self.listen_event(
            self.handle_event,
            CustomEvents.EVERYTHING_OFF
        )

    def handle_event(self, event_name, data, kwargs):
        """
        Receive event and print log.
        """
        lights_settings = [
            (Entities.LIGHT__KITCHEN_LIGHTS, None),
            (Entities.LIGHT__LIVINGROOM_LAMP, None),
            (Entities.LIGHT__LIVING_ROOM_CEILING_LIGHTS, None),
            (Entities.LIGHT__LIVINGROOM_LAMP, None),
            (Entities.LIGHT__BACK_ROOM, None),
            (Entities.LIGHT__STAIRWAY_DOWNSTAIRS, None),
            (Entities.LIGHT__STAIRWAY_UPSTAIRS, None),
            (Entities.LIGHT__BEDROOM_LAMP_LEFT, None),
            (Entities.LIGHT__BEDROOM_LAMP_RIGHT, None),
            (Entities.LIGHT__PATIO, None),

        ]

        # turn off radio
        self.call_service(
            Services.MEDIA_PLAYER__MEDIA_PAUSE,
            entity_id=Entities.MEDIA_PLAYER__BEDROOM,
        )

        # turn off dimmer lights
        for entity, level in lights_settings:
            self.turn_off(entity)

        # turn off patio light switch
        self.notify("Turned off all lights", title="Lights")


class ZeroLights(UtilsMixin, hass.Hass):
    def initialize(self):
        # register event callback
        self.listen_event(
            self.handle_event,
            CustomEvents.ZERO_LIGHTS
        )

    def handle_event(self, event_name, data, kwargs):
        """
        Receive event and print log.
        """
        lights_settings = [
            (Entities.LIGHT__LIVINGROOM_LAMP, 20),
            (Entities.LIGHT__LIVING_ROOM_CEILING_LIGHTS, None),
            (Entities.LIGHT__KITCHEN_LIGHTS, None),
            (Entities.LIGHT__BACK_ROOM, None),
            (Entities.LIGHT__STAIRWAY_DOWNSTAIRS, None),
            (Entities.LIGHT__STAIRWAY_UPSTAIRS, None),
            (Entities.LIGHT__BEDROOM_LAMP_LEFT, 20),
            (Entities.LIGHT__BEDROOM_LAMP_RIGHT, 20),
            (Entities.LIGHT__PATIO, None),
        ]

        self.set_lights(lights_settings)
        # self.turn_off(Entities.LIGHT__KITCHEN_LIGHTS)
        self.notify("Set lights to zero", title="Lights")


class PatioLightsToggle(UtilsMixin, hass.Hass):
    def initialize(self):
        # register event callback
        self.listen_event(
            self.handle_event,
            CustomEvents.PATIO_LIGHTS_TOGGLE
        )

    def handle_event(self, event_name, data, kwargs):
        """
        Receive event and print log.
        """
        state = self.get_state(Entities.LIGHT__PATIO)
        if state == 'on':
            self.turn_off(Entities.LIGHT__PATIO)
            self.notify("Patio lights off", title="Lights")
        else:
            self.turn_on(Entities.LIGHT__PATIO)
            self.notify("Patio lights on", title="Lights")


class FloodLightsTimer(UtilsMixin, hass.Hass):
    def initialize(self):
        # register event callback based on times
        time_on = datetime.time(20, 0, 0)
        time_off = datetime.time(7, 0, 0)

        self.run_daily(self.turn_floodlights_on, time_on)
        self.run_daily(self.turn_floodlights_off, time_off)

    def turn_floodlights_on(self, kwargs):
        self.turn_on(Entities.LIGHT__OUTDOOR_FLOOD_LIGHTS)
        self.push_bullet(title='Turned on flood lights')

    def turn_floodlights_off(self, kwargs):
        self.turn_off(Entities.LIGHT__OUTDOOR_FLOOD_LIGHTS)
        self.push_bullet(title='Turned off flood lights')


# EOF
