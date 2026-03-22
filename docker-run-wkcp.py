#!/usr/bin/env python3

import os
import sys


def main():
    args = sys.argv[1:]

    filemounts = set()
    dirmounts = set()
    for a in args:
        if os.path.isfile(a) and a.startswith('/'):
            filemounts.add(os.path.dirname(a))
        if os.path.isdir(a) and a.startswith('/'):
            dirmounts.add(os.path.dirname(a))

    # Base docker run command arguments
    cmd = [
        "docker", "run",
        "--net", "host",
        "--rm",
        "-v", f"{os.getcwd()}:/work",
        "-w", "/work",
        "-e", f"DISPLAY={os.environ.get('DISPLAY', '')}",
        "-v", "/tmp/.X11-unix:/tmp/.X11-unix"
    ]

    # If files were referenced via absolute path, mount their directories
    for dir_mount in filemounts:
        cmd.extend(["-v", f"{dir_mount}:{dir_mount}:rw"])
    for dir_mount in dirmounts:
        cmd.extend(["-v", f"{dir_mount}:{dir_mount}:rw"])

    cmd.extend(["-t", "wkcp"])

    # Execute the docker command, effectively replacing the current python process
    os.execvp("docker", cmd + args)


if __name__ == "__main__":
    main()
