import time
import json
from pyaxidraw import axidraw  # import module

# Used this tool to convert svg path to point path in mm
# https://spotify.github.io/coordinator/

ad = axidraw.AxiDraw()  # Initialize class


def print_position():
    """
    Query, report, and print position and pen state
    """
    turtle_position = ad.turtle_pos()
    current_position = ad.current_pos()
    print(f"Turtle position: {turtle_position[0]:0.3f}, {turtle_position[1]:0.3f}")
    print(f"Actual position: {current_position[0]:0.3f}, {current_position[1]:0.3f}\n")


def add_current_pos_to_path(point_list, xy):
    for i, _point in enumerate(point_list):
        point_list[i] = [_point[0] + xy[0], _point[1] + xy[1]]
    return point_list


# Load in points file
with open("points.json") as f:
    points = json.load(f)

ad.interactive()  # Enter interactive context
if not ad.connect():  # Open serial port to AxiDraw;
    quit()  #   Exit, if no connection.

# Set up Axidraw options
ad.options.model = 5  # set axidraw model to AxiDraw SE/A1
ad.options.units = 0  # set units to inches
ad.update()

# Usable pen travel (inches): 34.02 × 23.39 inches.
MAX_Y = 23.39  # inches
MAX_X = 34.02  # inches

# Travel to center of page
ad.moveto(MAX_X / 2, MAX_Y / 2)

try:
    # Now change units to mm and draw svg path
    ad.options.units = 2  # set units to mm
    ad.update()
    xy = ad.current_pos()
    # Have to add mm path to current pos to make it draw relative to where it is
    points = add_current_pos_to_path(points, xy)
    ad.draw_path(points)  # Plot the path
    print_position()
    input()
except Exception as e:
    print(f"Error: {e}")
    ad.options.units = 0  # set units to inches
    ad.update()
    ad.moveto(0, 0)
    ad.disconnect()

# Move home when finished
ad.options.units = 0  # set units to inches
ad.update()
ad.moveto(0, 0)
ad.disconnect()
