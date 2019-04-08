#! /usr/bin/env python3

from duct import cmd, sh
import os
from pathlib import Path
import sys

here = Path(__file__).parent


def main():
    os.chdir(str(here))

    status = sh("git status --porcelain").read()
    if status:
        print("repo isn't clean")
        return 1

    cmd("git", "push", "origin", "master").run()

    cmd(
        "ssh",
        "jacko@jacko.io",
        "cd /srv/jacko.io && git pull --ff-only && peru sync --no-cache",
    ).run()


if __name__ == "__main__":
    sys.exit(main())
