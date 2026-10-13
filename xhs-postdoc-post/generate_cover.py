from pathlib import Path
from random import Random

from PIL import Image, ImageDraw, ImageFilter, ImageFont


OUT = Path(__file__).with_name("xhs_cover.png")
W, H = 1080, 1440

FONT_REGULAR = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
FONT_MEDIUM = "/usr/share/fonts/opentype/noto/NotoSansCJK-Medium.ttc"
FONT_BOLD = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def centered(draw: ImageDraw.ImageDraw, text: str, y: int, fnt, fill) -> None:
    bbox = draw.textbbox((0, 0), text, font=fnt)
    x = (W - (bbox[2] - bbox[0])) // 2
    draw.text((x, y), text, font=fnt, fill=fill)


def draw_paper_texture(base: Image.Image, box: tuple[int, int, int, int]) -> None:
    rng = Random(202706)
    tex = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    layer = ImageDraw.Draw(tex)
    x0, y0, x1, y1 = box
    for _ in range(95):
        x = rng.randint(x0, x1)
        y = rng.randint(y0, y1)
        r = rng.randint(18, 70)
        alpha = rng.randint(10, 24)
        shade = rng.choice([(225, 225, 220), (255, 255, 255), (210, 215, 218)])
        layer.ellipse((x - r, y - r, x + r, y + r), fill=(*shade, alpha))
    base.alpha_composite(tex.filter(ImageFilter.GaussianBlur(20)))


def main() -> None:
    img = Image.new("RGBA", (W, H), (82, 126, 245, 255))
    draw = ImageDraw.Draw(img)

    blue_dark = (52, 80, 162, 255)
    black = (5, 5, 5, 255)
    gray = (142, 148, 154, 255)
    paper = (247, 247, 245, 255)
    green = (169, 255, 118, 230)

    # Paper shadow.
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    paper_box = (70, 112, 1010, 1322)
    sd.rounded_rectangle((86, 126, 1028, 1338), radius=20, fill=(0, 0, 0, 46))
    img.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(18)))

    # Top clip.
    draw.rounded_rectangle((48, 84, 1032, 126), radius=12, fill=blue_dark)

    # Ticket-like paper body.
    draw.rectangle(paper_box, fill=paper)
    draw_paper_texture(img, paper_box)
    draw = ImageDraw.Draw(img)

    # Side notches and lower perforation.
    draw.ellipse((42, 1118, 102, 1178), fill=(82, 126, 245, 255))
    draw.ellipse((978, 1118, 1038, 1178), fill=(82, 126, 245, 255))
    for x in range(82, 990, 68):
        draw.ellipse((x, 1300, x + 48, 1348), fill=(82, 126, 245, 255))

    # Dotted divider.
    for x in range(124, 956, 32):
        draw.rectangle((x, 1147, x + 5, 1152), fill=gray)
        draw.rectangle((x + 11, 1147, x + 16, 1152), fill=gray)

    # Main short text. The green underline intentionally catches only the first phrase.
    draw.rounded_rectangle((150, 462, 520, 514), radius=18, fill=green)
    draw.text((150, 380), "寻找2027", font=font(FONT_BOLD, 118), fill=black)
    draw.text((150, 555), "生信 AI4S", font=font(FONT_BOLD, 118), fill=black)
    draw.text((150, 730), "博后/交换机会", font=font(FONT_BOLD, 100), fill=black)

    # Small bottom metadata, kept visually secondary.
    draw.text((120, 1224), "Singapore / North America", font=font(FONT_MEDIUM, 30), fill=gray)
    draw.text((120, 1264), "postdoc / exchange", font=font(FONT_MEDIUM, 30), fill=gray)
    draw.text((782, 1234), "空间组学", font=font(FONT_MEDIUM, 28), fill=gray)
    draw.text((782, 1274), "生物信息", font=font(FONT_MEDIUM, 28), fill=gray)

    img.convert("RGB").save(OUT, "PNG", optimize=True)


if __name__ == "__main__":
    main()
