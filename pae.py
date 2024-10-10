import shutil
import psutils

def check_disk_usage(disk):
    du = shutil.dish_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutils.cpu_percent(1)
    return usage < 75