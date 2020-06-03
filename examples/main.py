from xCore import xCore
from xSW01 import xSW01

SW01 = xSW01()

while True:
    print(SW01.values())
    xCore.sleep(1000)