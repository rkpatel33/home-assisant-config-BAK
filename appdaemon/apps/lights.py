"""
Lights apps
"""
import appdaemon.plugins.hass.hassapi as hass
from constants import CustomEvents, Entities
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
            (Entities.LIGHT__BEDROOM_LAMP_LEFT, 50),
        ]

        downstairs_lights_settings = [
            (Entities.LIGHT__KITCHEN_LIGHTS, 50),
            (Entities.LIGHT__LIVINGROOM_LAMP, 60),
            (Entities.LIGHT__LIVING_ROOM_CEILING_LIGHTS, 60),
            (Entities.LIGHT__BACK_ROOM, 60),
            # (Entities.LIGHT__STAIRWAY_DOWNSTAIRS, 50),
            # (Entities.LIGHT__STAIRWAY_UPSTAIRS, 50),
        ]
        self.set_lights(downstairs_lights_settings)

        # only turn them on before sunrise
        if self.now() < self.sunrise():
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
            (Entities.LIGHT__LIVINGROOM_LAMP, 50),
            (Entities.LIGHT__LIVING_ROOM_CEILING_LIGHTS, 50),
            (Entities.LIGHT__KITCHEN_LIGHTS, 50),
            (Entities.LIGHT__LIVINGROOM_LAMP, 50),
            (Entities.LIGHT__BACK_ROOM, 50),
            (Entities.LIGHT__STAIRWAY_DOWNSTAIRS, 30),
            (Entities.LIGHT__STAIRWAY_UPSTAIRS, 30),
            (Entities.LIGHT__BEDROOM_LAMP_LEFT, 50),
            (Entities.LIGHT__BEDROOM_LAMP_RIGHT, 50),
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
            (Entities.LIGHT__LIVINGROOM_LAMP, 35),
            (Entities.LIGHT__LIVING_ROOM_CEILING_LIGHTS, 35),
            (Entities.LIGHT__KITCHEN_LIGHTS, 35),
            (Entities.LIGHT__LIVINGROOM_LAMP, 35),
            (Entities.LIGHT__BACK_ROOM, 35),
            (Entities.LIGHT__STAIRWAY_DOWNSTAIRS, 30),
            (Entities.LIGHT__STAIRWAY_UPSTAIRS, 30),
            (Entities.LIGHT__BEDROOM_LAMP_LEFT, 35),
            (Entities.LIGHT__BEDROOM_LAMP_RIGHT, 35),
        ]

        self.set_lights(lights_settings)
        self.notify("Turned on bedtime lights", title="Lights")
