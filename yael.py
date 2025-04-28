# Scrolling "Yael" slowly across the 16x32 Matrix using MatrixPortal

import board
import time
import displayio
from adafruit_matrixportal.matrixportal import MatrixPortal
from adafruit_display_text.label import Label
from adafruit_bitmap_font import bitmap_font

# Setup MatrixPortal
matrixportal = MatrixPortal(status_neopixel=board.NEOPIXEL, bit_depth=6)

# Load small pixel font
small_font = bitmap_font.load_font("/fonts/5x8.bdf")

# Create Main Display Group
main_group = displayio.Group()

# Create the Text Label
text_label = Label(
    small_font,
    text="Yael",
    color=0xFF0000  # Red
)

# Start at the right edge
display_width = matrixportal.graphics.display.width
text_label.x = display_width
text_label.y = 5  # vertical position

# Add label to main group
main_group.append(text_label)

# Set the root group to the display
matrixportal.graphics.display.root_group = main_group

# ==== Main Loop ====
while True:
    text_label.x -= 1  # Move left by 1 pixel

    # If the text moves completely off screen, reset to right
    if (text_label.x + text_label.bounding_box[2]) < 0:
        text_label.x = display_width

    time.sleep(0.08)  # SLOWER speed (bigger = slower)
