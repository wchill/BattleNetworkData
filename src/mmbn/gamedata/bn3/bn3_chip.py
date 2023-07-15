import functools
from enum import Enum
from typing import Any, Dict, List

from ..chip import Chip, Code


@functools.total_ordering
class BN3Element(Enum):
    Heat = 1
    Aqua = 2
    Elec = 3
    Wood = 4
    Null = 5

    def __le__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


@functools.total_ordering
class BN3Chip(Chip):
    STANDARD = 1
    MEGA = 2
    GIGA = 3
    NOTHING = 4

    def __init__(
        self,
        name: str,
        chip_id: str,
        code: Code,
        atk: int,
        element: BN3Element,
        mb: int,
        chip_type: int,
        description: str,
    ):
        super().__init__(3, name, chip_id, code, atk, element, mb, chip_type, description)

    @property
    def chip_image_path(self) -> str:
        raise NotImplementedError

    def get_chip_id(self) -> str:
        return self.chip_id.split(" ")[-1]

    def __lt__(self, other: "BN3Chip") -> bool:
        if self.chip_type != other.chip_type:
            return self.chip_type < other.chip_type

        if self.sorting_chip_id == other.sorting_chip_id:
            if self.code == Code.Star and other.code != Code.Star:
                return False
            elif self.code != Code.Star and other.code == Code.Star:
                return True
            else:
                return self.code < other.code

        return self.sorting_chip_id < other.sorting_chip_id

    @classmethod
    def make(cls, chip_dict: Dict[str, Any], chip_type: int) -> List["BN3Chip"]:
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
                    BN3Element[chip_dict["element"]],
                    chip_dict["mb"],
                    chip_type,
                    chip_dict["description"],
                )
            )
        return ret
