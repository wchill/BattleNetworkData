from mmbn.gamedata.navicust_part import BugT


class BN4NaviCustBug(BugT):
    Nothing = ""
    Activation = "Doesn't activate when bugged."
    AutoBugHalfHP = "Auto Bug: MegaMan's HP is halved."
    BattleHP = (
        "MegaMan's HP drops steadily in battle.\n"
        "- L1: 1 HP every 10 frames (6/sec)\n"
        "- L2: 1 HP every 6 frames (10/sec)\n"
        "- L3: 1 HP every 3 frames (20/sec)"
    )
    Buster = (
        "The MegaBuster normal shot has a chance of firing blanks.\n"
        "- L1: 2/8 chance\n"
        "- L2: 4/8 chance\n"
        "- L3: 5/8 chance"
    )
    Color = (
        "MegaMan starts with additional bugs.\n"
        "- 5 colors: Level 1 Player + Custom Bug\n"
        "- 6 colors: Level 2 Player + Custom Bug"
    )
    CustomHP = (
        "MegaMan's HP drops steadily while on the Custom Screen.\n"
        "- L1: 1 HP every 6 frames (10/sec)\n"
        "- L2: 1 HP every 4 frames (15/sec)\n"
        "- L3: 1 HP every 3 frames (20/sec)"
    )
    Encounter = "Enemies appear more frequently."
    Movement = "When MegaMan moves, he warps to the edge of his field."
    Panel = (
        "MegaMan changes panels when he steps off them.\n"
        "- L1: Cracked panel\n"
        "- L2: Hole panel\n"
        "- L3: Swamp panel"
    )
    Player = (
        "MegaMan begins battle with a certain condition.\n"
        "- L1: Confused status for 10 seconds\n"
        "- L2: MegaMan always moves forward\n"
        "- L3: MegaMan always moves back"
    )
    BattleResult = "You only receive Zennys as Battle Rewards."
