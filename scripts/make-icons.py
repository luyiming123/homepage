"""生成主页需要的 PNG 图标（与 favicon.svg 视觉一致）"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(parents=True, exist_ok=True)

TOP = (31, 95, 169, 255)      # #1f5fa9
BOTTOM = (18, 59, 107, 255)   # #123b6b
FG = (255, 255, 255, 255)


def font(size):
    for name in ("georgiab.ttf", "timesbd.ttf", "DejaVuSerif-Bold.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def gradient(size):
    img = Image.new("RGB", (1, size))
    for y in range(size):
        t = y / max(1, size - 1)
        img.putpixel((0, y), tuple(round(TOP[i] + (BOTTOM[i] - TOP[i]) * t) for i in range(3)))
    return img.resize((size, size))


def render(size):
    s = size * 4
    base = gradient(s).convert("RGBA")
    mask = Image.new("L", (s, s), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, s - 1, s - 1], radius=int(s * 0.22), fill=255)
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    img.paste(base, (0, 0), mask)
    d = ImageDraw.Draw(img)
    d.text((s / 2, s / 2 + s * 0.01), "YL", font=font(int(s * 0.44)), fill=FG, anchor="mm")
    return img.resize((size, size), Image.LANCZOS)


for size in (32, 180):
    name = "apple-touch-icon.png" if size == 180 else f"favicon-{size}x{size}.png"
    render(size).save(out / name)

render(64).save(out / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
print("已生成图标到", out)
for p in sorted(out.glob("*")):
    print(" -", p.name, p.stat().st_size, "bytes")
