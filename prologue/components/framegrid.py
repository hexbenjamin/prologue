import itertools

import reflex as rx

from ..state import PrologueState, SwipeState
from ..config import CFG


cell_size = f"calc(min({CFG.grid.container.scale}vw, {CFG.grid.container.scale}vh))"


def frame_grid():
    return rx.box(
        rx.grid(
            *make_frames(),
            class_name="frame-grid",
            template_columns=f"repeat({PrologueState.cols}, {CFG.grid.container.scale}vw)",
            template_rows=f"repeat({PrologueState.rows}, {CFG.grid.container.scale}vh)",
            transform=PrologueState.translation,
            on_mouse_down=SwipeState.get_start,
            on_mouse_up=SwipeState.get_end,
        ),
        padding=f"{(100 - CFG.grid.container.scale) / 2}vh",
        background_image=CFG.grid.bg.path,
        background_repeat=CFG.grid.bg.repeat,
        background_size=f"{CFG.grid.bg.size}px auto",
        width=f"calc({PrologueState.cols} * {cell_size})",
        height=f"calc({PrologueState.rows} * {cell_size})",
        class_name="frame-grid-container",
    )


def make_frames():
    frames = []
    for row, col in itertools.product("ABC", range(1, 7)):
        frame_id = f"{row}{col}"
        if frame_id in CFG.grid.frames.keys():
            frame_dict = CFG.grid.frames[frame_id]
            img_src = f"/images/frames/{frame_dict['img']}"
            width = f"{frame_dict['width']}%"

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
                align_items="center",
                justify_content="center",
                class_name="frame",
                width=cell_size,
                height=cell_size,
            )

            frames.append(frm)

    return frames
