import os, time
from utils import run_ffmpeg
from config import DOWNLOAD_DIR

async def process_link(link, index):
    filename = f"Video_{index}.mp4"
    out = os.path.join(DOWNLOAD_DIR, filename)

    start = time.time()
    ok = run_ffmpeg(link, out)
    end = time.time()

    if ok:
        return out, round(end-start, 2)
    return None, None
  
