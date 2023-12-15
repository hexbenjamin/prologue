import reflex as rx


def background(content):
    return rx.vstack(
        content,
        justify_content="center",
        class_name="background",
    )
