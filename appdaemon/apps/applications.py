"""
All AppDaemon apps
"""
import datetime
import json
import requests
from timeit import default_timer as timer

import appdaemon.plugins.hass.hassapi as hass

from darksky import forecast
from pushbullet import Pushbullet


# *****************************************************************************
# MARK: Constants
# *****************************************************************************

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
    TOGGLE_KPCC_DOWNSTAIRS = 'TOGGLE_KPCC_DOWNSTAIRS'
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
    INPUT_BOOLEAN__KPCC_DOWNSTAIRS = 'input_boolean.input_kpcc_downstairs'
    # Deivces
    # DEVICE__NMAPTRACKER = 'device_tracker.d4a33d298b4b'
    DEVICE__NMAPTRACKER = 'device_tracker.rishis_iphone_xs'
    DEVICE__HA_IOSAPP = 'rishis_iphone_xs'
    DEVICE__OWNTRACKS_RISHI = 'device_tracker.rishi_rishi_owntrack'


class Services:
    MEDIA_PLAYER__VOLUME_SET = 'media_player/volume_set'
    MEDIA_PLAYER__SONOS_JOIN = 'sonos/join'
    MEDIA_PLAYER__SONOS_UNJOIN = 'sonos/unjoin'
    MEDIA_PLAYER__SELECT_SOURCE = 'media_player/select_source'
    MEDIA_PLAYER__MEDIA_PLAY = 'media_player/media_play'
    MEDIA_PLAYER__MEDIA_PAUSE = 'media_player/media_pause'


# *****************************************************************************
# MARK: Utils, Convenience functions
# *****************************************************************************

class UtilsMixin(object):
    """
    Convenience methods for apps
    """
    def set_lights(self, lights_settings):
        """
        lights_settings: list of tuples of (entity_id, bridghtness_pct)
        """
        for entity_id, brightness_pct in lights_settings:
            if brightness_pct is None:
                self.turn_off(entity_id)
                'Light {entity_id} off'.format(
                    entity_id=entity_id
                )
            else:
                self.turn_on(entity_id, brightness_pct=brightness_pct)
                self.log(
                    'Light {entity_id} to {brightness_pct}'.format(
                        entity_id=entity_id,
                        brightness_pct=brightness_pct
                    )
                )

    def push_bullet(self, title, body=None):
        pb = Pushbullet(Keys.PUSHBULLET)
        pb.push_note(title, body)


# *****************************************************************************
# MARK: Debug
# *****************************************************************************

class Debug(hass.Hass):
    """
    Debugging app for testing purposes.
    """
    def initialize(self):
        # register callback
        self.listen_event(
            self.handle_test_event,
            event=CustomEvents.TEST_APP
        )

        self.listen_state(
            self.handle_owntracks_event,
            entity=Entities.DEVICE__OWNTRACKS_RISHI
        )

    def handle_owntracks_event(self, event_name, data, kwargs):
        # get single entity state
        entity = Entities.DEVICE__OWNTRACKS_RISHI
        state = self.get_state(entity=entity, attribute='all')
        state = json.dumps(state, indent=4, sort_keys=True)
        self.log(
            'entity={entity} state={state}'.format(state=state, entity=entity)
        )

    def handle_test_event(self, event_name, data, kwargs):
        """
        Receive event and print log.
        """
        pb = Pushbullet(Keys.PUSHBULLET)

        self.log('Triggered event={event_name}'.format(event_name=event_name))
        # self.log('------------------------------------------------')
        # self.log(event_name)
        # self.log(data)
        # self.log(kwargs)
        # self.log('------------------------------------------------')

        # notifications
        # self.log('Success!')
        # self.notify('Success!')
        # pb.push_note('Success!', None)

        start = timer()

        # get single entity state
        entity = Entities.DEVICE__OWNTRACKS_RISHI
        state = self.get_state(entity=entity, attribute='all')
        state = json.dumps(state, indent=4, sort_keys=True)
        self.log(
            'entity={entity} state={state}'.format(state=state, entity=entity)
        )
        # pb.push_note('Success!', None)
        # self.notify(
        #     "Entities.DEVICE__OWNTRACKS_RISHI state={state}",
        #     title="Lights"
        # )


        # entity = Entities.LIGHT__BEDROOM_LAMP_RIGHT
        # state = self.get_state(entity=entity, attribute='all')
        # state = json.dumps(state, indent=4, sort_keys=True)
        # self.log(
        #     'entity={entity} state={state}'.format(state=state, entity=entity)
        # )

        self.turn_on(Entities.LIGHT__KITCHEN_LIGHTS, brightness=1)

        end = timer()
        self.log('time={time}ms'.format(time=(end-start)*1000))


        # entire system state
        # state = self.get_state()
        # self.log(
        #     'entity={entity} state={state}'.format(state=state, entity=None)
        # )

# *****************************************************************************
# MARK: Hello
# *****************************************************************************

class HelloWorld(hass.Hass):
    def initialize(self):
        self.log("Hello from AppDaemon!!!!!!!!!!!!!!!!")

