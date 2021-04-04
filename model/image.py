import base64
import io

import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import matplotlib.pyplot as plt

from model.ssd import DataTransform
from utils import utils


class SsdImage(object):
    def __init__(self, binary_data):
        self.binary = binary_data
        self.color_mean = (104, 117, 123)
        self.input_size = 300

        self.__origin = Image.open(io.BytesIO(base64.b64decode(self.binary)))
        # numpy配列(RGBA) <- PILイメージ
        img_numpy = np.asarray(self.__origin)
        # numpy配列(BGR) <- numpy配列(RGBA)
        self.target = cv2.cvtColor(img_numpy, cv2.COLOR_RGBA2BGR)
        self.height, self.width, self.channels = self.target.shape
        self.bbox_list = list()

    def get_origin(self, binary=False):
        if not binary:
            return self.__origin
        else:
            output = io.BytesIO()
            self.__origin.save(output, format="JPEG")
            return base64.b64encode(output.getvalue())

    def show(self):
        plt.imshow(cv2.cvtColor(self.target, cv2.COLOR_BGR2RGB))
        plt.show()

    def transform(self, phase="val"):
        transform = DataTransform(self.input_size, self.color_mean)
        self.target, _, _ = transform(
            self.target, phase, "", "")

    def attach_bbox(self, fnt):
        """
        物体検出の予測結果を画像で表示させる関数。
        """
        d = ImageDraw.Draw(self.__origin)
        fnt = ImageFont.truetype(font=fnt, size=utils.bbox_text_size(self.height, self.width))
        # BBox分のループ
        for bbox in self.bbox_list:
            bbox.add_label_data(d=d, fnt=fnt)

            d.rectangle(bbox.coordinates, outline=bbox.color, width=utils.bbox_rectangle_width(self.height, self.width))
            d.rectangle([bbox.label["coordinate"], tuple(np.array(bbox.label["coordinate"]) + bbox.label["size"])],
                        fill=bbox.color)
            d.text(xy=bbox.label["coordinate"], text=bbox.label["display_text"], font=fnt)


class BBox(object):
    def __init__(self):
        self.__score = None
        self.__coordinates = None
        self.__label = dict()
        self.__color = None

    @property
    def score(self):
        return self.__score

    @property
    def coordinates(self):
        return self.__coordinates

    @property
    def label(self):
        return self.__label

    @property
    def color(self):
        return self.__color

    @score.setter
    def score(self, score):
        self.__score = score

    @coordinates.setter
    def coordinates(self, coordinates):
        self.__coordinates = tuple(coordinates)

    @label.setter
    def label(self, label):
        self.__label['class_name'] = label
        # self.__label['class_name'] = utils.breed_dict[label]

    @color.setter
    def color(self, color):
        self.__color = tuple([int(i * 255) for i in color[:3]])

    def add_label_data(self, d: ImageDraw, fnt):
        if self.score is not None:
            self.__label["display_text"] = '%s: %.2f' % (self.label["class_name"], self.score)
        else:
            self.__label["display_text"] = '%s: ans' % (self.label["class_name"])

        label_size = d.textsize(self.__label["display_text"], font=fnt)
        self.__label["size"] = label_size
        self.__label["coordinate"] = (
            self.__coordinates[0],
            self.__coordinates[1]
        )
