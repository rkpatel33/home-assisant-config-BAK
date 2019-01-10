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
