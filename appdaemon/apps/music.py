"""
Music appss
"""
import appdaemon.plugins.hass.hassapi as hass
from constants import CustomEvents, Events, Services, Entities
from utils import UtilsMixin
import json


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

        # register event callback for on/off
        self.listen_state(
            self.turn_on_radio,
            Entities.INPUT_BOOLEAN__KPCC,
            new="on"
        )

        self.listen_state(
            self.turn_off_radio,
            Entities.INPUT_BOOLEAN__KPCC,
            new="off"
        )

        self.listen_event(
            self.radio_toggle,
            CustomEvents.TOGGLE_KPCC,
        )

    def radio_toggle(self, event_name, data, kwargs):
        # TODO: Not working yest, need to test what comes through in the TOGGLE
        # event
        state = self.get_state(Entities.MEDIA_PLAYER__BEDROOM)
        if state == 'playing':
            self.turn_off_radio(
                Entities.MEDIA_PLAYER__BEDROOM, None, None, None, None
            )
        if state == 'paused':
            self.turn_on_radio(
                Entities.MEDIA_PLAYER__BEDROOM, None, None, None, None
            )

    def turn_off_radio(self, entity, attribute, old, new, kwargs):
        # pause
        self.log('Turned off KPCC')
        self.call_service(
            Services.MEDIA_PLAYER__MEDIA_PAUSE,
            entity_id=Entities.MEDIA_PLAYER__BEDROOM,
        )

    def turn_on_radio(self, entity, attribute, old, new, kwargs):
        """
        Play music in the morning.
        """
        # self.notify("Test", title="Test")
        self.log('---------------------------------------')
        self.log(entity)
        self.log(attribute)
        self.log('---------------------------------------')

        speaker_settings = [
            (Entities.MEDIA_PLAYER__BEDROOM, 0.35),
            (Entities.MEDIA_PLAYER__BATHROOM, 0.25),
            (Entities.MEDIA_PLAYER__LIVINGROOM, 0.20),
        ]

        # make sure speakers are joined
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



# EOF
