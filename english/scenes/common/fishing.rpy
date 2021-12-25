# game/scenes/common/fishing.rpy:164
translate english scene_fishing_home_done_b67b8cdb:

    # lee_think "{e=fish}{rt}[_return]{/rt}{e=arrow_right}{e=inventory}"
    if _return > 1:
        lee_think "Managed to catch [_return] fishes"
    else:
        lee_think "Managed to catch [_return] fish"

translate english strings:

    # game/scenes/common/fishing.rpy:112
    old "{e=skip}"
    new "Skip"

translate english strings:

    # game/scenes/common/fishing.rpy:303
    old "{e=skip} ({e=no}{s=gift})"
    new "Skip (No rare stuff)"

