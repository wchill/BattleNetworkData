import functools
import os
from pathlib import Path
from typing import Any, Dict, List

from ..chip import Chip, Code, Element


@functools.total_ordering
class BN6Element(Element):
    Heat = 1
    Aqua = 2
    Elec = 3
    Wood = 4
    Sword = 5
    Wind = 6
    Cursor = 7
    Object = 8
    Plus = 9
    Break = 10
    Null = 11

    def __le__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


@functools.total_ordering
class BN6Chip(Chip):
    GAME = 6

    def __init__(
        self,
        name: str,
        chip_id: str,
        code: Code,
        atk: int,
        element: BN6Element,
        mb: int,
        chip_type: int,
        description: str,
    ):
        super().__init__(name, chip_id, code, atk, element, mb, chip_type, description)

    @property
    def sorting_chip_id(self) -> str:
        # Ugly hack to get proper sorting
        return "007 " + self.chip_id if self.is_version_exclusive_chip() else self.chip_id

    @property
    def chip_image_path(self) -> str:
        # TODO: ew

        base_path = Path(os.path.join(os.path.dirname(__file__), "chip_images"))
        if self.chip_type == Chip.STANDARD:
            filename = f"BN6Chip{self.chip_id}.png"
        elif self.chip_type == Chip.MEGA:
            if self.is_version_exclusive_chip():
                filename = f"BN6{self.chip_id[1]}MChip{self.get_chip_id()}.png"
            else:
                filename = f"BN6MChip{self.get_chip_id()}.png"
        elif self.chip_type == Chip.GIGA:
            filename = f"BN6{self.chip_id[1]}GChip{self.get_chip_id()}.png"
        else:
            raise RuntimeError(f"Bad chip type {self.chip_type}")

        return str(base_path / filename)

    def is_version_exclusive_chip(self) -> bool:
        return self.chip_id.startswith("C")

    def get_chip_id(self) -> str:
        return self.chip_id.split(" ")[-1]

    @classmethod
    def make(cls, chip_dict: Dict[str, Any], chip_type: int) -> List["BN6Chip"]:
        ret = []
        for code in chip_dict["codes"]:
            if code == "*":
                code = "Star"
            ret.append(
                cls(
                    chip_dict["name"],
                    chip_dict["id"],
                    Code[code],
                    chip_dict["atk"],
                    BN6Element[chip_dict["element"]],
                    chip_dict["mb"],
                    chip_type,
                    chip_dict["description"],
                )
            )
        return ret
