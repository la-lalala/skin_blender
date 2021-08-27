# BaseBumpテクスチャの皺をBaseColorテクスチャにブレンドするやつ（仮称）

## 概要
* BaseBumpテクスチャの皺をBaseColorテクスチャにブレンドするやつ
* GUIは上手くいったら付けるけど可能性は低いよ、現状pythonが使える人だけ用
* 頓挫したら自然消滅するよ

##　事前準備
1. pythonの仮想環境ツールをインストール
```
pip install pipenv
pipenv install
```

## 使い方
0. 「ブレンド先のBaseColor」「ブレンド元のBaseBump」テクスチャを用意してパスを控える  
1. settings.json内のパスを設定  
    * 二つ並んでるパスは前が「ブレンド先のBaseColor」後が「ブレンド元のBaseBump」  

2. 実行
```
pipenv shell
python skin_blender.py
```

3. outputs/wrinkle フォルダにブレンド後のテクスチャが出力される

## やりたいこと
* もっといい感じに皺を抽出したい
* 逆にBaseColorの「皺を除いた濃淡」を抽出したい（ローパスフィルタ？）
