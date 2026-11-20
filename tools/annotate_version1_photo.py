"""Create a numbered observation overlay for the user-supplied tank photo."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
folder = ROOT / 'case-studies' / 'version-1'
image = Image.open(folder / 'original-photo.jpeg').convert('RGB')
scale = 1.5
image = image.resize((int(image.width*scale), int(image.height*scale)))
canvas = Image.new('RGB', (image.width, image.height + 180), '#f4f7f9')
canvas.paste(image, (0, 0))
draw = ImageDraw.Draw(canvas)
font_path = Path('C:/Windows/Fonts/arial.ttf')
bold_path = Path('C:/Windows/Fonts/arialbd.ttf')
font = ImageFont.truetype(str(font_path), 20) if font_path.exists() else ImageFont.load_default()
bold = ImageFont.truetype(str(bold_path), 24) if bold_path.exists() else font

points = [(520, 275, '1'), (685, 365, '2'), (405, 238, '3'), (457, 488, '4'), (168, 205, '5')]
for x, y, label in points:
    x, y = int(x*scale), int(y*scale)
    r = 22
    draw.ellipse((x-r, y-r, x+r, y+r), fill='#fff4cc', outline='#173d59', width=4)
    box = draw.textbbox((0, 0), label, font=bold)
    draw.text((x-(box[2]-box[0])/2, y-(box[3]-box[1])/2-2), label, fill='#17324a', font=bold)

top = image.height + 12
draw.text((24, top), 'PHOTO OBSERVATIONS - VERIFY ON SITE', fill='#17324a', font=bold)
legend = [
    '1  Open-top rectangular process tank; exact service and dimensions are not identifiable.',
    '2  Repeated side-wall features may be ribs, rails, or fittings; their function is unconfirmed.',
    '3  Three dark vertical features at the far end; could be components or image shadows.',
    '4  Visible bottom/step transition; inspect bottom construction and any internal partition.',
    '5  Left rim-side assembly; its electrical or structural role cannot be determined from this view.'
]
for i, line in enumerate(legend):
    draw.text((26, top + 38 + i*22), line, fill='#243b4d', font=font)

canvas.save(folder / 'photo-observations.png', optimize=True)
print(folder / 'photo-observations.png')
