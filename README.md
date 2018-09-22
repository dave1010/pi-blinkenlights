# Pi Blinkenlights

Control a Pi's GPIO pins over the internet.

## How it works

When you hit a special URL on Dweet.io, a Python loop running on the Pi that's polling Dweet.io runs commands. These commands
use the `gpio` utility to turn on and off the GPIO pins on the Pi. For more effect, wire up the GPIO pins to a relay and
control mains power.

## Software setup

0. Install git, WiringPi, https://projects.drogon.net/raspberry-pi/wiringpi/the-gpio-utility/ and Dweepy, https://github.com/paddycarey/dweepy

    sudo apt install wiringpi git
    pip install dweepy

1. Clone this project into /home/pi/lights

    cd /home/pi; git clone https://github.com/dave1010/pi-blinkenlights.git lights

2. Pick a secret ID. Eg from https://www.uuidgenerator.net/ - this will be used on https://dweet.io/ (free and zero setup)

3. Add a cron task (`crontab -e`), changing the DWEETID envirnonment variable to your secret ID

    */5 * * * * killall keepalive.sh >/dev/null 2>/dev/null; DWEETID=my-secret-id /home/pi/lights/keepalive.sh >/tmp/lightsout 2>/tmp/lightserrors

## Hardware setup

Get a 5v relay module like https://www.amazon.co.uk/ELEGOO-Channel-Optocoupler-Arduino-Raspberry/dp/B06XK6HCQC/

Be careful if using mains power.

## Debugging

    /home/pi/lights/run-1.py on # trigger manually
    ps aux | grep listen.py # check it's listening for Dweets
    tail -f /tmp/lights* # check logs

## Remote control

See what's just been sent with https://dweet.io/get/latest/dweet/for/my-secret-id

Open https://dweet.io/dweet/for/my-secret-id?1=on in a browser (or hit with curl). Change "1=on" as required.

Sending "foo=bar" will run `run-foo.py` with the argument `bar`. Only alphanumeric keys and values are allowed.

Create more executable commands matching `run-*.py`.

### IFTTT

1. Sign up to https://ifttt.com/
2. Create a new applet https://ifttt.com/create (eg Alexa, Google Assistant), set the "that" to make a "webhook" request to https://dweet.io/dweet/for/my-secret-id?1=on (Google Assistant allows using a numerical "ingredient" in the URL but Alexa doesn't)

## Security

Anyone who can find your secret ID can get your Pi to execute files matching `/home/pi/lights/run-*.py`!

