[![GitHub Issues](https://img.shields.io/github/issues/xinabox/Python-SW01.svg)](https://github.com/xinabox/Python-SW01/issues)
![GitHub Commit](https://img.shields.io/github/last-commit/xinabox/Python-SW01)
![Maintained](https://img.shields.io/maintenance/yes/2020)
![Build status badge](https://github.com/xinabox/Python-SW01/workflows/Python/badge.svg)
![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)

# Python-SW01

The SW01 xChip is equipped with a weather sensor that is capable of measuring the temperature, humidity and atmospheric pressure. It is based on the BME280 manufactured by Bosch.

The humidity sensor provides an extremely fast responce time for fast context awareness application and high overall accuracy over a wide temperature range.

The pressure sensor is an absolute barometric pressure sensor with extremely high accuracy and resolution.

The integrated temperature sensor has been optimized for lowest noise and highest resolution. Its output is used for temperature compensation of the pressure and humidity sensors and can also be used for estimation of the ambient temperature.

# Usage

## Mu-editor
Download [Mu-editor](https://github.com/xinabox/mu-editor/releases/tag/v1.1.0a2)

### CW01 and CW02
- Use [XinaBoxUploader](https://github.com/xinabox/XinaBoxUploader/releases/latest) and flash MicroPython to the CW01/CW02.
- Download Python packages from the REPL with the following code:
    ```python
    import network
    import upip
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect("ssid", "password")
    upip.install("xinabox-SW01")
    ```

### CC03, CS11 and CW03
- Download the .UF2 file for CC03/CS11/CW03 [CircuitPython](https://circuitpython.org/board/xinabox_cs11/) and flash it to the board.
- TO DO

### MicroBit
- TO DO

## Raspberry Pi

Requires Python 3
```
pip3 install xinabox-SW01
```

# Example
```python
from xCore import xCore
from xSW01 import xSW01

SW01 = xSW01()

while True:
    print(SW01.values())
    xCore.sleep(1000)
```