import copy
import cv2
import json
import numpy as np
import os
from pathlib import Path

SETTINGS_FILE = "settings.json"
TOCHU_PATH = "outputs/tochu"
WRINCLE_PATH = "outputs/wrinkle"

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def blend_imgs(base_path, mask_path):
    outfile_name = f"{os.path.splitext(os.path.basename(base_path))[0]}.png"
    outfile_name2 = f"{os.path.splitext(os.path.basename(base_path))[0]}2.png"

    base_img = cv2.imread(base_path)
    blend_img = copy.deepcopy(base_img)
    mask_img = cv2.imread(mask_path)

    if base_img is None:
        print(f"{base_path}が存在しない")
    if mask_img is None:
        print(f"{mask_path}が存在しない")
    if base_img is None or mask_img is None:
        return

    # 脱色
    b, g, r = cv2.split(mask_img)
    mask_img = (0.299*r + 0.587*g + 0.114*b).astype(np.uint8)

    # 反転
    mask_img =  cv2.bitwise_not(mask_img)
    # 正規化
    mask_img = cv2.equalizeHist(mask_img)

    # ガンマ補正
    gamma = 6
    x = np.arange(256)
    y = (x / 255) ** gamma * 255
    mask_img = cv2.LUT(mask_img, y)
    mask_img = cv2.cvtColor(mask_img.astype(np.uint8), cv2.COLOR_GRAY2BGR) / 255 * 0.5
    cv2.imwrite(os.path.join(TOCHU_PATH, outfile_name), mask_img)

    # 輝度-20
    blend_img = blend_img - 20

    # 重ねる
    base_img = (base_img * (1.0 - mask_img) + blend_img * mask_img).astype(np.uint8)

    # 出力
    cv2.imwrite(os.path.join(WRINCLE_PATH, outfile_name), base_img)

if __name__ == '__main__':
    settings = load_json(SETTINGS_FILE)

    targets = settings["target_paths"]
    for k in targets:
        blend_imgs(
            targets[k][0],
            targets[k][1]
        )
