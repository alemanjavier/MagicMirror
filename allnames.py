import time
import board
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

# Define the list of kids' names with their favorite colors
kids_data = [
    {"name": "Aya", "color": 0xFF0000},  # Red
    {"name": "Logan", "color": 0xFFFF00},  # Yellow
    {"name": "Victor", "color": 0xFF6600},  # Deeper Orange
    {"name": "Yoel", "color": 0xFF0000},  # Red
    {"name": "Yael", "color": 0xFF00FF},  # Magenta
]

# Display settings
display_width = matrixportal.graphics.display.width
display_height = matrixportal.graphics.display.height

# Loop through the kids' names and display them one by one
while True:
    for kid in kids_data:
        # Create the text label for the current name
        text_label = Label(small_font, text=kid["name"], color=kid["color"])

        # Set the text label to start at the right edge of the screen
        text_label.x = display_width
        text_label.y = display_height // 2 - 4  # Vertically center the text (slightly adjusted)

        # Add label to the main group
        main_group.append(text_label)

        # Set the root group to the display
        matrixportal.graphics.display.root_group = main_group

        # Scroll the text from right to left
        while text_label.x + text_label.bounding_box[2] > 0:  # Keep scrolling until the text is off the screen
            text_label.x -= 1  # Move the text left by 1 pixel
            time.sleep(0.08)  # Control the speed of the scrolling

        # Pause briefly before the next name starts
        time.sleep(0.5)

        # Clear the previous label for the next loop iteration
        main_group.remove(text_label)
