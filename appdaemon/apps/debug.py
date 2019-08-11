import json
from timeit import default_timer as timer

import appdaemon.plugins.hass.hassapi as hass
from pushbullet import Pushbullet
from constants import (
    CustomEvents,
    Entities,
    Keys,
    Services,
)


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

# EOF
