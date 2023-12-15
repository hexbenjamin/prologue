import reflex as rx

from ..state import ScrollState


def background(content):
    return rx.box(
        rx.tablet_and_desktop(buttons()),
        rx.vstack(
            content,
            justify_content="center",
            width="100%",
            height="100%",
        ),
        width="100vw",
        height="100vh",
        class_name="background",
        background_position=ScrollState.bg_position,
    )


def create_button(direction, on_click):
    return rx.hstack(
        rx.button(
            rx.icon(tag=f"chevron_{direction}"),
            variant="outline",
            on_click=on_click,
            color="#ffc8ff",
            border_color="#ffc8ff80",
            border_width="2px",
            icon_spacing=0,
            is_disabled=getattr(ScrollState, f"{direction}_disabled"),
            z_index=1,
            width="1rem",
        ),
        class_name="btn-frame",
    )


def buttons():
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
    return rx.box(
        rx.grid(
            *grid_items,
            class_name="btn-grid",
        ),
        position="absolute",
        top="0%",
        left="0%",
        bottom="0%",
        right="0%",
        display="flex",
        justify_content="center",
        align_items="center",
    )
