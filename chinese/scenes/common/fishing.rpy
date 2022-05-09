# game/scenes/common/fishing.rpy:164
translate chinese scene_fishing_home_done_b67b8cdb:

    # lee_think "{e=fish}{rt}[_return]{/rt}{e=arrow_right}{e=inventory}"
    if _return > 1:
        lee_think "钓到  [_return] 条鱼"
    else:
        lee_think "钓到  [_return] 条鱼"

translate chinese strings:

    # game/scenes/common/fishing.rpy:112
    old "{e=skip}"
    new "跳过"

translate chinese strings:

    # game/scenes/common/fishing.rpy:303
    old "{e=skip} ({e=no}{s=gift})"
    new "跳过（没有稀有物品）"

