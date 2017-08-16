# Controlling ws2812-LED-Strips via internet
Goals: Simple & fast protocol

The server (esp8266) uses adafruits Neopixel-library as well as the ESP8266WiFi and WiFiUdp - libraries and is based on the arduino-core for esp8266. Make sure these are available.
# Preperations:
Change SSID and PSK in server/server.ino to fit your Wifi and modify LEN as well as DO to represent the led-strip.
Flash the esp8266 using the Arduino IDE.

Edit client/larson.py and client/rainbow.py and change IP to the IP-Address of your esp8266 and LEN to the lenght of the strip.
# Usage:
./larson.py [BRIGHTNESS MODE]
BRIGHTNESS must be an Integer between 0 and 254. MODE must be an Integer between 0 and 3: 0<=mode<=2 ->RGB, mode==3: rainbow

./rainbow.py [BRIGHTNESS MODE]
MODE=0 - "Exponential" color-distribution, MODE=1 - "linear"
# Specifications
The server listens for UDP-Packets on port 3000. The ordinal number (latin-1) of each received character is used as the brightness-value for the current led and increments the led-counter (each pixel=3 leds).
\\0 enters the "command-mode" - another \\0 updates the strip and resets the led-counter. "#" takes the next characters and updates the counter to the corresponding number, \0 changes back to interpreting characters as brightness-values.
# ToDo!
- Implement a "buffer" to store commands and allow for a precise timing between color-changes
- Allow the programming of presets and storage of animations via udp/serial
