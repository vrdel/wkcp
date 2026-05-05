#!/usr/bin/env python3

import os
import sys


def host_timezone():
    if os.environ.get("TZ"):
        return os.environ["TZ"]

    try:
        with open("/etc/timezone", "r", encoding="utf-8") as fp:
            timezone = fp.read().strip()
            if timezone:
                return timezone
    except OSError:
        pass

    localtime = "/etc/localtime"
    if os.path.islink(localtime):
        zoneinfo_prefix = "/usr/share/zoneinfo/"
        target = os.path.realpath(localtime)
        if target.startswith(zoneinfo_prefix):
            return target[len(zoneinfo_prefix):]

    return None


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

    timezone = host_timezone()
    if timezone:
        cmd.extend(["-e", f"TZ={timezone}"])
    if os.path.exists("/etc/localtime"):
        cmd.extend(["-v", "/etc/localtime:/etc/localtime:ro"])
    if os.path.exists("/etc/timezone"):
        cmd.extend(["-v", "/etc/timezone:/etc/timezone:ro"])

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
