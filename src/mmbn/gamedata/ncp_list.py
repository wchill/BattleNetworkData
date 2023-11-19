import functools
from typing import Type, Dict, Any, List, Tuple, Optional, Union

from mmbn.gamedata import ncp_list_utils
from mmbn.gamedata.bn3.ncp_bugs import BN3NaviCustBug
from mmbn.gamedata.bn4.ncp_bugs import BN4NaviCustBug
from mmbn.gamedata.bn5.ncp_bugs import BN5NaviCustBug
from mmbn.gamedata.bn6.ncp_bugs import BN6NaviCustBug
from mmbn.gamedata.navicust_part import BugT, NaviCustPart, NaviCustColors

game_classes: Dict[int, Type[BugT]] = {
    3: BN3NaviCustBug,
    4: BN4NaviCustBug,
    5: BN5NaviCustBug,
    6: BN6NaviCustBug
}


class NcpList:
    def __init__(self, game: int):
        self.game = game
        self.bug_cls = game_classes[game]

    def _make_parts(self, ncp_dict: Dict[str, Any], internal_id: int) -> List[NaviCustPart]:
        name = ncp_dict["name"]
        description = ncp_dict["description"]
        compression_code = ncp_dict["compression"]
        bug = self.bug_cls["".join(ncp_dict["bug"].split(" "))]
        layout = ncp_dict["layout"]
        return [
            NaviCustPart(
                name, NaviCustColors[color], description, compression_code, bug, layout, internal_id + offset
            )
            for offset, color in enumerate(ncp_dict["color"])
        ]

    @property
    def _nothing_part(self) -> NaviCustPart:
        return NaviCustPart("Nothing", NaviCustColors.Nothing, "Nothing", "", self.bug_cls["Nothing"], ["     "] * 5, 999)

    @functools.cached_property
    def all_parts(self) -> List[NaviCustPart]:
        return ncp_list_utils.get_navicust_parts(self.game, self._make_parts)

    @functools.cached_property
    def tradable_parts(self) -> List[NaviCustPart]:
        return ncp_list_utils.get_tradable_parts(self.game, self._make_parts)

    @functools.cached_property
    def illegal_parts(self) -> List[NaviCustPart]:
        return ncp_list_utils.get_illegal_parts(self.game, self._make_parts)

    @functools.cached_property
    def parts_index(self) -> Dict[Tuple[str, NaviCustColors], NaviCustPart]:
        return {(ncp.name.lower(), ncp.color): ncp for ncp in self.all_parts}

    @functools.cached_property
    def illegal_parts_index(self) -> Dict[Tuple[str, NaviCustColors], NaviCustPart]:
        return {(ncp.name.lower(), ncp.color): ncp for ncp in self.illegal_parts}

    def get_ncp(self, name: str, color: Union[NaviCustColors, str]) -> Optional[NaviCustPart]:
        return ncp_list_utils.get_ncp(self.parts_index, name, NaviCustColors, color)

    def get_parts_by_color(self, color: Union[NaviCustColors, str]) -> List[NaviCustPart]:
        return ncp_list_utils.get_parts_by_color(self.all_parts, NaviCustColors, color)

    def get_parts_by_name(self, name: str) -> List[NaviCustPart]:
        return ncp_list_utils.get_parts_by_name(self.all_parts, name)
