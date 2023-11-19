import functools
from typing import List, Dict, Any

from mmbn.gamedata.chip import Code, Chip, Element


@functools.total_ordering
class BN5Element(Element):
    Heat = 1
    Aqua = 2
    Elec = 3
    Wood = 4
    Sword = 5
    Wind = 6
    Cursor = 7
    Recover = 8
    Object = 9
    Invis = 10
    Plus = 11
    Break = 12
    Null = 13

    def __le__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


@functools.total_ordering
class BN5Chip(Chip):
    GAME = 5

    def __init__(
        self,
        name: str,
        chip_id: str,
        code: Code,
        atk: int,
        element: BN5Element,
        mb: int,
        chip_type: int,
        description: str,
    ):
        super().__init__(name, chip_id, code, atk, element, mb, chip_type, description)

    @property
    def sorting_chip_id(self) -> str:
        # Ugly hack to get proper sorting
        if self.is_version_exclusive_chip():
            if "TP" in self.chip_id:
                return "022 1 " + self.chip_id
            else:
                return "022 2 " + self.chip_id
        return self.chip_id

    def is_version_exclusive_chip(self) -> bool:
        return self.chip_id.startswith("T")

    @property
    def chip_image_path(self) -> str:
        raise NotImplementedError

    def get_chip_id(self) -> str:
        return self.chip_id.split(" ")[-1]

    @classmethod
    def make(cls, chip_dict: Dict[str, Any], chip_type: int) -> List["BN5Chip"]:
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
                    BN5Element[chip_dict["element"]],
                    chip_dict["mb"],
                    chip_type,
                    chip_dict["description"],
                )
            )
        return ret
