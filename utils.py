import subprocess, os
from config import HEADERS

FFMPEG_PATH = "./ffmpeg" if os.path.exists("./ffmpeg") else "ffmpeg"

def run_ffmpeg(m3u8, out_file):
    os.makedirs(os.path.dirname(out_file), exist_ok=True)

    cmd = [
        FFMPEG_PATH, "-y",
        "-loglevel", "error",
        "-stats",
        "-headers", HEADERS,
        "-i", m3u8,
        "-c", "copy",
        "-bsf:a", "aac_adtstoasc",
        out_file
    ]

    p = subprocess.run(cmd)
    return p.returncode == 0 and os.path.exists(out_file)
