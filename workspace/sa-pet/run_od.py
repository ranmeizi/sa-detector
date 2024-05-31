import numpy as np
import cv2
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils

# 加载保存的模型
model = tf.saved_model.load('exported-models/ssd_sa/saved_model')

# 加载标签映射文件
label_map_path = 'annotations/pet_map_v0.pbtxt'
category_index = label_map_util.create_category_index_from_labelmap(label_map_path, use_display_name=True)

# 加载图像
image_path = 'images/pet/train/8061715405934_.pic_hd.jpg'
image_np = cv2.imread(image_path)
image_resized = cv2.resize(image_np, (640, 640), interpolation=cv2.INTER_AREA)
input_tensor = tf.convert_to_tensor(np.expand_dims(image_resized, 0), dtype=tf.float32)

# 进行检测
detections = model(input_tensor)

# 获取检测结果
num_detections = int(detections.pop('num_detections'))
detection_classes = detections['detection_classes'][0].numpy()
detection_boxes = detections['detection_boxes'][0].numpy()
detection_scores = detections['detection_scores'][0].numpy()

# 可视化检测结果
viz_utils.visualize_boxes_and_labels_on_image_array(
    image_np,
    detection_boxes,
    detection_classes,
    detection_scores,
    category_index,
    use_normalized_coordinates=True,
    max_boxes_to_draw=200,
    min_score_thresh=.30,
    agnostic_mode=False)

# 显示图像
cv2.imshow('Object Detection', image_np)
cv2.waitKey(0)
cv2.destroyAllWindows()