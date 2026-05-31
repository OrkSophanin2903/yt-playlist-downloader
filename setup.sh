#!/usr/bin/env bash
set -e

echo "[1/4] Creating virtual environment..."
python3 -m venv .venv

echo "[2/4] Activating virtual environment..."
source .venv/bin/activate

echo "[3/4] Installing Python dependencies..."
pip install --upgrade pip -q
pip install -r requirements.txt

echo "[4/4] Checking for ffmpeg..."
if ! command -v ffmpeg &> /dev/null; then
    echo ""
    echo "[WARNING] ffmpeg is not installed. High-resolution downloads require it."
    echo "  macOS  : brew install ffmpeg"
    echo "  Ubuntu : sudo apt install ffmpeg"
else
    echo "  ffmpeg found: $(ffmpeg -version 2>&1 | head -n1)"
fi

echo ""
echo "[DONE] Environment ready!"
echo "To activate: source .venv/bin/activate"
echo "To run     : python yt_playlist_downloader.py <playlist_url>"
