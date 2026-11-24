#!/usr/bin/env python3
"""Copy the news-image-20261124 entry into the harness output directory.

Prefers entry.png when it fits the 1 MiB limit, otherwise falls back to
entry.jpg. Source directory: MAKEFUN_BOT_DIR when set, else /bot when it
holds an entry file, else this script's own directory.
"""
import os
import shutil
import sys

LIMIT = 1048576


def repo_dir():
    env_dir = os.environ.get("MAKEFUN_BOT_DIR")
    if env_dir:
        return env_dir
    if os.path.exists("/bot/entry.png") or os.path.exists("/bot/entry.jpg"):
        return "/bot"
    return os.path.dirname(os.path.abspath(__file__))


def pick_source(directory):
    # PNG first: it is the lossless master; JPG is only the fallback when
    # the PNG would bust the harness size limit.
    png = os.path.join(directory, "entry.png")
    jpg = os.path.join(directory, "entry.jpg")
    if os.path.exists(png) and os.path.getsize(png) <= LIMIT:
        return png
    if os.path.exists(jpg):
        return jpg
    return None


def main():
    src = pick_source(repo_dir())
    if src is None:
        print("no entry file found", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, os.path.basename(src))
    shutil.copyfile(src, dst)
    n = os.path.getsize(dst)
    print("copied {} -> {} ({} bytes)".format(src, dst, n))
    return 0


if __name__ == "__main__":
    sys.exit(main())
