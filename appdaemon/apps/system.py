"""
System apps
"""
import appdaemon.plugins.hass.hassapi as hass


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
