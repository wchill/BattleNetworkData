import collections
import json
import pkgutil
from typing import (
    Any,
    Callable,
    Dict,
    List,
    MutableMapping,
    Optional,
    Tuple,
    Type,
    Union,
)

from .navicust_part import ColorT, NaviCustPart


def get_navicust_parts(game: int, make_func: Callable[[Dict[str, Any], int], List[NaviCustPart]]) -> List[NaviCustPart]:
    data = pkgutil.get_data(__name__, f"bn{game}/data/navicust.json").decode("utf-8")
    ncp_data = json.loads(data)
    retval = []
    for ncp in ncp_data:
        retval += make_func(ncp, len(retval))
    return retval


def create_ncp_index(
    game: int, make_func: Callable[[Dict[str, Any], int], List[NaviCustPart]]
) -> Dict[Tuple[str, ColorT], NaviCustPart]:
    parts = get_navicust_parts(game, make_func)
    index = {(ncp.name.lower(), ncp.color): ncp for ncp in parts}
    count: MutableMapping[NaviCustPart, int] = collections.defaultdict(int)
    for part in parts:
        count[part] += 1

    for part, part_count in count.items():
        if part_count == 1:
            index[(part.name, None)] = part

    return index


def get_ncp(
    parts_index: Dict[Tuple[str, ColorT], NaviCustPart], name: str, color_cls: Type[ColorT], color: Union[ColorT, str]
) -> Optional[NaviCustPart]:
    try:
        if isinstance(color, color_cls):
            ncp_color = color
        else:
            ncp_color = color_cls[color.lower().capitalize()]

        return parts_index.get((name.lower(), ncp_color))
    except KeyError:
        return None


def get_parts_by_color(
    all_parts: List[NaviCustPart], color_cls: Type[ColorT], color: Union[ColorT, str]
) -> List[NaviCustPart]:
    if isinstance(color, color_cls):
        ncp_color = color
    else:
        ncp_color = color_cls[color.lower().capitalize()]

    retval = []
    for ncp in all_parts:
        if ncp.color == ncp_color:
            retval.append(ncp)
    return retval


def get_parts_by_name(all_parts: List[NaviCustPart], name: str) -> List[NaviCustPart]:
    retval = []
    lower_name = name.lower()
    for ncp in all_parts:
        if ncp.name.lower() == lower_name:
            retval.append(ncp)
    return retval