# *****************************************************************************
# MARK: Lights
# *****************************************************************************

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
            (Entities.LIGHT__BEDROOM_LAMP_LEFT, 45),
            (Entities.LIGHT__BEDROOM_LAMP_RIGHT, 45),
        ]

        downstairs_lights_settings = [
            (Entities.LIGHT__KITCHEN_LIGHTS, 100),
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
            (Entities.LIGHT__KITCHEN_LIGHTS, 60),
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
            (Entities.LIGHT__KITCHEN_LIGHTS, 40),
            (Entities.LIGHT__LIVINGROOM_LAMP, 35),
            (Entities.LIGHT__LIVING_ROOM_CEILING_LIGHTS, 25),
            (Entities.LIGHT__BACK_ROOM, 25),
            (Entities.LIGHT__STAIRWAY_DOWNSTAIRS, 30),
            (Entities.LIGHT__STAIRWAY_UPSTAIRS, 30),
            (Entities.LIGHT__BEDROOM_LAMP_LEFT, 20),
            (Entities.LIGHT__BEDROOM_LAMP_RIGHT, 20),
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

        # based on time
        # time_on = datetime.time(20, 0, 0)
        # time_off = datetime.time(7, 0, 0)
        # self.run_daily(self.turn_floodlights_on, time_on)
        # self.run_daily(self.turn_floodlights_off, time_off)

        # based on sunset/sunrise
        self.run_at_sunset(self.turn_floodlights_on, offset=0)
        self.run_at_sunrise(self.turn_floodlights_off, offset=0)

    def turn_floodlights_on(self, kwargs):
        self.turn_on(Entities.LIGHT__OUTDOOR_FLOOD_LIGHTS)
        # self.push_bullet(title='Turned on flood lights')
        self.notify(title='Turned on flood lights')

    def turn_floodlights_off(self, kwargs):
        self.turn_off(Entities.LIGHT__OUTDOOR_FLOOD_LIGHTS)
        # self.push_bullet(title='Turned off flood lights')
        self.notify(title='Turned off flood lights')


# *****************************************************************************
# MARK: Music
# *****************************************************************************

class MorningRadio(UtilsMixin, hass.Hass):
    """
    KPCC in the morning

    Scenarios:
    1: play/pause from input swtich
    2: sync on startup
    3: play/pause from sonos app (UNFINISHED) - need to listen to events on
    media player and set input accordingly
    """
    def initialize(self):
        # sync up input to sonos state on startup

        self.log('Initializing morning radio')

        playing_state = self.get_state(
            entity=Entities.MEDIA_PLAYER__BEDROOM,
            attribute='state'
        )
        source = self.get_state(
            entity=Entities.MEDIA_PLAYER__BEDROOM,
            attribute='source'
        )
        if playing_state == 'playing' and source == 'KPCC':
            self.turn_on(Entities.INPUT_BOOLEAN__KPCC)
        else:
            self.turn_off(Entities.INPUT_BOOLEAN__KPCC)

        # list for change in input button state
        # register event callback for on/off
        self.listen_state(
            cb=self.turn_on_radio,
            entity=Entities.INPUT_BOOLEAN__KPCC,
            new="on"
        )

        self.listen_state(
            cb=self.turn_off_radio,
            entity=Entities.INPUT_BOOLEAN__KPCC,
            new="off"
        )

        # listend for an explicit event
        self.listen_event(
            cb=self.radio_toggle,
            event=CustomEvents.TOGGLE_KPCC,
        )

        self.listen_event(
            cb=self.turn_on_radio_downstairs,
            event=CustomEvents.TOGGLE_KPCC_DOWNSTAIRS,
        )

        self.listen_event(
            self.radio_toggle,
            CustomEvents.TOGGLE_KPCC,
        )

    def radio_toggle(self, event_name, data, kwargs):
        """
        Read state and toggle betweeen play/paused.
        """
        # event
        state = self.get_state(Entities.MEDIA_PLAYER__BEDROOM)
        self.log('Calling radio toggle')
        self.log(dict(state=state))

        valid_states = ['playing', 'paused']

        if not state in valid_states:
          self.notify('Sonos not in {states}, state={s}'.format(
            states=valid_states, s=state))

        if state == 'playing':
            self.turn_off_radio(
                Entities.MEDIA_PLAYER__BEDROOM, None, None, None, None
            )
        if state == 'paused':
            self.turn_on_radio(
                Entities.MEDIA_PLAYER__BEDROOM, None, None, None, None
            )

    def turn_on_radio(self, entity, attribute, old, new, kwargs):
        """
        Play music in the morning.
        """
        self.log('Turned KPCC ON')

        speaker_settings = [
            (Entities.MEDIA_PLAYER__BEDROOM, 0.35),
            (Entities.MEDIA_PLAYER__BATHROOM, 0.25),
            (Entities.MEDIA_PLAYER__LIVINGROOM, 0.20),
        ]

        # make sure speakers are joined
        self.log('Joining speakers to {speaker}'.format(
            speaker=Entities.MEDIA_PLAYER__BEDROOM
        ))
        self.call_service(
            Services.MEDIA_PLAYER__SONOS_JOIN,
            master=Entities.MEDIA_PLAYER__BEDROOM,
            entity_id=[
                Entities.MEDIA_PLAYER__LIVINGROOM,
                Entities.MEDIA_PLAYER__BATHROOM
            ]
        )

        # set volumes on all speakers
        for entity_id, volume in speaker_settings:
            self.log(
                'Setting volume: {entity_id}={volume}'.format(
                    entity_id=entity_id,
                    volume=volume
                )
            )
            self.call_service(
                Services.MEDIA_PLAYER__VOLUME_SET,
                entity_id=entity_id,
                volume_level=volume
            )

        # set channel
        self.call_service(
            Services.MEDIA_PLAYER__SELECT_SOURCE,
            entity_id=Entities.MEDIA_PLAYER__BEDROOM,
            source='KPCC'
        )

        # play
        self.call_service(
            Services.MEDIA_PLAYER__MEDIA_PLAY,
            entity_id=Entities.MEDIA_PLAYER__BEDROOM,
        )
        self.log('Play KPCC')

    def turn_off_radio(self, entity, attribute, old, new, kwargs):
        # pause
        self.log('Turned KPCC OFF')
        self.call_service(
            Services.MEDIA_PLAYER__MEDIA_PAUSE,
            entity_id=Entities.MEDIA_PLAYER__BEDROOM,
        )

    def turn_on_radio_downstairs(self, event_name, data, kwargs):
        """
        Play music in the morning downstairs.
        """
        speaker_settings = [
            (Entities.MEDIA_PLAYER__LIVINGROOM, 0.10),
        ]

        state = self.get_state(Entities.MEDIA_PLAYER__LIVINGROOM)
        self.log(dict(state=state))

        valid_states = ['playing', 'paused']

        if not state in valid_states:
          self.notify('Sonos not in {states}, state={s}'.format(
            states=valid_states, s=state))

        if state == 'playing':
            self.turn_off_radio(
                Entities.MEDIA_PLAYER__LIVINGROOM, None, None, None, None
            )
        else:
            # make sure living room speaker is unjoined
            self.log('Unjoining speakers to {speaker}'.format(
                speaker=Entities.MEDIA_PLAYER__LIVINGROOM
            ))

            self.call_service(
                service=Services.MEDIA_PLAYER__SONOS_UNJOIN,
                entity_id=Entities.MEDIA_PLAYER__LIVINGROOM,
            )

            # set volumes on all speakers
            for entity_id, volume in speaker_settings:
                self.log(
                    'Setting volume: {entity_id}={volume}'.format(
                        entity_id=entity_id,
                        volume=volume
                    )
                )
                self.call_service(
                    service=Services.MEDIA_PLAYER__VOLUME_SET,
                    entity_id=entity_id,
                    volume_level=volume
                )

        # set channel
        self.call_service(
            service=Services.MEDIA_PLAYER__SELECT_SOURCE,
            entity_id=Entities.MEDIA_PLAYER__LIVINGROOM,
            source='KPCC'
        )

        # play
        self.call_service(
            Services.MEDIA_PLAYER__MEDIA_PLAY,
            entity_id=Entities.MEDIA_PLAYER__LIVINGROOM,
        )
        self.log('Play KPCC downstairs')


# *****************************************************************************
# MARK: Presence
# *****************************************************************************

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

        is_in_blocked_time = self.now_is_between("23:00:00", "05:00:00")

        if old == 'not_home' and new == 'home' and not is_in_blocked_time:
            # turn on after sunset
            if self.sun_down():
                self.log('Turning on lights when you arrive after sunset')
                self.notify(
                    'Turning on lamp and patio lights',
                    title="Lights"
                )
                self.set_lights(lights_settings)
                self.turn_on(Entities.LIGHT__PATIO)


class LightsOnLightsAtSunset(UtilsMixin, hass.Hass):
    """
    Turn on the lights if I am home
    """
    def initialize(self):
        # register event callback for on/off
        self.run_at_sunset(self.turn_on_light, offset=0)

    def turn_on_light(self, kwargs):
        # let me know which it was

        self.log('Turning on lights at sunset')

        presence_state = self.get_state(
            entity=Entities.DEVICE__NMAPTRACKER
        )

        lights_settings = [
            (Entities.LIGHT__LIVINGROOM_LAMP, 50),
            (Entities.LIGHT__PATIO, 100),
        ]

        if presence_state == 'home':
            self.set_lights(lights_settings)


# *****************************************************************************
# MARK: System
# *****************************************************************************

class Restart(hass.Hass):
    """
    Lights controls
    """
    def initialize(self):
        # register event callback
        self.listen_event(
            self.handle_event,
            'appd_started'
        )
        self.listen_event(
            self.handle_event,
            'component_loaded'
        )

    def handle_event(self, event_name, data, kwargs):
        self.notify("Restart complete", title="App Daemon")

        self.log(
            '---------------- Restart complete ----------------'
        )

# *****************************************************************************
# MARK: Weather
# *****************************************************************************

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
