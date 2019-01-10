"""
Constants
"""


class Location:
    latitude = 33.978924
    longitude = -118.465342


class Keys:
    PUSHBULLET = 'o.RLRexz1gbcc9ENsrBcbr4DuEOCmKrBqb'
    DARKSKY = '99b117dd1eeffa3351a0fa4316997671'


class CustomEvents:
    TEST_APP = 'APP_TEST'
    MORNING_LIGHTS = 'MORNING_LIGHTS'
    EVENING_LIGHTS = 'EVENING_LIGHTS'
    BEDTIME_LIGHTS = 'BEDTIME_LIGHTS'
    ZERO_LIGHTS = 'ZERO_LIGHTS'
    EVERYTHING_OFF = 'EVERYTHING_OFF'
    TOGGLE_KPCC = 'TOGGLE_KPCC'
    PATIO_LIGHTS_TOGGLE = 'PATIO_LIGHTS_TOGGLE'


class Events:
    STATE_CHANGED = 'state_changed'


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
    LIGHT__PATIO = 'light.patio_lights'
    LIGHT__OUTDOOR_FLOOD_LIGHTS = 'light.outdoor_flood_lights'
    # Music and media
    MEDIA_PLAYER__LIVINGROOM = 'media_player.livingroom'
    MEDIA_PLAYER__BATHROOM = 'media_player.bathroom'
    MEDIA_PLAYER__BEDROOM = 'media_player.bedroom'
    # Switches
    INPUT_BOOLEAN__TEST = 'input_boolean.test_input'
    INPUT_BOOLEAN__KPCC = 'input_boolean.input_kpcc'
    # Deivces
    # DEVICE__NMAPTRACKER = 'device_tracker.d4a33d298b4b'
    DEVICE__NMAPTRACKER = 'device_tracker.rishis_iphone_xs'
    DEVICE__HA_IOSAPP = 'rishis_iphone_xs'


class Services:
    MEDIA_PLAYER__VOLUME_SET = 'media_player/volume_set'
    MEDIA_PLAYER__SONOS_JOIN = 'media_player/sonos_join'
    MEDIA_PLAYER__SELECT_SOURCE = 'media_player/select_source'
    MEDIA_PLAYER__MEDIA_PLAY = 'media_player/media_play'
    MEDIA_PLAYER__MEDIA_PAUSE = 'media_player/media_pause'
