from mmbn.gamedata.navicust_part import BugT


class BN6NaviCustBug(BugT):
    Nothing = ""
    Activation = "Doesn't activate when bugged."
    Buster = (
        "The MegaBuster normal shot has a chance of firing blanks, and a chance of firing a ChargeShot (10x "
        "attack buster shot). This bug does not apply to Beast Out. The ChargeShot effect does not get removed "
        "by BugFix.\n"
        "- L1: 6/16 Blank; 1/16 ChargeShot; 9/16 Normal Shot\n"
        "- L2: 10/16 Blank; 2/16 ChargeShot; 4/16 Normal Shot\n"
        "- L3: 13/16 Blank; 3/16 ChargeShot; 0/16 Normal Shot"
    )
    Custom = (
        "The player's Custom Screen selection is decreased by one slot every turn after a certain number of "
        "turns. It does not drop below 2 available chips. Charge Cross' ability equalizes this negative effect "
        "for 3 turns.\n"
        "- L1: after 3 turns\n"
        "- L2: after 2 turns\n"
        "- L3: after 1 turn"
    )
    Damage = (
        "MegaMan's HP drops steadily in battle. Can start with L1-3. Gains one level after a flinch, knockback, "
        "or pull.\n"
        "- L1: 1 HP every 40 frames (1.5/sec)\n"
        "- L2: 1 HP every 35 frames (1.7/sec)\n"
        "- L3: 1 HP every 30 frames (2/sec)\n"
        "- L4: 1 HP every 25 frames (2.4/sec)\n"
        "- L5: 1 HP every 20 frames (3/sec)\n"
        "- L6: 1 HP every 15 frames (4/sec)\n"
        "- L7: 1 HP every 10 frames (6/sec)"
    )
    Emotion = (
        "Base MegaMan's emotion window rapidly changes between Normal, Full Synchro, Anger, and Tired during "
        "battle. Emotion remains constant during Custom Screen, you cannot Beast Out while Tired. If you Cross "
        "while Tired, the emotion returns back to normal.\n"
        "- Normal: 14/16 Tired, 1/16 Angry, 1/16 Full Synchro\n"
        "- Tired: 14/16 Normal, 1/16 Angry, 1/16 Full Synchro\n"
        "- Angry: 7/16 Normal, 8/16 Tired, 1/16 Full Synchro\n"
        "- Full Synchro: 7/16 Normal, 8/16 Tired, 1/16 Full Synchro"
    )
    Encounter = "Enemies appear more frequently."
    Movement = "When MegaMan moves, he warps to the edge of his field."
    Panel = (
        "MegaMan has a chance of cracking the panel he moves from.\n"
        "- L1: 2/8 chance\n"
        "- L2: 3/8 chance\n"
        "- L3: 4/8 chance"
    )
    Result = "You only receive Zennys as Battle Rewards."
    Status = (
        "At the beginning of the battle, MegaMan is confused, blinded, flashing, or invincible for a set amount "
        "of time. Flashing status disappears if you transform.\n"
        "- 5 colors: 5 seconds\n"
        "- 6 colors: 10 seconds"
    )
