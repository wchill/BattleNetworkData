import functools
from enum import auto
from typing import Any, Dict, List, Optional, Tuple, Union

from .. import ncp_list_utils
from ..navicust_part import BugT, ColorT, NaviCustPart

GAME = 6


class BN6NaviCustPartColor(ColorT):
    White = "⚪"
    Pink = "<:pink:1105722810183196702>"
    Yellow = "🟡"
    Green = "🟢"
    Blue = "🔵"
    Red = "🔴"
    Nothing = auto()


class BN6NaviCustBug(BugT):
    Nothing = ""
    Activation = "Doesn't activate when bugged."
    Buster = "The MegaBuster normal shot has a chance of firing blanks, and a chance of firing a ChargeShot (10x attack buster shot). This bug does not apply to Beast Out. The ChargeShot effect does not get removed by BugFix.\n- L1: 6/16 Blank; 1/16 ChargeShot; 9/16 Normal Shot\n- L2: 10/16 Blank; 2/16 ChargeShot; 4/16 Normal Shot\n- L3: 13/16 Blank; 3/16 ChargeShot; 0/16 Normal Shot"
    Custom = "The player's Custom Screen selection is decreased by one slot every turn after a certain number of turns. It does not drop below 2 available chips. Charge Cross' ability equalizes this negative effect for 3 turns.\n- L1: after 3 turns\n- L2: after 2 turns\n- L3: after 1 turn"
    Damage = "MegaMan's HP drops steadily in battle. Can start with L1-3. Gains one level after a flinch, knockback, or pull.\n- L1: 1HP every 40 frames\n- L2: 1HP every 35 frames\n- L3: 1HP every 30 frames\n- L4: 1HP every 25 frames\n- L5: 1HP every 20 frames\n- L6: 1HP every 15 frames\n- L7: 1 HP every 10 frames"
    Emotion = "Base MegaMan's emotion window rapidly changes between Normal, Full Synchro, Anger, and Tired during battle. Emotion remains constant during Custom Screen, you cannot Beast Out while Tired. If you Cross while Tired, the emotion returns back to normal.\n- Normal: 14/16 Tired, 1/16 Angry, 1/16 Full Synchro\n- Tired: 14/16 Normal, 1/16 Angry, 1/16 Full Synchro\n- Angry: 7/16 Normal, 8/16 Tired, 1/16 Full Synchro\n- Full Synchro: 7/16 Normal, 8/16 Tired, 1/16 Full Synchro"
    Encounter = "Enemies appear more frequently."
    Movement = "When MegaMan moves, he warps to the edge of his field."
    Panel = "MegaMan has a chance of cracking the panel he moves from.\n- L1: 2/8 chance\n- L2: 3/8 chance\n- L3: 4/8 chance"
    Result = "You only receive Zennys as Battle Rewards."
    Status = "At the beginning of the battle, MegaMan is confused, blinded, flashing, or invincible for a set amount of time. Flashing status disappears if you transform.\n- 5 colors: 5 seconds\n- 6 colors: 10 seconds"


def _make_bn6_part(ncp_dict: Dict[str, Any], internal_id: int) -> List[NaviCustPart]:
    name = ncp_dict["name"]
    description = ncp_dict["description"]
    compression_code = ncp_dict["compression"]
    bug = BN6NaviCustBug[ncp_dict["bug"]]
    layout = ncp_dict["layout"]
    return [
        NaviCustPart(
            name, BN6NaviCustPartColor[color], description, compression_code, bug, layout, internal_id + offset
        )
        for offset, color in enumerate(ncp_dict["color"])
    ]


@functools.cache
def _get_navicust_parts() -> List[NaviCustPart]:
    return ncp_list_utils.get_navicust_parts(6, _make_bn6_part)


def _create_ncp_index() -> Dict[Tuple[str, ColorT], NaviCustPart]:
    return ncp_list_utils.create_ncp_index(6, _make_bn6_part)


ALL_PARTS = _get_navicust_parts()
TRADABLE_PARTS = ncp_list_utils.get_tradable_parts(GAME, _make_bn6_part)
ILLEGAL_PARTS = ncp_list_utils.get_illegal_parts(GAME, _make_bn6_part)
NOTHING = NaviCustPart(
    "Nothing", BN6NaviCustPartColor.Nothing, "Nothing", "", BN6NaviCustBug.Nothing, ["     "] * 5, 999
)

PARTS_INDEX = {(ncp.name.lower(), ncp.color): ncp for ncp in ALL_PARTS}
ILLEGAL_PARTS_INDEX = {(ncp.name.lower(), ncp.color): ncp for ncp in ILLEGAL_PARTS}


def get_ncp(name: str, color: Union[BN6NaviCustPartColor, str]) -> Optional[NaviCustPart]:
    return ncp_list_utils.get_ncp(PARTS_INDEX, name, BN6NaviCustPartColor, color)


def get_parts_by_color(color: Union[BN6NaviCustPartColor, str]) -> List[NaviCustPart]:
    return ncp_list_utils.get_parts_by_color(ALL_PARTS, BN6NaviCustPartColor, color)


def get_parts_by_name(name: str) -> List[NaviCustPart]:
    return ncp_list_utils.get_parts_by_name(ALL_PARTS, name)
