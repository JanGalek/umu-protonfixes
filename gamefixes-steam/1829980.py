"""Game fix for Cafe Stella"""

from protonfixes import util


def main() -> None:
    """Install quartz, wmp11, qasf

    Fixes in-game video playback for the intro and ending.
    """
    util.protontricks('quartz')
    util.protontricks('wmp11')
    util.protontricks('qasf')
