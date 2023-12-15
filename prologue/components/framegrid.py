import itertools

import reflex as rx

from ..state import ScrollState
from .. import config as CFG


def frame_grid():
    return rx.grid(
        *make_frames(),
        class_name="frame-grid",
        transform=ScrollState.translation,
        background_image="/images/bricks.png",
        background_repeat="repeat",
        background_size="calc(max(50vh, 50vw)) auto",
    )


def make_frames():
    frames = []
    for row, col in itertools.product("ABC", range(1, 7)):
        frame_id = f"{row}{col}"
        if frame_id in CFG.frames.keys():
            frame_dict = CFG.frames[frame_id]
            img_src = f"/images/frames/{frame_dict['img']}"
            width = f"calc(min({frame_dict['width']}vw, {frame_dict['width']}vh))"

            translate = f"translate({frame_dict['x']}%, {frame_dict['y']}%)"
            rotate = f"rotate({frame_dict['rotate']}deg)"
            transform = f"{translate} {rotate}"

            frm = rx.grid_item(
                rx.image(
                    src=img_src,
                    width=width,
                    height="auto",
                    transform=transform,
                ),
                area=frame_id,
                align_self="center",
                justify_self="center",
                class_name="frame",
                width=width,
            )

            frames.append(frm)

    return frames
