import functools
from abc import abstractmethod
from enum import Enum
from typing import Any, Dict, List


class Sort(Enum):
    ID = 0
    ABCDE = 1
    Code = 2
    Attack = 3
    Element = 4
    No = 5
    MB = 6


@functools.total_ordering
class Code(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8
    I = 9
    J = 10
    K = 11
    L = 12
    M = 13
    N = 14
    O = 15
    P = 16
    Q = 17
    R = 18
    S = 19
    T = 20
    U = 21
    V = 22
    W = 23
    X = 24
    Y = 25
    Z = 26
    Star = 27

    def __le__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return self.value

    def __str__(self):
        if self == Code.Star:
            return "*"
        return self.name


@functools.total_ordering
class Chip:
    STANDARD = 1
    MEGA = 2
    GIGA = 3
    NOTHING = 4

    def __init__(
        self,
        game: int,
        name: str,
        chip_id: str,
        code: Code,
        atk: int,
        element: Enum,
        mb: int,
        chip_type: int,
        description: str,
    ):
        self.game = game
        self.name = name
        self.chip_id = chip_id
        self.code = code
        self.atk = atk
        self.element = element
        self.mb = mb
        self.chip_type = chip_type
        self.description = description

    @property
    def sorting_chip_id(self) -> str:
        # Ugly hack to get proper sorting
        return self.chip_id

    @property
    def chip_image_path(self) -> str:
        raise NotImplementedError

    def get_chip_id(self) -> str:
        return self.chip_id.split(" ")[-1]

    def __lt__(self, other: "Chip") -> bool:
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        return self.__dict__ == other.__dict__

    @classmethod
    @abstractmethod
    def make(cls, chip_dict: Dict[str, Any], chip_type: int) -> List["Chip"]:
        raise NotImplementedError

    def __hash__(self) -> int:
        return hash((self.name, self.chip_id, self.code, self.element.value, self.atk, self.mb, self.chip_type))

    def __repr__(self) -> str:
        if self.chip_type == Chip.NOTHING:
            return "Nothing"
        return f"{self.chip_id} - {self.name} {self.code} ({self.element.name}, {self.atk}, {self.mb}MB)"

    def __str__(self) -> str:
        if self.chip_type == Chip.NOTHING:
            return "Nothing"
        return f"{self.name} {self.code}"

    def __setstate__(self, state):
        self.__dict__ = state

        if "BN3Chip" in self.__class__.__name__:
            self.game = 3
        else:
            self.game = 6
