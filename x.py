#!/usr/bin/python3

import subprocess
#cmd_dnames="docker ps --format '{{.Names}}'"
cmd_dnames="hostname"
cmd=subprocess.Popen(cmd_dnames, shell=True, stderr=subprocess.PIPE)
(output, err) = cmd.communicate()
print output
