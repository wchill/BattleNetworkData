from typing import Type, Tuple, Dict, List, Union, Optional

from mmbn.gamedata.bn1.bn1_chip import BN1Chip, BN1Element
from mmbn.gamedata.bn2.bn2_chip import BN2Chip, BN2Element
from mmbn.gamedata.bn3.bn3_chip import BN3Chip, BN3Element
from mmbn.gamedata.bn4.bn4_chip import BN4Chip, BN4Element
from mmbn.gamedata.bn5.bn5_chip import BN5Chip, BN5Element
from mmbn.gamedata.bn6.bn6_chip import BN6Chip, BN6Element
from mmbn.gamedata.chip import Element, Chip, Sort, Code
from mmbn.gamedata.chip_list_utils import ChipReader, SORT_METHODS

game_classes: Dict[int, Tuple[Type[Chip], Type[Element]]] = {
    1: (BN1Chip, BN1Element),
    2: (BN2Chip, BN2Element),
    3: (BN3Chip, BN3Element),
    4: (BN4Chip, BN4Element),
    5: (BN5Chip, BN5Element),
    6: (BN6Chip, BN6Element)
}


class ChipList:
    def __init__(self, game: int):
        self.game = game
        self.chip_cls, self.element_cls = game_classes[game]
        self.chip_reader = ChipReader(game, self.chip_cls)

    @property
    def standard_chips(self) -> List[Chip]:
        return self.chip_reader.get_standard_chips()

    @property
    def mega_chips(self) -> List[Chip]:
        return self.chip_reader.get_mega_chips()

    @property
    def giga_chips(self) -> List[Chip]:
        return self.chip_reader.get_giga_chips()

    @property
    def dark_chips(self) -> List[Chip]:
        return self.chip_reader.get_dark_chips()

    @property
    def all_chips(self) -> List[Chip]:
        return self.chip_reader.get_all_chips()

    @property
    def untradable_chips(self) -> List[Chip]:
        return self.chip_reader.get_untradable_chips()

    @property
    def tradable_standard_chips(self) -> List[Chip]:
        return self.chip_reader.get_tradable_standard_chips()

    @property
    def tradable_mega_chips(self) -> List[Chip]:
        return self.chip_reader.get_tradable_mega_chips()

    @property
    def tradable_chips(self) -> List[Chip]:
        return self.chip_reader.get_tradable_chips()

    @property
    def illegal_chips(self) -> List[Chip]:
        return self.chip_reader.get_illegal_chips()

    @property
    def tradable_chip_order(self) -> Dict[Sort, List[Chip]]:
        return {
            method: self.chip_reader.calculate_sort_result(method, self._nothing_chip, self._sentinel_chip) for method in SORT_METHODS
        }

    @property
    def tradable_chip_index(self) -> Dict[Tuple[str, Code], Chip]:
        return {(chip.name.lower(), chip.code): chip for chip in self.tradable_chips}

    @property
    def illegal_chip_index(self) -> Dict[Tuple[str, Code], Chip]:
        return {(chip.name.lower(), chip.code): chip for chip in self.illegal_chips}

    @property
    def chip_index(self) -> Dict[Tuple[str, Code], Chip]:
        return {(chip.name.lower(), chip.code): chip for chip in self.all_chips}

    @property
    def _nothing_chip(self) -> Chip:
        return self.chip_cls("Nothing", "999", Code.Star, 0, self.element_cls["Null"], 100, Chip.NOTHING, "")

    @property
    def _sentinel_chip(self) -> Chip:
        return self.chip_cls("", "", Code.Star, 0, self.element_cls["Null"], 0, Chip.NOTHING, "")

    def get_tradable_chip(self, name: str, code: Union[str, Code]) -> Optional[Chip]:
        return self.get_chip_from_index(name, code, self.tradable_chip_index)

    def get_illegal_chip(self, name: str, code: Union[str, Code]) -> Optional[Chip]:
        return self.get_chip_from_index(name, code, self.illegal_chip_index)

    def get_chip(self, name: str, code: Union[str, Code]) -> Optional[Chip]:
        return self.get_chip_from_index(name, code, self.chip_index)

    def get_chip_from_index(self, name: str, code: Union[str, Code], index: Dict[Tuple[str, Code], Chip]) -> Optional[Chip]:
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

    def get_chips_by_name(self, name: str) -> List[Chip]:
        retval = []
        for chip in self.all_chips:
            if chip.name.lower() == name.lower():
                retval.append(chip)
        return retval
