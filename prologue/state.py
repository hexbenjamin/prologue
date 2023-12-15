import reflex as rx


class ScrollState(rx.State):
    """The app state."""

    direction: str = "down"
    pos_x: int = 0
    pos_y: int = 0

    @rx.var
    def bg_position(self) -> str:
        return f"{self.pos_x * 100}vw {self.pos_y * 100}vh"

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
