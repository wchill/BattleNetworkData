from mmbn.gamedata.navicust_part import BugT


class BN3NaviCustBug(BugT):
    Nothing = ""
    Support = "If there is more than one Support program in the NaviCust, or if it is bugged, it will not activate."
    WeakenedBuster = (
        "The normal MegaBuster shot and ChargeShot (not elemental B PowerAttacks) have a chance of "
        "failure\n"
        "- L1: 1/4 chance of blanks\n"
        "- L2: 1/2 chance of blanks\n"
        "- L3: First 15 shots become Guard"
    )
    CustomScreenHPDrop = (
        "HP steadily drops in the custom screen.\n"
        "- L1: 1 HP every 31 frames (1.9/sec)\n"
        "- L2: 1 HP every 16 frames (3.8/sec)\n"
        "- L3: 1 HP every 8 frames (7.5/sec)"
    )
    BattleHPDrop = (
        "HP steadily drops during battle.\n"
        "- L1: 1 HP every 30 frames (2/sec)\n"
        "- L2: 1 HP every 16 frames (3.8/sec)\n"
        "- L3: 1 HP every 8 frames (7.5/sec)"
    )
    RaisedEncounterRate = "Viruses appear more frequently."
    ModifiedShot = (
        "MegaMan's Charge Shot changes.\n"
        "- L1: Spawn RockCube 1sq ahead\n"
        "- L2: Shoot 100dmg water gun 1sq ahead\n"
        "- L3: Shoots flowers (does nothing)"
    )
    PlayerMovement = (
        "MegaMan starts in a certain movement condition and remain that way the entire battle.\n"
        "- L1: always moves up\n"
        "- L2: always moves down\n"
        "- L3: moves randomly (always confused)"
    )
    BattlePanelChange = (
        "When the battle starts, all normal panels on MegaMan's side becomes a certain type panel.\n"
        "- L1: Cracked\n"
        "- L2/L3: Swamp"
    )
    BattleResult = "If possible, only Zennies drop from battles."
    CustomGauge = "The custom gauge automatically has the SlowGauge effect."
    AutoBugCustomChip = "Auto Bug: Reduces the number of chips available in the custom screen by 1."
    AutoBugSwampPanel = "Auto Bug: The panel MegaMan steps off from becomes a Swamp panel."
    AutoBugChipUse = "Auto Bug: All chips selected are used immediately. Zeta PAs are constantly used."
    AutoBugHalfHP = "Auto Bug: MegaMan's HP is halved."
