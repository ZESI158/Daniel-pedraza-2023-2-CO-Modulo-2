from dino_runner.components.power_ups.power_up  import PowerUP
from dino_runner.utils.constants import SHIELD , SHIELD_TYPE, HAMMER


class Shield(PowerUP):
    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE)

