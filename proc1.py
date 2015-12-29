
def check_status(self):
    # each of these is a process I want to make sure they are running.
    status = {
        'pm' : False,
        'om' : False,
        'dm' : False,
        'redis' : False,
    }
    cmd = "sudo %s/foo status" % config.FOO_TOOLS
    output = subprocess.check_output(cmd, shell=True)
    print output
    for k, v in status.iteritems():
        print k

proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
# skip [WARN]
proc.stdout.readline()
# look for interesting data in remaining
for line in proc.stdout:
    # terminate after processing the [INFO] section
    if line.startswith('[INFO] :  redis'):
        status['redis'] = True
        for line in proc.stdout:
            pass
        break
    # get the process status
    name, remaining = line.split(' ', 1):
    if name in status:
        status[name] = not 'Not running' in remaining
proc.wait()
