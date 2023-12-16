import reflex as rx

from ..state import ScrollState, ButtonState
from ..config import CFG


def create_button(direction, on_click):
    return rx.hstack(
        rx.button(
            rx.icon(tag=f"chevron_{direction}"),
            variant="outline",
            on_click=on_click,
            color=CFG.buttons.color,
            border_color=f"{CFG.buttons.border_color}{CFG.buttons.border_opacity:02x}",
            border_width=f"{CFG.buttons.border_width}px",
            icon_spacing=0,
            is_disabled=getattr(ButtonState, f"{direction}_disabled"),
            z_index=1,
            width="1rem",
        ),
        class_name="btn-frame",
    )


def create_btngrid():
    directions = {
        "left": ScrollState.left,
        "up": ScrollState.up,
        "down": ScrollState.down,
        "right": ScrollState.right,
    }
    grid_items = [
        rx.grid_item(
            create_button(direction, on_click),
            area=direction,
        )
        for direction, on_click in directions.items()
    ]
    return rx.grid(
        *grid_items,
        class_name="btn-grid",
    )
