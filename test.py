from main import select_distinct_frames
from config import Configs

sf = select_distinct_frames(Configs.SFRAME_PATH, Configs.GROUND_INDEX, target=Configs.TARGET_DIR)