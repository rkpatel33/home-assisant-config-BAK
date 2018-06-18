

# HTTP calls to trigger events

http://192.168.1.10:8123/api/events/minimote_button_1

http://hassio.local:8123/api/events/minimote_button_1
http://192.168.7.34:8123/api/events/minimote_button_1

curl -X POST http://hassio.local:8123/api/events/minimote_button_1
curl -d '{"topic":"xyz topic"}' -X POST http://hassio.local:8123/api/events/minimote_button_1



ssh root@hassio.local "tail -f /config/home-assistant.log" | lnav



local http = require "socket.http"

http.timeout = 5
local  body, code, headers, status = http.request {
  method = "POST",
  url = "http://hassio.local:8123/api/events/minimote_button_1",
  headers = { ["x-ha-access"] = "YOURPASSWORD" }
}