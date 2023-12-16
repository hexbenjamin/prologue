import math
import reflex as rx

from rich import inspect


class BaseState(rx.State):
    """The app state."""

    pos_x: int = 0
    pos_y: int = 0
    cols: int = 6
    rows: int = 3

    def initialize(self):
        self.pos_x = 0
        self.pos_y = 0


class ScrollState(BaseState):
    @rx.var
    def translation(self) -> str:
        return f"translate({self.pos_x * 100}vw, {self.pos_y * 100}vh)"

    def left(self):
        self.pos_x += 1

    def right(self):
        self.pos_x -= 1

    def up(self):
        self.pos_y += 1

    def down(self):
        self.pos_y -= 1


class SwipeState(BaseState):
    swipe_start: tuple[int, int] = (-1, -1)
    swipe_end: tuple[int, int] = (-1, -1)

    mouse_x: int = 0
    mouse_y: int = 0

    def get_start(self):
        return [
            rx.call_script(
                '["start", [mousePosition.x, mousePosition.y]]',
                callback=SwipeState.update_coords,
            )
        ]

    def update_coords(self, coords):
        self.mouse_x, self.mouse_y = coords
        print(f"cartesian: {(self.mouse_x, self.mouse_y)}")


class ButtonState(BaseState):
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
