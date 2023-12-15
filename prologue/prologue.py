"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
import reflex as rx

from .components import background


class State(rx.State):
    """The app state."""

    pass


@rx.page("/", title="Prologue", image="favicon.ico")
def dom_bruh() -> rx.Component:
    return background(
        rx.image(
            src="/images/dom_bruh.png",
            width="42vw",
            box_shadow="0 0 10px 10px #d3bd7088",
        ),
    )


@rx.page("/scrollin", title="Scrollogue .", image="favicon.ico")
def scrollin() -> rx.Component:
    return background(
        rx.image(
            src="/images/dom_bruh.png",
            width="42vw",
            box_shadow="0 0 10px 10px #d3bd7088",
        ),
    )


# Add state and page to the app.
app = rx.App(
    overlay_component=None,
    stylesheets=["css/styles.css"],
)
app.compile()
