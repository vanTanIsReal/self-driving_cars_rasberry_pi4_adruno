import cv2
import math

def draw_steering_gauge(img, angle, center, radius):
    cv2.ellipse(img, center, (radius, radius), 180, 0, 180, (200,200,200), 2)

    angle_rad = math.radians(angle)
    end_x = int(center[0] + radius * math.sin(angle_rad))
    end_y = int(center[1] - radius * math.cos(angle_rad))

    color = (0,255,0) if abs(angle)<15 else (0,255,255) if abs(angle)<35 else (0,0,255)
    cv2.line(img, center, (end_x, end_y), color, 4)