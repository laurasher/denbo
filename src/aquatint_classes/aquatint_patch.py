import random
import pandas as pd
import numpy as np
import json
import datetime
from pyaxidraw import axidraw

from PIL import Image, ImageOps
import sys, os
import seaborn as sns
import matplotlib.pyplot as plt


class AquatintPatch:
    """
    This class is used to

    Methods:

    Attributes:

    Dependent upon:
    """

    def __init__(
        self,
        xy,
        patch_pos_from_source,
        patch_w,
        patch_h,
        patch_pos_on_page,
        print_page_w,
        print_page_h,
    ):
        self.xy = xy
        self.xoffset = patch_pos_on_page[1]
        self.yoffset = patch_pos_on_page[0]
        self.patch_origin_x = patch_pos_from_source[1]
        self.patch_origin_y = patch_pos_from_source[0]
        self.patch_w = patch_w
        self.patch_h = patch_h
        self.print_page_w = print_page_w
        self.print_page_h = print_page_h
        self.patch_xy = []
        self.df = pd.DataFrame()

        self.printing_origin = [0, 0]

        # Select patch from input x,y
        self.patch_xy = [
            [x, y]
            for x, y in self.xy
            if (x >= self.patch_origin_x and x <= self.patch_origin_x + self.patch_h)
            and (y >= self.patch_origin_y and y <= self.patch_origin_y + self.patch_w)
        ]

        self.df["x_val"] = [_p[1] for _p in self.patch_xy]
        self.df["y_val"] = [_p[0] for _p in self.patch_xy]

        # Then reposition path to origin

        # Then translate to yoffset, xoffset

        # Scale xy coordinates to fit within axidraw's travel area

    def get_df(self):
        return self.df
    
    def preview(self, size=0.02):
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.set(xlim=(0, self.print_page_w), ylim=(0, self.print_page_h))
        ax.invert_yaxis()
        ax.invert_xaxis()
        plt.scatter(self.df["x_val"], self.df["y_val"], s=size, color="black")
        # plt.scatter(self.df["x_val"], self.df["y_val"], s=size, marker="s", linewidths=size/2, color="white", edgecolors="black")
        plt.scatter(
            min(self.df["x_val"]),
            min(self.df["y_val"]),
            s=size * 100,
            linewidths=0,
            color="red",
        )
        # plt.title(title)
        fig.tight_layout()
        ax.set_aspect("equal", adjustable="box")
        plt.show()
        fig.clf()
        return
