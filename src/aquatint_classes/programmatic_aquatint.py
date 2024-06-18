from PIL import Image, ImageOps
import numpy as np
import sys, os

# import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

'''
This class takes an image path and various parameters as inputs, 
and outputs a preview "aquatint" image plot and a csv file of
the aquatint points (x,y) locations.
'''

class ProgrammaticAquatint:
    def __init__(
        self,
        image_path,
        output_path,
        n_aquatint_pixels=5,
        sample_rate=0.5,
        view_images=False,
        use_sampled_image=False,
        data_channel_division_factor=1,
        plot_point_size=0.005,
    ):
        self.image_path = image_path
        self.output_path = output_path
        # n_aquatint_pixels is the number of pixels in the x and y direction from the original image
        # If n_aquatint_pixels is set to MAX, plot whole image in aquatint
        self.n_aquatint_pixels = n_aquatint_pixels
        self.sample_rate = sample_rate
        self.view_images = view_images
        self.use_sampled_image = use_sampled_image
        self.data_channel_division_factor = data_channel_division_factor
        self.plot_point_size = plot_point_size
        self.image_output_path = os.path.join(
            self.output_path, self.image_path.split(".")[0].replace("imgs/", ""), 
            f"div_factor_{data_channel_division_factor}_point_size_{plot_point_size}".replace(".", "p")
        )

    def cls_log(self, msg):
        print(f"[ProgrammaticAquatint] {msg}")
        return

    def img_plot(self, df, title, size=10):
        plt = sns.scatterplot(
            data=df,
            x="x_val",
            y="y_val",
            s=size,
            hue="data_channel",
            legend=False,
        )
        fig = plt.get_figure()
        fig.savefig(os.path.join(self.image_output_path, f"{title}.png"))
        fig.clf()
        return

    def histogram_plot(self, df, title, size=10):
        plt = sns.histplot(
            data=df,
            x="data_channel",
            # y="y_val",
        )
        fig = plt.get_figure()
        fig.savefig(os.path.join(self.image_output_path, f"{title}.png"))
        fig.clf()
        return

    def aquatint_plot(self, df, title, size):
        fig = plt.figure()
        ax = fig.add_subplot()
        plt.scatter(df["x_val"], df["y_val"], s=size, linewidths=0, color="black")
        plt.title(title)
        fig.tight_layout()

        # square plot
        ax.set_aspect("equal", adjustable="box")
        fig.savefig(
            os.path.join(self.image_output_path, f"aquatint_{title}.png"), dpi=300
        )
        plt.show()
        fig.clf()
        return

    def intensity_per_pixel(self):
        # Make folder for output and intermediate files
        # _img_output_path = os.path.join(self.output_path, self.image_path.split(".")[0])
        os.makedirs(self.image_output_path, exist_ok=True)
        img_file = Image.open(self.image_path)
        img_file.save(os.path.join(self.image_output_path, f"original.png"))
        
        # Invert the grayscale for katazome printing
        # img_file = ImageOps.invert(img_file)
        # img_file.save(os.path.join(self.image_output_path, f"original_inverted.png"))
        self.view_images and img_file.show()

        # get original image parameters...
        width, height = img_file.size
        format = img_file.format
        mode = img_file.mode

        # Make image Greyscale
        img_grey = img_file.convert("L")
        img_grey.save(os.path.join(self.image_output_path, f"grayscale.png"))
        self.view_images and img_grey.show()

        # Convert grayscale image to ARRAY
        value = np.asarray(img_grey.getdata(), dtype=int).reshape(
            (img_grey.size[1], img_grey.size[0])
        )
        # Convert array to DATAFRAME
        df = pd.DataFrame(value)
        df_stacked = df.stack().reset_index()
        # df_stacked.columns = ["x_val", "y_val", "data_channel"]
        df_stacked.columns = ["y_val", "x_val", "data_channel"]

        # Seaborn setting
        sns.set_style("white")

        # Add normalization step
        df_stacked["data_channel"] = [int(x) for x in df_stacked["data_channel"]]

        # Plot histogram of pixels across tonal range, before and after norm
        self.histogram_plot(df_stacked, "histogram_before_norm")
        self.img_plot(df_stacked, "flattened")

        # Save the aquatint image
        flattened_output_path = os.path.join(self.image_output_path, f"flattened.csv")
        df_stacked.to_csv(flattened_output_path, index=False)
        self.cls_log(f"Wrote flattened csv to {flattened_output_path}")


        # Try sampling the image- I don't really use this
        sr_str = f"{self.sample_rate}".replace(".", "p")
        sr_output_path = os.path.join(
            self.image_output_path, f"flattened_sample_rate_{sr_str}.csv"
        )
        df_stacked_sampled = df_stacked.sample(
            frac=self.sample_rate, replace=True, random_state=1
        ).reset_index(drop=True)

        # Don't save these anymore b/c I am not using the sampled image.
        0 and df_stacked_sampled.to_csv(sr_output_path, index=False)
        0 and self.img_plot(df_stacked_sampled, f"flattened_sr_{sr_str}")
        if self.use_sampled_image:
            self.cls_log(f"Wrote sampled flattened csv to {sr_output_path}")
            return df_stacked_sampled
        return df_stacked

    def aquatint_pixel(self, n_dots, x_offset=0, y_offset=0):
        dist = np.random.uniform(0, 1, size=(n_dots, 2))
        dist_df = pd.DataFrame(dist, columns=["x_val", "y_val"])
        dist_df["x_val"] = dist_df["x_val"] + x_offset
        dist_df["y_val"] = dist_df["y_val"] + y_offset
        dist_df["data_channel"] = 1
        return dist_df

    def aquatint(self):
        df = self.intensity_per_pixel()
        print(df)
        max_data_channel = df["data_channel"].max()
        min_data_channel = df["data_channel"].min()
        print(max_data_channel)
        print(min_data_channel)
        row_pixels = []

        if self.n_aquatint_pixels == "MAX":
            XMAX = df["x_val"].max()
            YMAX = df["y_val"].max()
        else:
            XMAX = self.n_aquatint_pixels
            YMAX = self.n_aquatint_pixels

        if self.use_sampled_image:
            xrange = list(set(df["x_val"]))
            yrange = list(set(df["y_val"]))
        else:
            xrange = range(XMAX)
            yrange = range(YMAX)

        self.cls_log(f"------> X MAX: {XMAX}")
        self.cls_log(f"------> Y MAX: {YMAX}")
        self.cls_log(f"------> xrange: {xrange}")
        self.cls_log(f"------> yrange: {yrange}")
        # Flip order here in order to draw left to right as opposed to top to bottom
        # Make one aquatint pixel
        for y in yrange:
            row = df[df["y_val"] == y]
            if self.use_sampled_image:
                xrange = list(set(row["x_val"]))
            for x in xrange:
                n_dots = row[row["x_val"] == x]["data_channel"].values[0]
                n_dots = int(n_dots / self.data_channel_division_factor)
                # n_dots = int(n_dots / (min_data_channel*self.data_channel_division_factor))
                pixel = self.aquatint_pixel(n_dots, x, y)
                row_pixels.append(pixel)
            not (x % 10) and self.cls_log(f"-- Progress X: {x} Y: {y}")
        row_pixels = pd.concat(row_pixels)
        row_pixels.to_csv(
            os.path.join(self.image_output_path, "aquatint_pixel_concat.csv"),
            index=False,
        )
        self.cls_log(f"Total points in aq {(row_pixels.shape[0])}")
        self.aquatint_plot(row_pixels, "aquatint_pixel_concat", self.plot_point_size)
        return os.path.join(self.image_output_path, "aquatint_pixel_concat.csv")


def main():
    n_aquatint_pixels = 150
    # aq = ProgrammaticAquatint("long_copper_img.png", "output", n_aquatint_pixels)
    # lop56011_crop MAX ---> X: 542 Y: 362
    aq = ProgrammaticAquatint(
        "lop56011_crop.jpg",
        "output",
        n_aquatint_pixels=n_aquatint_pixels,
        sample_rate=0.25,
        use_sampled_image=False,
        data_channel_division_factor=5,
    )
    aq.aquatint()


if __name__ == "__main__":
    main()
