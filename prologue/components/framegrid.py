import itertools

import reflex as rx

from ..state import ScrollState, SwipeState
from ..config import CFG


def frame_grid():
    return rx.grid(
        *make_frames(),
        style={"--pos-x": ScrollState.pos_x, "--pos-y": ScrollState.pos_y},
        class_name="frame-grid",
        background_image=CFG.grid.bg.path,
        background_repeat=CFG.grid.bg.repeat,
        background_size=f"{CFG.grid.bg.size}px auto",
        transform=ScrollState.translation,
        on_mouse_down=SwipeState.get_start,
    )


def make_frames():
    frames = []
    for row, col in itertools.product("ABC", range(1, 7)):
        frame_id = f"{row}{col}"
        if frame_id in CFG.grid.frames.keys():
            frame_dict = CFG.grid.frames[frame_id]
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
