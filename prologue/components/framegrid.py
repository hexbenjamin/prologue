import itertools

import reflex as rx

from ..math import scale_min, scale_max
from ..state import PrologueState, SwipeState
from ..config import CFG


def frame_grid(mobile: bool = False):
    # print(scale_min())
    grid = rx.grid(
        *make_frames(),
        class_name="frame-grid",
        template_columns=f"repeat(6, calc({scale_min()}))",
        template_rows=f"repeat(3, calc({scale_min()}))",
        width="600vw",
        height="450vh",
        top=f"{(100 - CFG.grid.scale) / 2}vh",
        left=f"{(100 - CFG.grid.scale) / 2}vw",
    )
    return rx.box(
        grid,
        position="absolute",
        top=0,
        left=0,
        width="600vw",
        height="450vh",
        background_image=CFG.grid.bg.path,
        background_repeat=CFG.grid.bg.repeat,
        background_size=f"{CFG.grid.bg.size}px auto",
        transform=PrologueState.translation,
        transition_duration=f"{CFG.grid.speed}s",
        on_mouse_down=SwipeState.get_start,
        on_mouse_up=SwipeState.get_end,
    )


def make_frames():
    frames = []
    for row, col in itertools.product("ABC", range(1, 7)):
        frame_id = f"{row}{col}"
        if frame_id in CFG.grid.frames.keys():
            frame_dict = CFG.grid.frames[frame_id]
            img_src = f"/images/frames/{frame_dict['img']}"

            translate = f"translate({frame_dict['x']}%, {frame_dict['y']}%)"
            rotate = f"rotate({frame_dict['rotate']}deg)"
            transform = f"{translate} {rotate}"

            img_width, img_height = get_img_dims(frame_dict["scale"])

            frm = rx.grid_item(
                rx.image(
                    src=img_src,
                    width="auto",
                    height="auto",
                    # object_fit="contain" if frame_id == "B4" else "cover",
                    transform=transform,
                ),
                overflow="visible",
                area=frame_id,
                align_items="center",
                justify_content="center",
                class_name="frame",
                width=img_width,
                height=img_height,
            )

            frames.append(frm)

    return frames


def get_img_dims(dims):
    if dims["width"] and dims["height"] == 0:
        return f"{dims['width']}%", "auto"
    elif dims["width"] == 0 and dims["height"]:
        return "auto", f"{dims['height']}%"
    else:
        return f"{dims['width']}%", f"{dims['height']}%"
