"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
import reflex as rx


class State(rx.State):
    """The app state."""

    pass


@rx.page("/", title="Prologue", image="favicon.ico")
def index() -> rx.Component:
    return rx.vstack(
        rx.container(
            class_name="background",
        ),
        class_name="viewport",
    )


# Add state and page to the app.
app = rx.App(
    overlay_component=None,
    stylesheets=["css/styles.css"],
)
app.compile()
