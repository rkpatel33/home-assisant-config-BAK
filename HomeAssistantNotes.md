
http://192.168.1.10:8123/api/events/minimote_button_1

http://hassio.local:8123/api/events/minimote_button_1
http://192.168.7.34:8123/api/events/minimote_button_1

curl -X POST http://hassio.local:8123/api/events/minimote_button_1
curl -d '{"topic":"xyz topic"}' -X POST http://hassio.local:8123/api/events/minimote_button_1
