import functools
import io
from enum import Enum
from typing import List, Literal

from PIL import Image, ImageDraw


class NaviCustColors(Enum):
    White = "⚪"
    Pink = "<:pink:1105722810183196702>"
    Yellow = "🟡"
    Green = "🟢"
    Blue = "🔵"
    Red = "🔴"
    Orange = "🟠"
    Purple = "🟣"
    Dark = "⚫"
    Nothing = ""


class BugT(Enum):
    pass


COLORS = {
    "White": (245, 245, 245),
    "Yellow": (255, 235, 59),
    "Green": (100, 221, 23),
    "Blue": (21, 101, 192),
    "Red": (213, 0, 0),
    "Pink": (213, 0, 249),
    "Orange": (255, 153, 51),
    "Purple": (204, 51, 255),
    "Dark": (77, 77, 77),
}


ColorLiteral = Literal["White", "Yellow", "Green", "Blue", "Red", "Pink", "Orange", "Purple", "Dark"]


@functools.total_ordering
class NaviCustPart:
    def __init__(
        self,
        game: int,
        name: str,
        color: NaviCustColors,
        description: str,
        compression_code: str,
        bug: BugT,
        layout: List[str],
        internal_id: int,
    ):
        self.game = game
        self.name = name
        self.color = color
        self.description = description
        self.compression_code = compression_code
        self.bug = bug
        self.layout = layout
        self.internal_id = internal_id

    @functools.cached_property
    def block_image(self) -> bytes:
        line_thickness = 2
        block_size = 20
        dimension = 5 * block_size + 6 * line_thickness

        im = Image.new(mode="RGB", size=(dimension, dimension), color=(0x4A, 0x6B, 0x8C))
        draw = ImageDraw.Draw(im)

        color = COLORS[self.color.name]
        darker = (int(color[0] * 0.6), int(color[1] * 0.6), int(color[2] * 0.6))

        for y, line in enumerate(self.layout):
            for x, sq in enumerate(line):
                left = line_thickness + (block_size + line_thickness) * x - 1
                right = left + block_size + 2
                top = line_thickness + (block_size + line_thickness) * y - 1
                bottom = top + block_size + 2
                if sq == " ":
                    continue
                elif sq == "X":
                    draw.rectangle((left, top, right, bottom), color, outline=(0, 0, 0), width=1)
                elif sq == "#":
                    midpoint_x = (left + right) / 2
                    midpoint_y = (top + bottom) / 2
                    draw.rectangle((left, top, right, bottom), color, outline=(0, 0, 0), width=1)
                    draw.line((midpoint_x, top, midpoint_x, bottom), fill=darker, width=2)
                    draw.line((left, midpoint_y, right, midpoint_y), fill=darker, width=2)
                    draw.rectangle((left, top, right, bottom), None, outline=(0, 0, 0), width=1)
                elif sq == "-":
                    draw.rectangle((left, top, right, bottom), darker, outline=(0, 0, 0), width=1)

        with io.BytesIO() as output:
            im.save(output, format="PNG")
            return output.getvalue()

    def __le__(self, other: "NaviCustPart") -> bool:
        return self.internal_id < other.internal_id

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        return self.internal_id == other.internal_id

    def __hash__(self) -> int:
        return hash((self.name, self.color, self.internal_id))

    def __repr__(self) -> str:
        if self.name == "Nothing":
            return "Nothing"
        return f"{self.name} ({self.color.name})"

    def __setstate__(self, state):
        if "BN3NaviCustPartColor" in self.color.__class__.__name__:
            self.game = 3
        else:
            self.game = 6
