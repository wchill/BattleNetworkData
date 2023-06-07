from mmbn.gamedata.bn3 import bn3_chip_list, bn3_ncp_list


class TestBN3GameData:
    def test_bn3_chip_list(self):
        assert len(bn3_chip_list.ALL_CHIPS) > 0
        assert len(bn3_chip_list.STANDARD_CHIPS) > 0
        assert len(bn3_chip_list.MEGA_CHIPS) > 0
        assert len(bn3_chip_list.GIGA_CHIPS) > 0
        assert len(bn3_chip_list.TRADABLE_CHIPS) > 0
        assert len(bn3_chip_list.TRADABLE_STANDARD_CHIPS) > 0
        assert len(bn3_chip_list.TRADABLE_MEGA_CHIPS) > 0

        assert len(bn3_chip_list.get_chips_by_name("Cannon")) == 6
        assert bn3_chip_list.get_tradable_chip("Cannon", "*") is not None
        assert bn3_chip_list.get_tradable_chip("FolderBak", "*") is None

    def test_bn3_chips(self):
        for chip in bn3_chip_list.ALL_CHIPS:
            assert str(chip)
            assert repr(chip)
            assert chip == chip
            assert not (chip < chip)
            assert not (chip > chip)
            assert hash(chip) != 0

    def test_bn3_ncp_list(self):
        assert len(bn3_ncp_list.get_parts_by_name("SprArmor")) == 1
        assert len(bn3_ncp_list.get_parts_by_color("Red")) > 0
        assert bn3_ncp_list.get_ncp("SprArmor", "Red") is not None
        assert bn3_ncp_list.get_ncp("SprArmor", "Blue") is None

        assert bn3_ncp_list.ILLEGAL_PARTS_INDEX.get("HP+200", "White") is not None
