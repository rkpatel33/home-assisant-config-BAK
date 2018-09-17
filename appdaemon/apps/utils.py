"""
Convenience functions.
"""
from constants import Keys
from pushbullet import Pushbullet


class UtilsMixin(object):
    """
    Convenience methods for apps
    """
    def set_lights(self, lights_settings):
        """
        lights_settings: list of tuples of (entity_id, bridghtness_pct)
        """
        for entity_id, brightness_pct in lights_settings:
            self.log(entity_id)
            self.turn_on(entity_id, brightness_pct=brightness_pct)

    def push_bullet(self, title, body=None):
        pb = Pushbullet(Keys.PUSHBULLET)
        pb.push_note(title, body)
