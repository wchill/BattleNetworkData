from mmbn.gamedata.navicust_part import BugT


class BN5NaviCustBug(BugT):
    Nothing = ""
    Activation = "Doesn't activate when bugged."
    Buster = (
        "The MegaBuster normal shot has a 4/16 chance of firing blanks, and a 2/16 chance of firing a "
        "ChargeShot (10x attack buster shot) instead of the normal shot. The ChargeShot effect does not get "
        "removed by BugFix."
    )
    Color = (
        "At the beginning of the battle, MegaMan is confused, blinded, flashing, or invincible for a set amount "
        "of time.\n"
        "- 5 colors: 5 seconds\n"
        "- 6 colors: 10 seconds"
    )
    Custom = (
        "Every time the Custom Window opens, MegaMan loses HP.\n"
        "- L1: Lose 20 HP each time\n"
        "- L2: Lose 40 HP each time\n"
        "- L3: Lose 80 HP each time"
    )
    DamageHP = (
        "MegaMan's HP drops steadily in battle. Start with no HP drain. Gains one level after a flinch, "
        "knockback, or pull.\n"
        "- L1: 1 HP every 40 frames (1.5/sec)\n"
        "- L2: 1 HP every 35 frames (1.7/sec)\n"
        "- L3: 1 HP every 30 frames (2/sec)\n"
        "- L4: 1 HP every 25 frames (2.4/sec)\n"
        "- L5: 1 HP every 20 frames (3/sec)\n"
        "- L6: 1 HP every 15 frames (4/sec)\n"
        "- L7: 1 HP every 10 frames (6/sec)"
    )
    Emotion = (
        "Base MegaMan's emotion window rapidly changes between Normal, Full Synchro, Anger, and Worried during "
        "battle. Emotion remains constant during Custom Screen. Evil emotion is unaffected.\n"
        "- Normal: 7/9 Worried, 1/9 Angry, 1/9 Full Synchro\n"
        "- Worried: 7/9 Normal, 1/9 Angry, 1/9 Full Synchro\n"
        "- Angry: 7/15 Normal, 7/15 Worried, 1/15 Angry\n"
        "- Full Synchro: 7/15 Normal, 7/15 Worried, 1/15 Full Synchro"
    )
    Encounter = "Enemies appear more frequently."
    Movement = "When MegaMan moves, he warps to the edge of his field."
    Panel = (
        "MegaMan has a chance of cracking the panel he moves from.\n"
        "- L1: 25% chance\n"
        "- L2: 50% chance\n"
        "- L3: 100% chance"
    )
    Result = "You only receive Zennys as Battle Rewards."
