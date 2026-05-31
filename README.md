# YouTube Playlist Downloader

Download all videos from a YouTube playlist at the highest available resolution.

## Requirements

- Python 3.10+
- ffmpeg (system-level, required for merging high-res video + audio)

## Setup

**1. Run the setup script** (creates a virtual environment and installs dependencies):

```bash
chmod +x setup.sh
./setup.sh
```

**2. Activate the virtual environment:**

```bash
source .venv/bin/activate
```

**3. Install ffmpeg** (if not already installed):

```bash
# macOS
brew install ffmpeg

# Ubuntu / Debian
sudo apt install ffmpeg
```

---

## Usage

```bash
python yt_playlist_downloader.py <playlist_url> [options]
```

### Examples

**Download a playlist at the highest resolution (default output: `./downloads`):**
```bash
python yt_playlist_downloader.py "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID"
```

**Save to a custom folder:**
```bash
python yt_playlist_downloader.py "YOUR_URL" -o ~/Videos/MyPlaylist
```

**Cap resolution at 1080p:**
```bash
python yt_playlist_downloader.py "YOUR_URL" --max-height 1080
```

**Combine options:**
```bash
python yt_playlist_downloader.py "YOUR_URL" -o ~/Videos -max-height 720
```

---

## Options

| Flag | Default | Description |
|------|---------|-------------|
| `url` | *(required)* | YouTube playlist URL |
| `-o`, `--output` | `./downloads` | Output directory |
| `--max-height` | *(none)* | Max video height in pixels (e.g. `1080`, `720`) |

---

## Output Structure

Videos are saved as:
```
<output_dir>/
└── <Playlist Title>/
    ├── 1 - Video Title.mp4
    ├── 2 - Video Title.mp4
    └── ...
```

---

## Notes

- Already-downloaded videos are skipped automatically — safe to re-run.
- Partial downloads are resumed automatically.
- Unavailable or private videos are skipped without stopping the whole playlist.
- Videos are saved as `.mp4` with embedded thumbnail and metadata.
