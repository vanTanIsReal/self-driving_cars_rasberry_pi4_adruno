from ultralytics import YOLO
from picamera2 import Picamera2
import time
import cv2

from config.settings import *
from perception.node_detection import detect_node_color
from perception.lane_detection import compute_steering
from perception.object_detection import detect_traffic_stop
from control.serial_comm import init_serial, send_control
from utils.visualization import draw_steering_gauge

def main():
    lane_model = YOLO(LANE_MODEL_PATH, task="segment")
    obj_model = YOLO(OBJ_MODEL_PATH, task="detect")

    ser = init_serial()

    picam2 = Picamera2()
    config = picam2.create_preview_configuration(main={"size": (FRAME_WIDTH, FRAME_HEIGHT)})
    picam2.configure(config)
    picam2.start()

    target_node = int(input("Target node: "))

    cam_x = FRAME_WIDTH // 2
    cam_y = FRAME_HEIGHT
    last_angle = 0

    while True:
        frame = picam2.capture_array()

        node = detect_node_color(frame)

        obj_results = obj_model(frame, imgsz=IMG_SIZE)
        stop, _ = detect_traffic_stop(obj_results, obj_model)

        lane_results = lane_model(frame, imgsz=IMG_SIZE)
        angle, target = compute_steering(lane_results[0].masks, cam_x, cam_y, last_angle)
        last_angle = angle

        send_control(ser, angle, not stop)

        draw_steering_gauge(frame, angle, (160,80), 60)
        cv2.imshow("car", frame)

        if cv2.waitKey(1) == ord('q'):
            break

if __name__ == "__main__":
    main()