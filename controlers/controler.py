import numpy as np
import torch

from model.ssd import SSD
from model.image import SsdImage, BBox
from utils import utils
import settings


class SSDPredictModel(object):
    def __init__(self, binary_data, data_confidence_level=settings.confidence_level,
                 font=str(settings.BASE_DIR / "fonts/Helvetica.ttc")):
        self.data_confidence_level = data_confidence_level
        self.net = SSD(phase='inference', cfg=utils.ssd_cfg)
        self.net_weight = torch.load(settings.BASE_DIR / f'weights/{settings.weight_file}',
                                     map_location={'cuda:0': 'cpu'})
        self.net.load_state_dict(self.net_weight)
        self.img = SsdImage(binary_data=binary_data)
        self.target = None
        self.font = font

    @property
    def predict(self):
        self.img.transform()
        self.target = torch.from_numpy(self.img.target[:, :, (2, 1, 0)]).permute(2, 0, 1)

        self.net.eval()
        x = self.target.unsqueeze(0)
        detections = self.net(x)

        # confidence_levelが基準以上を取り出す
        detections = detections.cpu().detach().numpy()

        # 条件以上の値を抽出
        find_index = np.where(detections[:, 0:, :, 0] >= self.data_confidence_level)
        detections = detections[find_index]
        for i in range(len(find_index[1])):  # 抽出した物体数分ループを回す
            if (find_index[1][i]) > 0:  # 背景クラスでないもの
                bbox = BBox()

                bbox.score = detections[i][0]  # 確信度
                bbox.coordinates = detections[i][1:] * [self.img.width, self.img.height, self.img.width,
                                                        self.img.height]
                # find_indexはミニバッチ数、クラス、topのtuple
                inx = find_index[1][i] - 1
                bbox.label = utils.voc_classes[inx]
                bbox.color = utils.color_cfg[inx]
                # （注釈）
                # 背景クラスが0なので1を引く

                self.img.bbox_list.append(bbox)

        self.img.attach_bbox(fnt=self.font)

        return self.img.get_origin(binary=True)
