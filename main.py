"""make.fun news-image-20261122 entry: writes the front page for Sunday 22 November 2026.

The page is drawn ahead of time by art/draw.py (Pillow) and committed as entry.png;
this program, standard library only and offline, copies those exact bytes to the
output folder, so both runs write the same file.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"), os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
