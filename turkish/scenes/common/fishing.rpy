# game/scenes/common/fishing.rpy:164
translate turkish scene_fishing_home_done_b67b8cdb:

    # lee_think "{e=fish}{rt}[_return]{/rt}{e=arrow_right}{e=inventory}"
    if _return > 1:
        lee_think "[_return] tane balık tuttun"
    else:
        lee_think "[_return] tane balık tuttun"

translate turkish strings:

    # game/scenes/common/fishing.rpy:112
    old "{e=skip}"
    new "Geç"

translate turkish strings:

    # game/scenes/common/fishing.rpy:303
    old "{e=skip} ({e=no}{s=gift})"
    new "Geç (ender seyler çıkmayacak)"

