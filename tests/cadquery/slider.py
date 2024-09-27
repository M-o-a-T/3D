from __future__ import annotations

import sys

import math

if "/src/moat" not in sys.path:
    sys.path.insert(0, "/src/moat")
    from moat._dev_fix import _fix

    _fix()

sq = math.sqrt(2)
from moat.cad import Slider

r = Slider(15, 10)