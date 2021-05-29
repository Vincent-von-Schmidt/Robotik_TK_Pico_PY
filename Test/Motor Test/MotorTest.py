import machine
import utime
from motor import *

OnFwd(MOT_A, 100)
utime.sleep(1)
Off(MOT_A)

OnRev(MOT_B, 100)
utime.sleep(1)
Off(MOT_B)