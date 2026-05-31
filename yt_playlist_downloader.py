#!/usr/bin/env python3

import argparse
import subprocess
import sys
import shutil


def check_dependencies():
    missing = []
    if not shutil.which("yt-dlp"):
        missing.append("yt-dlp")
    if not shutil.which("ffmpeg"):
        missing.append("ffmpeg")
    if missing:
        print(f"[ERROR] Missing required tools: {', '.join(missing)}")
        print()
        print("Install them with:")
        if "yt-dlp" in missing:
            print("  pip install yt-dlp")
        if "ffmpeg" in missing:
            print("  brew install ffmpeg       # macOS")
            print("  sudo apt install ffmpeg   # Ubuntu/Debian")
        sys.exit(1)


def download_playlist(url: str, output_dir: str, max_height: int | None):
    format_selector = "bestvideo+bestaudio/best"
    if max_height:
        format_selector = f"bestvideo[height<={max_height}]+bestaudio/best[height<={max_height}]"

    output_template = f"{output_dir}/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s"

    cmd = [
        "yt-dlp",
        "--format", format_selector,
        "--merge-output-format", "mp4",
        "--output", output_template,
        "--no-overwrites",          # skip already downloaded
        "--continue",               # resume partial downloads
        "--ignore-errors",          # skip unavailable videos, don't abort
        "--progress",
        "--embed-thumbnail",
        "--embed-metadata",
        "--no-check-certificate",
        url,
    ]

    print(f"[INFO] Downloading playlist: {url}")
    print(f"[INFO] Output directory   : {output_dir}")
    if max_height:
        print(f"[INFO] Max resolution     : {max_height}p")
    else:
        print(f"[INFO] Resolution         : highest available")
    print()

    try:
        subprocess.run(cmd, check=True)
        print("\n[DONE] All downloads completed.")
    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] yt-dlp exited with code {e.returncode}")
        sys.exit(e.returncode)
    except KeyboardInterrupt:
        print("\n[ABORTED] Download cancelled by user.")
        sys.exit(0)


def main():
    parser = argparse.ArgumentParser(
        description="Download all videos from a YouTube playlist at the highest resolution."
    )
    parser.add_argument("url", help="YouTube playlist URL")
    parser.add_argument(
        "-o", "--output",
        default="./downloads",
        help="Output directory (default: ./downloads)",
    )
    parser.add_argument(
        "--max-height",
        type=int,
        default=None,
        metavar="HEIGHT",
        help="Limit resolution, e.g. 1080 for 1080p (default: no limit)",
    )

    args = parser.parse_args()

    check_dependencies()
    download_playlist(args.url, args.output, args.max_height)


if __name__ == "__main__":
    main()
