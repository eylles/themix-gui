# from _typeshed import Incomplete
from typing import IO

# DEFAULT_NUM_COLORS: int
# DEFAULT_MINV: int
# DEFAULT_MAXV: int
# DEFAULT_BOLD_ADD: int
# DEFAULT_FONT_SIZE: int
# DEFAULT_BG_COLOR: str
# THUMB_SIZE: Incomplete
# SCALE: float

# def down_scale(x): ...
# def up_scale(x): ...
# def hexify(rgb): ...
# def get_colors(img): ...
# def clamp(color, min_v, max_v): ...
# def order_by_hue(colors): ...
# def brighten(color, brightness): ...
def colorz(
    fd: IO[bytes], n: int = ...,
    min_v: int = ..., max_v: int = ...,
    bold_add: int = ..., order_colors: bool = True
) -> list[tuple[tuple[int, int, int], tuple[int, int, int]]]:
    ...
# def html_preview(colors, font_size=..., bg_color=..., bg_img: Incomplete | None = ..., fd: Incomplete | None = ...): ...
# def parse_args(): ...
# def main() -> None: ...
