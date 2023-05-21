import functools
import json
import pkgutil
from typing import List, Type, TypeVar

from .chip import Chip, Sort

ChipT = TypeVar("ChipT", bound=Chip)


SORT_METHODS = [Sort.ID, Sort.ABCDE, Sort.Code, Sort.Attack, Sort.Element, Sort.No, Sort.MB]


class ChipReader:
    def __init__(self, game: int, chip_cls: Type[ChipT]):
        self.game = game
        self.chip_cls = chip_cls

    def read_chips_from_file(self, filename: str, chip_type: int) -> List[ChipT]:
        data = pkgutil.get_data(__name__, f"bn{self.game}/data/{filename}").decode("utf-8")
        chips = json.loads(data)
        retval = []
        for chip in chips:
            retval += self.chip_cls.make(chip, chip_type)
        return retval

    @functools.cache
    def get_standard_chips(self) -> List[ChipT]:
        return self.read_chips_from_file("chips.json", Chip.STANDARD)

    @functools.cache
    def get_mega_chips(self) -> List[ChipT]:
        return self.read_chips_from_file("megachips.json", Chip.MEGA)

    @functools.cache
    def get_giga_chips(self) -> List[ChipT]:
        return self.read_chips_from_file("gigachips.json", Chip.GIGA)

    @functools.cache
    def get_all_chips(self) -> List[ChipT]:
        return self.get_standard_chips() + self.get_mega_chips() + self.get_giga_chips()

    @functools.cache
    def get_untradable_standard_chips(self) -> List[ChipT]:
        return self.read_chips_from_file("untradable.json", Chip.STANDARD)

    @functools.cache
    def get_untradable_mega_chips(self) -> List[ChipT]:
        return self.read_chips_from_file("untradable_mega.json", Chip.MEGA)

    @functools.cache
    def get_untradable_chips(self) -> List[ChipT]:
        return self.get_untradable_standard_chips() + self.get_untradable_mega_chips()

    @functools.cache
    def get_tradable_standard_chips(self) -> List[ChipT]:
        return sorted(set(self.get_standard_chips()) - set(self.get_untradable_standard_chips()))

    @functools.cache
    def get_tradable_mega_chips(self) -> List[ChipT]:
        return sorted(set(self.get_mega_chips()) - set(self.get_untradable_mega_chips()))

    @functools.cache
    def get_tradable_chips(self) -> List[ChipT]:
        return self.get_tradable_standard_chips() + self.get_tradable_mega_chips()

    @functools.cache
    def calculate_sort_result(self, sort: Sort, nothing: ChipT, sentinel: ChipT) -> List[ChipT]:
        all_tradable_chips = self.get_tradable_chips()
        if sort == Sort.ID:
            return sorted(all_tradable_chips, key=lambda chip: (chip.chip_type, chip.sorting_chip_id, chip.code)) + [
                nothing
            ]
        elif sort == Sort.ABCDE:
            return sorted(all_tradable_chips, key=lambda chip: (chip.name.lower(), chip.chip_type, chip.code)) + [
                nothing
            ]
        elif sort == Sort.Code:
            return sorted(all_tradable_chips, key=lambda chip: (chip.code, chip.chip_type, chip.sorting_chip_id)) + [
                nothing
            ]
        elif sort == Sort.Attack:
            return sorted(
                all_tradable_chips, key=lambda chip: (-chip.atk, chip.chip_type, chip.sorting_chip_id, chip.code)
            ) + [nothing]
        elif sort == Sort.Element:
            return sorted(
                all_tradable_chips, key=lambda chip: (chip.element, chip.chip_type, chip.sorting_chip_id, chip.code)
            ) + [nothing]
        elif sort == Sort.MB:
            return sorted(
                all_tradable_chips, key=lambda chip: (chip.mb, chip.chip_type, chip.sorting_chip_id, chip.code)
            ) + [nothing]
        elif sort == Sort.No:
            # Sentinel values to make things easier
            return [sentinel] * 9
        else:
            raise RuntimeError("Unsupported sort type")
