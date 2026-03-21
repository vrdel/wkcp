#!/usr/bin/env python3

import os
import sys

def main():
    args = sys.argv[1:]

    filemount = ""
    for a in args:
        if os.path.isfile(a) and a.startswith('/'):
            filemount = a

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

    # If a file was referenced via absolute path, mount its directory
    if filemount:
        dir_mount = os.path.dirname(filemount)
        cmd.extend(["-v", f"{dir_mount}:{dir_mount}:rw"])

    cmd.extend(["-t", "wkcp"])
    cmd.extend(args)

    # Execute the docker command, effectively replacing the current python process
    os.execvp("docker", cmd)

if __name__ == "__main__":
    main()
