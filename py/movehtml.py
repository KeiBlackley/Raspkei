#!/usr/bin/env python3
import shutil
import os
import sys

src = os.path.expanduser('/home/kei/Raspkei/web')
dest = '/var/www/html'

try:
    # Remove destination if it exists
    if os.path.exists(dest):
        shutil.rmtree(dest)
    # Copy source to destination
    shutil.copytree(src, dest)
    print(f"Moved {src} to {dest}")
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
