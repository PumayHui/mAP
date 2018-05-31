import sys
import os
import glob
import json
import shutil


if not os.path.exists("../true"):
  os.makedirs("../true")

if not os.path.exists("../pred"):
  os.makedirs("../pred")

if not os.path.exists("../img"):
  os.makedirs("../img")

pred_data = json.load(open("../json/save.ckpt-1000000.brainwash_test.json"))
for pred_obj in pred_data:
  shutil.copy(pred_obj['image_path'], '../img')
  # tmp_file = '../pred/' + pred_obj['image_path'].split('/')[1]
  tmp_file = '../pred/' + pred_obj['image_path'].split('\\')[3]
  with open(tmp_file.replace(".jpg", ".txt"), "a") as new_f:
    for obj in pred_obj['rects']:
      obj_name = 'head'
      conf = obj['score']
      left = obj['x1']
      top = obj['y1']
      right = obj['x2']
      bottom = obj['y2']
      new_f.write(obj_name + " " + str(conf) + " " + str(left) + " " + str(top) + " " + str(right) + " " + str(bottom) + '\n')
    print("%s Conversion completed!" % obj_name)

true_data = json.load(open("../json/save.ckpt-1000000.gt_brainwash_test.json"))
for true_obj in true_data:
  # tmp_file = '../true/' + true_obj['image_path'].split('/')[1]
  tmp_file = '../true/' + true_obj['image_path']
  with open(tmp_file.replace(".jpg", ".txt"), "a") as new_f:
    for obj in true_obj['rects']:
      obj_name = 'head'
      left = obj['x1']
      top = obj['y1']
      right = obj['x2']
      bottom = obj['y2']
      new_f.write(obj_name + " " + str(left) + " " + str(top) + " " + str(right) + " " + str(bottom) + '\n')
    print("%s Conversion completed!" % obj_name)
