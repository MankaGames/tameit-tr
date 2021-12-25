# game/scenes/common/fishing.rpy:164
translate german scene_fishing_home_done_b67b8cdb:

    # lee_think "{e=fish}{rt}[_return]{/rt}{e=arrow_right}{e=inventory}"
    if _return > 1:
        lee_think "Es ist mir gelungen, [_return] Fische zu fangen"
    else:
        lee_think "Es gelang mir, [_return] Fische zu fangen"

translate german strings:

    # game/scenes/common/fishing.rpy:112
    old "{e=skip}"
    new "Überspringen"

translate german strings:

    # game/scenes/common/fishing.rpy:303
    old "{e=skip} ({e=no}{s=gift})"
    new "Überspringen (keine seltenen Sachen)"

