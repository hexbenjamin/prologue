"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
import reflex as rx

from .components import button_grid, frame_grid
from .state import PrologueState, SwipeState


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
        rx.tablet_and_desktop(button_grid()),
        frame_grid(),
        position="fixed",
        width="100vw",
        height="100vh",
        display="flex",
        justify_content="center",
        align_items="center",
        overflow="hidden",
        id="prologue",
    )


# Add state and page to the app.
app = rx.App(
    overlay_component=None,
    stylesheets=["css/styles.css"],
)
app.compile()
