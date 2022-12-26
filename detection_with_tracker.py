import argparse
from typing import List, Optional, Union

import numpy as np
import torch

import norfair
from norfair import Detection, Paths, Tracker, Video

DISTANCE_THRESHOLD_BBOX: float = 0.7
DISTANCE_THRESHOLD_CENTROID: int = 30
MAX_DISTANCE: int = 10000


class YOLO:
    def __init__(self, model_name: str, device: Optional[str] = None):
        if device is not None and "cuda" in device and not torch.cuda.is_available():
            raise Exception(
                "Selected device='cuda', but cuda is not available to Pytorch."
            )
        # automatically set device if its None
        elif device is None:
            device = "cuda:0" if torch.cuda.is_available() else "cpu"

        # load model
        self.model = torch.hub.load("ultralytics/yolov5", model_name, device=device)

    def __call__(
        self,
        img: Union[str, np.ndarray],
        conf_threshold: float = 0.25,
        iou_threshold: float = 0.45,
        image_size: int = 720,
        classes: Optional[List[int]] = None,
    ) -> torch.tensor:

        self.model.conf = conf_threshold
        self.model.iou = iou_threshold
        if classes is not None:
            self.model.classes = classes
        detections = self.model(img, size=image_size)
        return detections


def center(points):
    return [np.mean(np.array(points), axis=0)]


def yolo_detections_to_norfair_detections(
    yolo_detections: torch.tensor # bbox or centroid
) -> List[Detection]:
    """convert detections_as_xywh to norfair detections"""
    norfair_detections: List[Detection] = []

    detections_as_xyxy = yolo_detections.xyxy[0]
    for detection_as_xyxy in detections_as_xyxy:
        bbox = np.array(
            [
                [detection_as_xyxy[0].item(), detection_as_xyxy[1].item()],
                [detection_as_xyxy[2].item(), detection_as_xyxy[3].item()],
            ]
        )
        scores = np.array(
            [detection_as_xyxy[4].item(), detection_as_xyxy[4].item()]
        )
        norfair_detections.append(
            Detection(
                points=bbox, scores=scores, label=int(detection_as_xyxy[-1].item())
            )
        )

    return norfair_detections


parser = argparse.ArgumentParser(description="Track objects in a video.")
parser.add_argument("files", type=str, nargs="+", help="Video files to process")
parser.add_argument(
    "--model-name", type=str, default="yolov5m6", help="YOLOv5 model name"
)


parser.add_argument(
    "--device", type=str, default=None, help="Inference device: 'cpu' or 'cuda'"
)

args = parser.parse_args()

model = YOLO(args.model_name, device=args.device)

for input_path in args.files:
    video = Video(input_path=input_path)

    distance_function = "iou_opt"
    distance_threshold = (
        DISTANCE_THRESHOLD_BBOX

    )

    tracker = Tracker(
        distance_function=distance_function,
        distance_threshold=distance_threshold,
    )

    for frame in video:
        yolo_detections = model(
            frame,
            conf_threshold=0.25,
            iou_threshold=0.45,
            image_size=720,
            classes=(39,41)
        )
        detections = yolo_detections_to_norfair_detections(
            yolo_detections
        )
        tracked_objects = tracker.update(detections=detections)
        # if args.track_points == "centroid":
        #     norfair.draw_points(frame, detections)
        #     norfair.draw_tracked_objects(frame, tracked_objects)
        # elif args.track_points == "bbox":
        norfair.draw_boxes(frame, detections)
        norfair.draw_tracked_boxes(frame, tracked_objects,draw_labels=True  )
        video.write(frame)