from .config import CFG


def scale_min(value=CFG.grid.scale):
    return f"min({int(value)}vw, {int(value)}vh)"


def scale_max(value=CFG.grid.scale):
    return f"max({int(value)}vw, {int(value)}vh)"


def calc_direction(start, end):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    angle = math.atan2(dy, dx)
    angle = math.degrees(angle)
    angle = (angle + 360) % 360

    directions = ["W", "NW", "N", "NE", "E", "SE", "S", "SW"]
    index = round(angle / 45) % 8
    return directions[index]


def calc_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)