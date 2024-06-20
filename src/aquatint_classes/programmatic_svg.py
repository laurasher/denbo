import pandas as pd
import numpy as np
import json
from pyaxidraw import axidraw


class ProgrammaticSvgManipulator:
    """
    This class is used to house multiple representations of an svg image to
    support art programming with AxiDraw and other PROGRAMMATIC applications.

    The xy coord representation cannot be back-converted, so this is only an
    output method used to send to AxiDraw.

    Methods:
    - Conversion from file contents to d-path, or xy coordinates
    - View in browser from file contents or d-path
    - file2dpath
    - file2xy
    - dpath2xy

    Attributes:
    - filename: str     (@input), source file name
    - xml: str          (@input, @output), xml file contents
    - d-path: str       (@input, @output), dpath from svg tag
    - xy: []            (@output), xy coordinates list of pair lists

    Dependent upon:
    - svg.path library
    """

    def __init__(self, filename):
        self.filename = filename
        self.xml = ""
        self.dpath = ""
        self.xy = []
        self.ad = axidraw.AxiDraw()
        self.units = 0  # 0 = inches, 1 = cm, 2 = mm
        self.units_map = {
            0: "inches",
            1: "cm",
            2: "mm",
        }
        self.initialize_ad()

        # Usable pen travel (inches): 34.02 × 23.39 inches.
        self.MAX_X = 34.02  # inches
        self.MAX_Y = 23.39  # inches
        ### These 3 were for 4 proofs on paper ###
        # self.scalar = 4.8
        # self.scalar = 6.4 #higher is smaller scale
        # self.scalar = 7.6 #higher is smaller scale
        ### These 3 were for 4 proofs on paper ###

        ### These are experiments for 9x12 plates ###
        self.scalar = 12
        ###  ###

        self.starting_origin = [0, 3]

        # Load in file
        self.cls_log(self.filename)
        if self.filename.split(".")[1] == "csv":
            self.cls_log("Loading aquatint points from csv...")
            self.xy = json.loads(
                (
                    pd.read_csv(self.filename)[["x_val", "y_val"]].to_json(
                        orient="values"
                    )
                )
            )
        self.cls_log("** Working area MAX X is 34.02 inches, MAX Y is 23.39 inches")
        self.cls_log(f"Original MAX X {max([_x[1] for _x in self.xy])}")
        self.cls_log(f"Original MAX Y {max([_x[0] for _x in self.xy])}")

        # Scale xy coordinates to fit within axidraw's travel area
        self.xy = [[x / self.scalar, y / self.scalar] for x, y in self.xy]
        self.cls_log(f"Scaled MAX X {max([_x[1] for _x in self.xy])}")
        self.cls_log(f"Scaled MAX Y {max([_x[0] for _x in self.xy])}")
        self.cls_log(f"Total points to plot {len(self.xy)}")

    def initialize_ad(self):
        # Initialize AxiDraw
        self.ad.interactive()
        try:
            self.ad.connect()
            self.ad.options.model = 5
            self.ad.options.units = self.units
            # fine sharpie settings
            # self.ad.options.pen_pos_up = 65 #default 60
            # self.ad.options.pen_pos_down = 5 #default 40

            # xl sharpie settings, sharpie sitting on cap ledge
            # self.ad.options.speed_pendown = 55  # default 25
            # self.ad.options.pen_pos_up = 100
            # self.ad.options.pen_pos_down = 40

            # paint marker for acetate positive settings
            self.ad.options.speed_pendown = 55  # default 25
            # self.ad.options.speed_pendown = 100  # default 25
            # self.ad.options.speed_penup = 100
            self.ad.options.pen_pos_up = 100
            self.ad.options.pen_pos_down = 40

            self.ad.update()
        except Exception as e:
            self.cls_log(f"Could not connect to AxiDraw: {e}")

    def cls_log(self, msg):
        print(f"[ProgrammaticSvgManipulator] {msg}")
        return

    def print_position(self):
        """
        Query, report, and print position and pen state
        """
        turtle_position = self.ad.turtle_pos()
        current_position = self.ad.current_pos()
        self.cls_log(
            f"Turtle position: {turtle_position[0]:0.3f}, {turtle_position[1]:0.3f}"
        )
        self.cls_log(
            f"Actual position: {current_position[0]:0.3f}, {current_position[1]:0.3f}\n"
        )
        return

    def add_current_pos_to_path(self, offset_xy):
        "Offset a list of xy coordinates by the current position of AxiDraw head"
        xy = []
        for i, _point in enumerate(self.xy):
            xy.append([self.xy[i][0] + offset_xy[0], self.xy[i][1] + offset_xy[1]])
        return xy

    def travel_to_page_center(self):
        self.ad.moveto(self.MAX_X / 2, self.MAX_Y / 2)
        return

    def calc_xy_size(self):
        "Calculate the total size of the image from xy coordinate list"
        _s = [
            round(max([_x[1] for _x in self.xy]) - min([_x[1] for _x in self.xy]), 1),
            round(max([_x[0] for _x in self.xy]) - min([_x[0] for _x in self.xy]), 1),
        ]
        self.cls_log(f"Total size in {self.units_map[self.units]} {_s}")
        return _s

    def draw_manual_circle(self, xy, of):
        try:
            # self.ad.moveto(xy[1] + of, xy[0])
            # self.ad.moveto(xy[1] + of, xy[0] + of)
            # self.ad.moveto(xy[1], xy[0] + of)
            # self.ad.moveto(xy[1], xy[0])
            self.ad.draw_path(
                [
                    [xy[1] + of, xy[0]],
                    [xy[1] + of, xy[0] + of],
                    [xy[1], xy[0] + of],
                    [xy[1], xy[0]],
                ]
            )
            return
        except Exception as e:
            self.cls_log(f"Unable to draw_manual_circle {e}")
            return

    def axidraw_calibrate(self):
        self.initialize_ad()
        self.ad.moveto(self.starting_origin[0], self.starting_origin[1])
        xy_current_pos = self.ad.current_pos()
        offset_xy = list(reversed(self.add_current_pos_to_path(xy_current_pos)))
        _maxx = max([_x[1] for _x in offset_xy])
        _minx = min([_x[1] for _x in offset_xy])
        _maxy = max([_x[0] for _x in offset_xy])
        _miny = min([_x[0] for _x in offset_xy])

        # Divide edges into divs, draw criss cross to test arm height
        div = 8
        diffx = (_maxx - _minx) / div
        diffy = (_maxy - _miny) / div
        self.ad.moveto(_minx, _miny)
        self.ad.pendown()
        for i in range(1, div + 1):
            (i % 2) and self.ad.lineto(_minx + diffx * i, _maxy)
            not (i % 2) and self.ad.lineto(_minx + diffx * i, _miny)
        self.ad.penup()
        self.ad.moveto(0, 0)

        # Draw random dots dist within bounding box to test id enough up/down
        n_dots = 10
        _maxx = max([_x[1] for _x in offset_xy])
        _minx = min([_x[1] for _x in offset_xy])
        _maxy = max([_x[0] for _x in offset_xy])
        _miny = min([_x[0] for _x in offset_xy])
        distx = np.random.uniform(_minx, _maxx, size=(n_dots, 1))
        disty = np.random.uniform(_miny, _maxy, size=(n_dots, 1))

        for i in range(n_dots):
            self.ad.moveto(distx[i][0], disty[i][0])
            self.ad.pendown()
            self.ad.penup()

        self.ad.moveto(0, 0)
        self.ad.disconnect()
        return

    def axidraw_xy_bounding_box(self):
        self.initialize_ad()
        # Move down 3 inches
        self.ad.moveto(self.starting_origin[0], self.starting_origin[1])
        xy_current_pos = self.ad.current_pos()
        offset_xy = list(reversed(self.add_current_pos_to_path(xy_current_pos)))
        _maxx = max([_x[1] for _x in offset_xy])
        _minx = min([_x[1] for _x in offset_xy])
        _maxy = max([_x[0] for _x in offset_xy])
        _miny = min([_x[0] for _x in offset_xy])
        self.cls_log(
            f"MAX_X: {round(_maxx,1)}, MIN_X: {round(_minx,1)}, MAX_Y: {round(_maxy,1)}, MIN_Y: {round(_miny,1)}"
        )
        self.ad.moveto(_minx, _miny)
        self.ad.pendown()
        self.ad.lineto(_minx, _maxy)
        self.ad.lineto(_maxx, _maxy)
        self.ad.lineto(_maxx, _miny)
        self.ad.lineto(_minx, _miny)
        self.ad.penup()
        self.ad.moveto(0, 0)
        self.ad.disconnect()
        return

    def axidraw_xy_dots_inches(self):
        self.initialize_ad()
        self.ad.moveto(self.starting_origin[0], self.starting_origin[1])
        of = 0.025
        # Draw xy points
        try:
            xy_current_pos = self.ad.current_pos()
            offset_xy = list(reversed(self.add_current_pos_to_path(xy_current_pos)))
            # offset_xy = self.add_current_pos_to_path(xy_current_pos)
            for ii, xy in enumerate(offset_xy):
                self.ad.moveto(xy[1], xy[0])
                self.ad.pendown()
                # self.draw_manual_circle(xy, of)
                self.ad.penup()
                not (ii % 100) and self.cls_log(f"XY progress {ii} / {len(offset_xy)}")
            self.cls_log("Done")
            self.print_position()
        except Exception as e:
            self.cls_log(f"Error: {e}")
            # Move home if errors out
            self.ad.moveto(0, 0)
            self.ad.disconnect()

        # Move home when finished
        self.ad.moveto(0, 0)
        self.ad.disconnect()
        return

    def axidraw_xy_path(self):
        self.cls_log(self.filename)
        if self.filename.split(".")[1] == "csv":
            self.cls_log("Loading aquatint points from csv...")
            self.xy = json.loads(
                (
                    pd.read_csv(self.filename)[["x_val", "y_val"]].to_json(
                        orient="values"
                    )
                )
            )

        self.cls_log(f"Total points to plot {len(self.xy)}")

        # Initialize AxiDraw
        self.ad.interactive()  # Enter interactive context
        if not self.ad.connect():  # Open serial port to AxiDraw;
            self.cls_log("Could not connect to AxiDraw")
            quit()  #   Exit, if no connection.
        # Set up Axidraw options
        self.ad.options.model = 5  # set axidraw model to AxiDraw SE/A1
        self.ad.options.units = self.units  # set units to inches
        self.ad.update()

        try:
            # Now change units to mm and draw svg path
            # self.ad.options.units = 2  # set units to mm
            # self.ad.update()
            xy_current_pos = self.ad.current_pos()
            # Have to add mm path to current pos to make it draw relative to where it is
            # points = self.add_current_pos_to_path(xy_current_pos)
            print(self.xy)
            print(self.xy[0])
            self.ad.draw_path(self.xy)  # Plot the path
            self.print_position()
            input()
        except Exception as e:
            self.cls_log(f"Error: {e}")
            self.ad.options.units = self.units  # set units to inches
            self.ad.update()
            self.ad.moveto(0, 0)
            self.ad.disconnect()

        # Move home when finished
        self.ad.options.units = self.units  # set units to inches
        self.ad.update()
        self.ad.moveto(0, 0)
        self.ad.disconnect()
        return
