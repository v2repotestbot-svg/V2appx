#!/bin/bash

echo "Downloading ffmpeg..."
curl -L -o ffmpeg.tar.xz https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz
tar -xf ffmpeg.tar.xz
cd ffmpeg-*-static
cp ffmpeg ../ffmpeg
cd ..
chmod +x ffmpeg
echo "ffmpeg ready"

