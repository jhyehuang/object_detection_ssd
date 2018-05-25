# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:22:30 2018

@author: admin
"""

# 本地运行训练
python object_detection/train.py --train_dir=D:/GitHub/object_detection_ssd/w8-data/output --pipeline_config_path=D:/GitHub/object_detection_ssd/models_r1.5/research/object_detection/ssd_mobilenet_v1_pets.config

#本地运行验证，注意这里的checkpoint就是训练时候的train_dir,验证的结果放在eval_dir，可以通过tensorboard看
python ./object_detection/eval.py --checkpoint_dir=D:/GitHub/object_detection_ssd/w8-data/output --eval_dir=D:/GitHub/object_detection_ssd/w8-data/eval_dir --pipeline_config_path=D:/GitHub/object_detection_ssd/models_r1.5/research/object_detection/ssd_mobilenet_v1_pets.config

# 导出训练好的模型，这里注意trained_checkpoint_prefix的参数是个前缀，不是一个文件名，这个参数代表的是三个文件以这个参数值开头的文件，最后的last_chekpoint_number是一个数字
python ./object_detection/export_inference_graph.py --input_type image_tensor --pipeline_config_path D:/GitHub/object_detection_ssd/models_r1.5/research/object_detection/ssd_mobilenet_v1_pets.config --trained_checkpoint_prefix D:/GitHub/object_detection_ssd/w8-data/output/model.ckpt-205 --output_directory D:/GitHub/object_detection_ssd/w8-data/exported_graphs

# 用导出的模型运行inference，详情参考代码
python ./object_detection/inference.py --output_dir=D:/GitHub/object_detection_ssd/w8-data --dataset_dir=D:/GitHub/object_detection_ssd/w8-data/data