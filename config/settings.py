import os
os.environ['OPENBLAS_CORETYPE'] = 'ARMV8'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LANE_MODEL_PATH = "/home/tuan/code/seg_ncnn_model"
OBJ_MODEL_PATH = "/home/tuan/code/detect_ncnn_model"

IMG_SIZE = 320
FRAME_WIDTH = 320
FRAME_HEIGHT = 240

SERIAL_PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600

SKIP_FRAMES = 2