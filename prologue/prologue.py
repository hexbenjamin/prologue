"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
import reflex as rx

from .components import background, frame_grid
from .state import ScrollState


@rx.page("/bruh", title="Prologue", image="favicon.ico")
def dom_bruh() -> rx.Component:
    return background(
        rx.image(
            src="/images/dom_bruh.png",
            width="calc(min(42vw, 42vh))",
            box_shadow="0 0 10px 10px #d3bd7088",
        ),
    )


@rx.page("/", title="Prologue", image="favicon.ico", on_load=ScrollState.initialize)
def index() -> rx.Component:
    return background(frame_grid())


# Add state and page to the app.
app = rx.App(
    overlay_component=None,
    stylesheets=["css/styles.css"],
)
app.compile()
