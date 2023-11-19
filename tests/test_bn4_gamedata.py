import pytest

from mmbn.gamedata.chip_list import ChipList
from mmbn.gamedata.ncp_list import NcpList


class TestBN4GameData:

    @pytest.fixture(scope="session")
    def chip_list(self):
        return ChipList(4)

    @pytest.fixture(scope="session")
    def ncp_list(self):
        return NcpList(4)

    def test_bn4_chip_list(self, chip_list):
        assert len(chip_list.all_chips) > 0
        assert len(chip_list.standard_chips) > 0
        assert len(chip_list.mega_chips) > 0
        assert len(chip_list.giga_chips) > 0
        assert len(chip_list.tradable_chips) > 0
        assert len(chip_list.tradable_standard_chips) > 0
        assert len(chip_list.tradable_mega_chips) > 0
        assert len(chip_list.dark_chips) > 0

        assert len(chip_list.get_chips_by_name("Cannon")) == 4
        assert chip_list.get_tradable_chip("Cannon", "*") is not None
        assert chip_list.get_tradable_chip("FolderBak", "*") is None

        assert len(set(chip_list.tradable_chips).intersection(chip_list.dark_chips)) == 0

    def test_bn4_chips(self, chip_list):
        for chip in chip_list.all_chips:
            assert str(chip)
            assert repr(chip)
            assert chip == chip
            assert not (chip < chip)
            assert not (chip > chip)
            assert hash(chip) != 0

    def test_bn4_ncp_list(self, ncp_list):
        assert len(ncp_list.get_parts_by_name("SprArmr")) == 1
        assert len(ncp_list.get_parts_by_color("Red")) > 0
        assert ncp_list.get_part("SprArmr", "Red") is not None
        assert ncp_list.get_part("SprArmr", "Blue") is None
