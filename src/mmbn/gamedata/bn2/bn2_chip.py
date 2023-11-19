import functools
from typing import Any, Dict, List

from ..chip import Chip, Code, Element


@functools.total_ordering
class BN2Element(Element):
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
class BN2Chip(Chip):
    GAME = 2

    def __init__(
        self,
        name: str,
        chip_id: str,
        code: Code,
        atk: int,
        element: BN2Element,
        mb: int,
        chip_type: int,
        description: str,
    ):
        super().__init__(name, chip_id, code, atk, element, mb, chip_type, description)

    @property
    def chip_image_path(self) -> str:
        raise NotImplementedError

    def get_chip_id(self) -> str:
        return self.chip_id.split(" ")[-1]

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
                    BN2Element[chip_dict["element"]],
                    chip_dict["mb"],
                    chip_type,
                    chip_dict["description"],
                )
            )
        return ret
