import board
import time
import displayio
from adafruit_matrixportal.matrixportal import MatrixPortal
from adafruit_display_text.label import Label
from adafruit_bitmap_font import bitmap_font

matrixportal = MatrixPortal(status_neopixel=board.NEOPIXEL, bit_depth=6)
small_font = bitmap_font.load_font("/fonts/5x8.bdf")

main_group = displayio.Group()

text_label = Label(
    small_font,
    text="Victor",
    color=0xFFA500  # Orange
)

display_width = matrixportal.graphics.display.width
text_label.x = display_width
text_label.y = 5

main_group.append(text_label)
matrixportal.graphics.display.root_group = main_group

while True:
    text_label.x -= 1
    if (text_label.x + text_label.bounding_box[2]) < 0:
        text_label.x = display_width
    time.sleep(0.08)
