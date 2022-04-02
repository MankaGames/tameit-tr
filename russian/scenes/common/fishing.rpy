# game/scenes/common/fishing.rpy:164
translate russian scene_fishing_home_done_b67b8cdb:

    # lee_think "{e=fish}{rt}[_return]{/rt}{e=arrow_right}{e=inventory}"
    if _return > 1:
        lee_think "Удалось выловить [_return] рыбы"
    else:
        lee_think "Удалось выловить [_return] рыбу"

translate russian strings:

    # game/scenes/common/fishing.rpy:112
    old "{e=skip}"
    new "Пропустить"

translate russian strings:

    # game/scenes/common/fishing.rpy:303
    old "{e=skip} ({e=no}{s=gift})"
    new "Пропустить (не будет редких штук)"

