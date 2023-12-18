import itertools

import reflex as rx

from ..math import scale_min, scale_max
from ..state import PrologueState, SwipeState
from ..config import CFG


def frame_grid(mobile: bool = False):
    # print(scale_min())
    grid = rx.grid(
        *make_frames(mobile),
        class_name="frame-grid",
        template_columns="repeat(6, 100vw)",
        template_rows="repeat(3, 100vh)",
        width="600vw",
        height="300vh",
        top=0,
        left=0,
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


def make_frames(mobile: bool = False):
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
                rx.container(
                    rx.image(
                        src=img_src,
                        width=f"{frame_dict['scale']}%",
                        height=f"{frame_dict['scale']}%",
                        object_fit="contain",
                        transform=transform,
                    ),
                    # align_items="center",
                    # justify_content="center",
                    center_content=True,
                    width="100%",
                    height="100%",
                    padding=f"calc({scale_min(5)})",
                ),
                overflow="visible",
                area=frame_id,
                class_name="frame",
                # width=width,
                # height=height,
                position="relative",
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
