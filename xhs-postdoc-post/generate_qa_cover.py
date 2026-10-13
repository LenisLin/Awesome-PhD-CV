from pathlib import Path
from random import Random

from PIL import Image, ImageDraw, ImageFilter, ImageFont


OUT = Path(__file__).with_name("xhs_qa_cover.png")
W, H = 1080, 1440

FONT_REGULAR = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"
FONT_MEDIUM = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Medium.ttc"
FONT_BOLD = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def texture(base: Image.Image, box: tuple[int, int, int, int]) -> None:
    rng = Random(20270607)
    tex = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(tex)
    x0, y0, x1, y1 = box
    for _ in range(160):
        x = rng.randint(x0, x1)
        y = rng.randint(y0, y1)
        r = rng.randint(18, 90)
        shade = rng.choice([(255, 255, 255), (224, 226, 220), (236, 234, 226), (245, 242, 235)])
        draw.ellipse((x - r, y - r, x + r, y + r), fill=(*shade, rng.randint(5, 18)))
    base.alpha_composite(tex.filter(ImageFilter.GaussianBlur(26)))


def draw_text(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, size: int, fill, bold=True) -> None:
    draw.text(xy, text, font=font(FONT_BOLD if bold else FONT_MEDIUM, size), fill=fill)


def underline(draw: ImageDraw.ImageDraw, x0: int, y: int, x1: int, color) -> None:
    draw.arc((x0, y - 12, x1, y + 22), start=8, end=173, fill=color, width=7)


def main() -> None:
    paper = (248, 247, 242, 255)
    ink = (5, 5, 5, 255)
    orange = (238, 100, 34, 255)
    muted = (55, 55, 55, 255)

    img = Image.new("RGBA", (W, H), paper)
    texture(img, (0, 0, W, H))
    draw = ImageDraw.Draw(img)

    # Minimal reference-style header.
    draw_text(draw, (52, 45), "(Sat.)", 42, ink)
    draw_text(draw, (828, 50), "六月六日", 34, ink)

    # Main Q&A hook.
    x = 126
    draw_text(draw, (x, 505), "植物wet lab转生信", 70, ink)
    underline(draw, 650, 596, 875, orange)
    draw_text(draw, (x, 670), "再转AI4S", 82, ink)
    underline(draw, 388, 770, 650, orange)
    draw_text(draw, (x, 855), "有什么想问的吗", 82, ink)

    # A small footer gives context without weakening the cover.
    draw_text(draw, (70, 1290), "PhD student 视角", 28, muted, bold=False)
    draw_text(draw, (742, 1290), "Q&A", 30, muted, bold=False)

    img.convert("RGB").save(OUT, "PNG", optimize=True)


if __name__ == "__main__":
    main()
