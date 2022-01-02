SSD_portfolio
====

## 作成に至った経緯

SSD判定のアプリのモデルです。犬と猫の種類が判定できるモデルを作成しました。
本ポートフォリオは、SSDに題材を絞って作成しました。

### 例）柴犬を送った場合。

![predict_dog01](https://user-images.githubusercontent.com/52523218/113596446-481afb80-9675-11eb-959c-885a1fcc617c.jpg)

また、判定可能な犬と猫の種類は以下の通りです。

```
犬種（計２５種）
・american_bulldog（アメリカン・ブルドッグ）
・american_pit_bull_terrier（アメリカン・ピット・ブル・テリア）
・basset_hound（バセット・ハウンド）
・beagle（ビーグル）
・boxer（ボクサー）
・chihuahua（チワワ）
・english_cocker_spaniel（イングリッシュ・コッカー・スパニエル）
・english_setter（イングリッシュ・セター） 
・german_shorthaired（ジャーマン・ショートヘアード・ポインター）
・great_pyrenees（グレート・ピレニーズ）
・havanese（ハバニーズ）
・japanese_chin（狆）
・keeshond（キースホンド）
・leonberger（レオンベルガー） 
・miniature_pinscher（ミニチュア・ピンシャー）
・newfoundland（ニューファンドランド）
・pomeranian（ポメラニアン）
・pug（パグ）
・saint_bernard（セント・バーナード）
・samoyed（サモエド）
・scottish_terrier（スコティッシュ・テリア）
・shiba_inu（柴犬）
・staffordshire_bull_terrier（スタッフォードシャー・ブル・テリア）
・wheaten_terrier（ソフトコーテッド・ウィートン・テリア）
・yorkshire_terrier（ヨークシャー・テリア）

猫種（計１２種）
・Abyssinian（アビシニアン）
・Bengal（ベンガル）
・Birman（バーマン） 
・Bombay（ボンベイ） 
・British_Shorthair（ブリティッシュ・ショートヘア）
・Egyptian_Mau（エジプシャン・マウ）
・Maine_Coon（メインクーン）
・Persian（ペルシャ）
・Ragdoll（ラグドール）
・Russian_Blue（ロシアンブルー）
・Siamese（シャム）
・Sphynx（スフィンクス） 
```

## プロジェクト構成

SSD_projectのファイル構成は以下の通りです。

```tree
SSD_project
├── controlers
│   ├── __init__.py
│   └── controler.py
├── model
│   ├── __init__.py
│   ├── image.py
│   └── ssd.py
├── utils
│   ├── __init__.py
│   ├── data_augumentation.py
│   ├── match.py
│   └── utils.py
├── settings.py
├── app.py
│
├── fonts
│   ├── Helvetica.ttc
│   └── Hiragino_w4.ttc
├── logfiles
│   └── SSD_project.log
├── README.md
├── requirements.txt
├── settings.ini
└── weights
    └── ssd300_100.pth

```

## 使い方

1. このプロジェクトを試すには別途、[SSD_project_kit](https://github.com/ktaroabobon/SSD_portfolio_kit)
   が必要です。[こちら](https://github.com/ktaroabobon/SSD_portfolio_kit) からダウンロードしてください。

2. [SSD_project_kit](https://github.com/ktaroabobon/SSD_portfolio_kit) のダウンロードが完了したらapp.pyを実行してください。

```
cd SSD_portfolio
python app.py
```

## 注意点

初期設定ではポート番号が8080に設定されています。

## 著作者

・作成者：[ktaroabobon](https://github.com/ktaroabobon)
