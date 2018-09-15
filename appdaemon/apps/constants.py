"""
Constants
"""


class CustomEvents:
    TEST_APP = 'APP_TEST'
    MORNING_LIGHTS = 'MORNING_LIGHTS'
    EVENING_LIGHTS = 'EVENING_LIGHTS'
    BEDTIME_LIGHTS = 'BEDTIME_LIGHTS'


class Entities:
    # Living room
    LIGHT__LIVINGROOM_LAMP = 'light.livingroom_lamp'
    LIGHT__LIVING_ROOM_CEILING_LIGHTS = 'light.living_room_ceiling_lights'
    LIGHT__KITCHEN_LIGHTS = 'light.kitchen_lights'
    LIGHT__BACK_ROOM = 'light.back_room'
    # Bedroom
    LIGHT__BEDROOM_LAMP_LEFT = 'light.bedroom_lamp_left'
    LIGHT__BEDROOM_LAMP_RIGHT = 'light.bedroom_lamp_right'
    SWITCH__FAN = 'switch.fan'
    # Stairway
    LIGHT__STAIRWAY_DOWNSTAIRS = 'light.stairway_downstairs'
    LIGHT__STAIRWAY_UPSTAIRS = 'light.stairway_upstairs'
    # Outside
    SWITCH__PATIO_LIGHTS = 'switch.patio_lights'
    LIGHT__OUTDOOR_FLOOD_LIGHTS = 'light.outdoor_flood_lights'
