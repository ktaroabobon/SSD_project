from matplotlib import cm
import numpy as np

voc_classes = [
    "Abyssinian", "american_bulldog", "american_pit_bull_terrier",
    "basset_hound", "beagle", "Bengal", "Birman", "Bombay", "boxer",
    "British_Shorthair", "chihuahua", "Egyptian_Mau", "english_cocker_spaniel",
    "english_setter", "german_shorthaired", "great_pyrenees", "havanese",
    "japanese_chin", "keeshond", "leonberger", "Maine_Coon", "miniature_pinscher",
    "newfoundland", "Persian", "pomeranian", "pug", "Ragdoll", "Russian_Blue",
    "saint_bernard", "samoyed", "scottish_terrier", "shiba_inu", "Siamese",
    "Sphynx", "staffordshire_bull_terrier", "wheaten_terrier", "yorkshire_terrier",
]

# SSD300の設定
ssd_cfg = {
    'num_classes': 38,  # 背景クラスを含めた合計クラス数
    'input_size': 300,  # 画像の入力サイズ
    'bbox_aspect_num': [4, 6, 6, 6, 4, 4],  # 出力するDBoxのアスペクト比の種類
    'feature_maps': [38, 19, 10, 5, 3, 1],  # 各sourceの画像サイズ
    'steps': [8, 16, 32, 64, 100, 300],  # DBOXの大きさを決める
    'min_sizes': [30, 60, 111, 162, 213, 264],  # DBOXの大きさを決める
    'max_sizes': [60, 111, 162, 213, 264, 315],  # DBOXの大きさを決める
    'aspect_ratios': [[2], [2, 3], [2, 3], [2, 3], [2], [2]],
}

color_cfg = cm.get_cmap('hsv')(np.linspace(0, 1, ssd_cfg['num_classes'] - 1)).tolist()

breed_dict = {
    "Abyssinian": "アビシニアン",
    "american_bulldog": "アメリカン・ブルドッグ",
    "american_pit_bull_terrier": "アメリカン・ピット・ブル・テリア",
    "basset_hound": "バセット・ハウンド",
    "beagle": "ビーグル", "Bengal": "ベンガル",
    "Birman": "バーマン", "Bombay": "ボンベイ", "boxer": "ボクサー",
    "British_Shorthair": "ブリティッシュ・ショートヘア", "chihuahua": "チワワ",
    "Egyptian_Mau": "エジプシャン・マウ", "english_cocker_spaniel": "イングリッシュ・コッカー・スパニエル",
    "english_setter": "イングリッシュ・セター", "german_shorthaired": "ジャーマン・ショートヘアード・ポインター",
    "great_pyrenees": "グレート・ピレニーズ", "havanese": "ハバニーズ",
    "japanese_chin": "狆（ちん）", "keeshond": "キースホンド",
    "leonberger": "レオンベルガー", "Maine_Coon": "メインクーン",
    "miniature_pinscher": "ミニチュア・ピンシャー",
    "newfoundland": "ニューファンドランド", "Persian": "ペルシャ",
    "pomeranian": "ポメラニアン", "pug": "パグ", "Ragdoll": "ラグドール", "Russian_Blue": "ロシアンブルー",
    "saint_bernard": "セント・バーナード", "samoyed": "サモエド", "scottish_terrier": "スコティッシュ・テリア",
    "shiba_inu": "柴犬", "Siamese": "シャム",
    "Sphynx": "スフィンクス", "staffordshire_bull_terrier": "スタッフォードシャー・ブル・テリア",
    "wheaten_terrier": "ソフトコーテッド・ウィートン・テリア", "yorkshire_terrier": "ヨークシャー・テリア",
}


def bbox_text_size(img_height, img_width: int) -> int:
    img_size = img_height * img_width
    text_size = 10

    if 300 * 300 < img_size and img_size <= 600 * 600:
        text_size = 20
    elif 600 * 600 < img_size and img_size <= 780 * 780:
        text_size = 30
    elif 780 * 780 < img_size:
        text_size = 36

    return text_size


def bbox_rectangle_width(img_height, img_width: int) -> int:
    img_size = img_height * img_width
    rectangle_width = 1

    if 300 * 300 < img_size and img_size <= 600 * 600:
        rectangle_width = 5
    elif 600 * 600 < img_size and img_size <= 780 * 780:
        rectangle_width = 8
    elif 780 * 780 < img_size:
        rectangle_width = 10

    return rectangle_width
