from typing import Dict, List, Optional, Tuple, Union, cast

from ..chip import Chip, Code
from ..chip_list_utils import SORT_METHODS, ChipReader
from .bn3_chip import BN3Chip, BN3Element

_BN3_CHIP_READER = ChipReader(3, BN3Chip)

NOTHING = Chip("Nothing", "999", Code.Star, 0, BN3Element.Null, 100, Chip.NOTHING, "")
SENTINEL = Chip("", "", Code.Star, 0, BN3Element.Null, 0, Chip.NOTHING, "")

STANDARD_CHIPS = cast(List[BN3Chip], _BN3_CHIP_READER.get_standard_chips())
MEGA_CHIPS = cast(List[BN3Chip], _BN3_CHIP_READER.get_mega_chips())
GIGA_CHIPS = cast(List[BN3Chip], _BN3_CHIP_READER.get_giga_chips())
ALL_CHIPS = cast(List[BN3Chip], _BN3_CHIP_READER.get_all_chips())
UNTRADABLE_CHIPS = cast(List[BN3Chip], _BN3_CHIP_READER.get_untradable_chips())
TRADABLE_STANDARD_CHIPS = cast(List[BN3Chip], _BN3_CHIP_READER.get_tradable_standard_chips())
TRADABLE_MEGA_CHIPS = cast(List[BN3Chip], _BN3_CHIP_READER.get_tradable_mega_chips())
TRADABLE_CHIPS = cast(List[BN3Chip], _BN3_CHIP_READER.get_tradable_chips())

TRADABLE_CHIP_ORDER = {
    method: _BN3_CHIP_READER.calculate_sort_result(method, NOTHING, SENTINEL) for method in SORT_METHODS
}
TRADABLE_CHIP_INDEX = {(chip.name.lower(), chip.code): chip for chip in TRADABLE_CHIPS}

CHIP_INDEX = {(chip.name.lower(), chip.code): chip for chip in ALL_CHIPS}


def get_tradable_chip(name: str, code: Union[str, Code]) -> Optional[BN3Chip]:
    return get_chip_from_index(name, code, TRADABLE_CHIP_INDEX)


def get_chip(name: str, code: Union[str, Code]) -> Optional[BN3Chip]:
    return get_chip_from_index(name, code, CHIP_INDEX)


def get_chip_from_index(name: str, code: Union[str, Code], index: Dict[Tuple[str, Code], BN3Chip]) -> Optional[BN3Chip]:
    try:
        if isinstance(code, Code):
            chip_code = code
        elif code == "*":
            chip_code = Code.Star
        else:
            chip_code = Code[code.upper()]

        return index.get((name.lower(), chip_code))
    except KeyError:
        return None


def get_chips_by_name(name: str) -> List[BN3Chip]:
    retval = []
    for chip in ALL_CHIPS:
        if chip.name.lower() == name.lower():
            retval.append(chip)
    return retval
