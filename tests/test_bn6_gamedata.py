from mmbn.gamedata.bn6 import bn6_chip_list, bn6_ncp_list


class TestBN6GameData:
    def test_bn6_chip_list(self):
        assert len(bn6_chip_list.ALL_CHIPS) > 0
        assert len(bn6_chip_list.STANDARD_CHIPS) > 0
        assert len(bn6_chip_list.MEGA_CHIPS) > 0
        assert len(bn6_chip_list.GIGA_CHIPS) > 0
        assert len(bn6_chip_list.TRADABLE_CHIPS) > 0
        assert len(bn6_chip_list.TRADABLE_STANDARD_CHIPS) > 0
        assert len(bn6_chip_list.TRADABLE_MEGA_CHIPS) > 0

        assert len(bn6_chip_list.get_chips_by_name("Cannon")) == 4
        assert bn6_chip_list.get_tradable_chip("Cannon", "*") is not None
        assert bn6_chip_list.get_tradable_chip("FolderBak", "*") is None

    def test_bn6_chips(self):
        for chip in bn6_chip_list.ALL_CHIPS:
            assert str(chip)
            assert repr(chip)
            assert chip == chip
            assert not (chip < chip)
            assert not (chip > chip)
            assert hash(chip) != 0

    def test_bn6_ncp_list(self):
        assert len(bn6_ncp_list.get_parts_by_name("SuprArmr")) == 1
        assert len(bn6_ncp_list.get_parts_by_color("Red")) > 0
        assert bn6_ncp_list.get_ncp("SuprArmr", "Red") is not None
        assert bn6_ncp_list.get_ncp("SuprArmr", "Blue") is None
