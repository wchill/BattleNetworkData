import functools
from typing import Any, Dict, List, Optional, Tuple, Union

from .. import ncp_list_utils
from ..navicust_part import BugT, NaviCustColors, NaviCustPart

GAME = 3


BN3NaviCustPartColor = NaviCustColors


class BN3NaviCustBug(BugT):
    Nothing = ""
    Support = "If there is more than one Support program in the NaviCust, or if it is bugged, it will not activate."
    WeakenedBuster = "The normal MegaBuster shot and ChargeShot (not elemental B PowerAttacks) have a chance of failure\n- L1: 1/4 chance of blanks\n- L2: 1/2 chance of blanks\n- L3: First 15 shots become Guard"
    CustomScreenHPDrop = "HP steadily drops in the custom screen.\n- L1: 1HP every 31 frames\n- L2: 1HP every 16 frames\n- L3: 1HP every 8 frames"
    BattleHPDrop = "HP steadily drops during battle.\n- L1: 1HP every 30 frames\n- L2: 1HP every 16 frames\n- L3: 1HP every 8 frames"
    RaisedEncounterRate = "Viruses appear more frequently."
    ModifiedShot = "MegaMan's Charge Shot changes.\n- L1: Spawn RockCube 1sq ahead\n- L2: Shoot 100dmg water gun 1sq ahead\n- L3: Shoots flowers (does nothing)"
    PlayerMovement = "MegaMan starts in a certain movement condition and remain that way the entire battle.\n- L1: always moves up\n- L2: always moves down\n- L3: moves randomly (always confused)"
    BattlePanelChange = "When the battle starts, all normal panels on MegaMan's side becomes a certain type panel.\n- L1: Cracked\n- L2/L3: Swamp"
    BattleResult = "If possible, only Zennies drop from battles."
    CustomGauge = "The custom gauge automatically has the SlowGauge effect."
    AutoBugCustomChip = "Auto Bug: Reduces the number of chips available in the custom screen by 1."
    AutoBugSwampPanel = "Auto Bug: The panel MegaMan steps off from becomes a Swamp panel."
    AutoBugChipUse = "Auto Bug: All chips selected are used immediately. Zeta PAs are constantly used."
    AutoBugHalfHP = "Auto Bug: MegaMan's HP is halved."


def _make_bn3_part(ncp_dict: Dict[str, Any], internal_id: int) -> List[NaviCustPart]:
    name = ncp_dict["name"]
    description = ncp_dict["description"]
    compression_code = ncp_dict["compression"]
    bug = BN3NaviCustBug["".join(ncp_dict["bug"].split(" "))]
    layout = ncp_dict["layout"]
    return [
        NaviCustPart(
            3, name, BN3NaviCustPartColor[color], description, compression_code, bug, layout, internal_id + offset
        )
        for offset, color in enumerate(ncp_dict["color"])
    ]


@functools.cache
def _get_navicust_parts() -> List[NaviCustPart]:
    return ncp_list_utils.get_navicust_parts(GAME, _make_bn3_part)


def _create_ncp_index() -> Dict[Tuple[str, NaviCustColors], NaviCustPart]:
    return ncp_list_utils.create_ncp_index(GAME, _make_bn3_part)


ALL_PARTS = _get_navicust_parts()
TRADABLE_PARTS = ncp_list_utils.get_tradable_parts(GAME, _make_bn3_part)
ILLEGAL_PARTS = ncp_list_utils.get_illegal_parts(GAME, _make_bn3_part)
NOTHING = NaviCustPart(
    3, "Nothing", BN3NaviCustPartColor.Nothing, "Nothing", "", BN3NaviCustBug.Nothing, ["     "] * 5, 999
)

PARTS_INDEX = {(ncp.name.lower(), ncp.color): ncp for ncp in ALL_PARTS}
ILLEGAL_PARTS_INDEX = {(ncp.name.lower(), ncp.color): ncp for ncp in ILLEGAL_PARTS}


def get_ncp(name: str, color: Union[BN3NaviCustPartColor, str]) -> Optional[NaviCustPart]:
    return ncp_list_utils.get_ncp(PARTS_INDEX, name, BN3NaviCustPartColor, color)


def get_parts_by_color(color: Union[BN3NaviCustPartColor, str]) -> List[NaviCustPart]:
    return ncp_list_utils.get_parts_by_color(ALL_PARTS, BN3NaviCustPartColor, color)


def get_parts_by_name(name: str) -> List[NaviCustPart]:
    return ncp_list_utils.get_parts_by_name(ALL_PARTS, name)
