from .config import CFG


def scale_min(value=CFG.grid.scale):
    return f"min({value}vw, {value}vh)"


def scale_max(value=CFG.grid.scale):
    return f"max({value}vw, {value}vh)"
