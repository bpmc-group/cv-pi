from PIL import Image
from PIL.ExifTags import TAGS
img = Image.open('runs/testxx.jpg')
exif_data = img._getexif()
for tag, value in exif_data.items():
  print(TAGS.get(tag, tag), value)

# the following is NOT EXIF info - it's PIL image info
width, height = img.size
print(f"W: {width}  H: {height}")
