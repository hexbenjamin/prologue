import math
import reflex as rx

from rich import inspect


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


class PrologueState(rx.State):
    """The app state."""

    pos_x: int = 0
    pos_y: int = 0
    cols: int = 6
    rows: int = 3

    def initialize(self):
        self.pos_x = 0
        self.pos_y = 0

    @rx.var
    def translation(self) -> str:
        return f"translate({self.pos_x * 100}vw, {self.pos_y * 100}vh)"

    def left(self):
        if self.pos_x != 0:
            self.pos_x += 1

    def right(self):
        if self.pos_x != self.cols - 1:
            self.pos_x -= 1

    def up(self):
        if self.pos_y != 0:
            self.pos_y += 1

    def down(self):
        if self.pos_y != self.rows - 1:
            self.pos_y -= 1


class SwipeState(PrologueState):
    swipe_start: tuple[int, int] = (-1, -1)
    swipe_end: tuple[int, int] = (-1, -1)

    mouse_x: int = 0
    mouse_y: int = 0

    def reset_swipe(self):
        self.swipe_start = (-1, -1)
        self.swipe_end = (-1, -1)

    def get_start(self):
        return [
            rx.call_script(
                "[mousePosition.x, mousePosition.y]",
                callback=SwipeState.update_start,
            )
        ]

    def update_start(self, coords):
        self.set_swipe_start(coords)
        # print("start!", self.swipe_start)

    def get_end(self):
        return [
            rx.call_script(
                "[mousePosition.x, mousePosition.y]",
                callback=SwipeState.update_end,
            )
        ]

    def update_end(self, coords):
        self.set_swipe_end(coords)
        # print("end!", self.swipe_end)
        # print("direction:", calc_direction(self.swipe_start, self.swipe_end))
        self.trigger_move()
        self.reset_swipe()

    def trigger_move(self):
        if calc_distance(self.swipe_start, self.swipe_end) <= 50:
            return
        direction = calc_direction(self.swipe_start, self.swipe_end)
        if "N" in direction:
            self.up()
        if "S" in direction:
            self.down()
        if "E" in direction:
            self.right()
        if "W" in direction:
            self.left()


class ButtonState(PrologueState):
    @rx.var
    def left_disabled(self) -> bool:
        return self.pos_x == 0

    @rx.var
    def right_disabled(self) -> bool:
        return self.pos_x == self.cols - 1

    @rx.var
    def up_disabled(self) -> bool:
        return self.pos_y == 0

    @rx.var
    def down_disabled(self) -> bool:
        return self.pos_y == self.rows - 1
