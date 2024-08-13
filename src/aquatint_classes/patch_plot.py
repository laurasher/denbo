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


class PatchPlot:
    """
    This class is used to

    Methods:

    Attributes:

    Dependent upon:
    """

    def __init__(
        self,
        patch_list,  # patch_list is a list of AquatintPatch objects
        print_page_w,
        print_page_h,
    ):
        self.patch_list = patch_list
        self.print_page_w = print_page_w
        self.print_page_h = print_page_h

    def preview(self, size=1):
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.set(xlim=(0, self.print_page_w), ylim=(0, self.print_page_h))
        ax.invert_yaxis()
        ax.invert_xaxis()

        for patch in self.patch_list:
            plt.scatter(
                patch.get_df()["x_val"], patch.get_df()["y_val"], s=size, c="black", marker="o", edgecolor='none'
            )
        fig.tight_layout()
        ax.set_aspect("equal", adjustable="box")
        plt.show()
        fig.clf()
        return
