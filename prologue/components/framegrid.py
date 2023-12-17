import itertools

import reflex as rx

from ..math import scale_min, scale_max
from ..state import PrologueState, SwipeState
from ..config import CFG


def frame_grid():
    # print(scale_min())
    grid = rx.grid(
        *make_frames(),
        class_name="frame-grid",
        template_columns=f"repeat(6, calc({scale_min()}))",
        template_rows=f"repeat(3, calc({scale_min()})",
        width=f"{6 * CFG.grid.scale}vw",
        height=f"{3 * CFG.grid.scale}vh",
        top=0,
        left=0,
    )
    return rx.box(
        grid,
        position="absolute",
        top=0,
        left=0,
        width="600vw",
        height="300vh",
        center_content=True,
        background_image=CFG.grid.bg.path,
        background_repeat=CFG.grid.bg.repeat,
        background_size=f"{CFG.grid.bg.size}px auto",
        transform=PrologueState.translation,
        transition_duration=f"{CFG.grid.speed}s",
        on_mouse_down=SwipeState.get_start,
        on_mouse_up=SwipeState.get_end,
        padding=f"calc({scale_max(100 - CFG.grid.scale)} / 2)",
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

            frm = rx.grid_item(
                rx.image(
                    src=img_src,
                    width=f"{frame_dict['scale']}%",
                    height=f"{frame_dict['scale']}%",
                    object_fit="contain",
                    transform=transform,
                ),
                area=frame_id,
                align_items="center",
                justify_content="center",
                class_name="frame",
                width=f"calc({scale_min()} * 2)"
                if frame_id == "A5"
                else f"calc({scale_min()})",
                height=f"calc({scale_min()} * 2)"
                if frame_id == "B4"
                else f"calc({scale_min()})",
            )

            frames.append(frm)

    return frames
