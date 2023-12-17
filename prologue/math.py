from .config import CFG


def scale_min(value=CFG.grid.scale):
    return f"min({int(value)}vw, {int(value)}vh)"


def scale_max(value=CFG.grid.scale):
    return f"max({int(value)}vw, {int(value)}vh)"
