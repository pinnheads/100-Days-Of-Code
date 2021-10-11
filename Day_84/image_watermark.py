from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class ImageWatermark:
    def __init__(self):
        self.text_color = (3, 8, 12)
        self.font = ImageFont.truetype(
            "/usr/share/fonts/noto/NotoSans-Regular.ttf",
            180,
        )

    def watermark_text(self, input_image_path, output_image_path, text, pos):
        photo = Image.open(input_image_path)
        # make the image editable
        drawing = ImageDraw.Draw(photo)
        drawing.text(
            pos,
            text,
            font=self.font,
            fill=self.text_color,
        )
        photo.show()
        photo.save(output_image_path)
        return output_image_path
