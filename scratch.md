1
# Down stairs
light.living_room_lamp
light.living_room_ceiling_lights
light.kitchen_lights
light.back_room
light.stairway_downstairs

# Upstairs
light.bedroom_lamp_left
light.bedroom_lamp_right
light.stairway_upstairs
switch.fan

# Outside
switch.patio_lights
light.patio_lights
light.outdoor_flood_lights

# Scripts
script.bedtime_lights
script.evening_lights
script.lights_off
script.morning_lights
script.morning_script
script.reload_automations
script.reload_core_config
script.restart_ha
script.trigger_mqtt


# CEC / Apple TV devices / TV

remote.rishis_apple_tv_4g

```json
service: hdmi_cec.power_on
service: hdmi_cec.standby
{"device": "switch.hdmi_0"}


Service: remote.send_command
entity: remote.rishis_apple_tv_4g
{
  "entity_id": "remote.rishis_apple_tv_4g",
  "command": "menu"
}
```


