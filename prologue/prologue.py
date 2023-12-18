"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
import reflex as rx

from .components import button_grid, frame_grid
from .state import PrologueState


@rx.page("/", title="Prologue", image="favicon.ico", on_load=PrologueState.initialize)
def index() -> rx.Component:
    return rx.box(
        rx.script(
            """let mousePosition = { x: 0, y: 0 };

            function handleMoveEvent(e) {
                if (e.type === 'mousemove') {
                    mousePosition.x = e.clientX;
                    mousePosition.y = e.clientY;
                } else if (e.type === 'touchmove') {
                    mousePosition.x = e.touches[0].clientX;
                    mousePosition.y = e.touches[0].clientY;
                }
            }

            document.addEventListener('mousemove', handleMoveEvent);
            document.addEventListener('touchmove', handleMoveEvent);"""
        ),
        rx.desktop_only(
            button_grid(),
            frame_grid(mobile=False),
        ),
        rx.mobile_and_tablet(
            button_grid(),
            frame_grid(mobile=True),
        ),
        position="absolute",
        top=0,
        left=0,
        width="100vw",
        height="100vh",
        overflow="hidden",
    )


# Add state and page to the app.
app = rx.App(
    overlay_component=None,
    stylesheets=["css/styles.css"],
)
app.compile()
