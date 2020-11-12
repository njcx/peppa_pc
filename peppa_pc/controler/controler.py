import argparse

usage ="""
usage: peppa_pc.py [-h] [-f TARGET_FILE | -t TARGET] [-p POC] [-T THREADS]
                   [-m MODE]

optional arguments:
  -h, --help            Show help message and exit
  -f TARGET_FILE, --target_file TARGET_FILE
                        target url or host (e.g. "/tmp/target.txt")
  -t TARGET, --target TARGET
                        target url or host (e.g. "https://www.google.com/" or "192.168.0.1" or  "192.168.0.1/24" )
  -p POC, --poc POC     poc_file  (e.g. "pocs/01-dz-sqli.py" or "all" ) 
  -T THREADS, --threads THREADS
                        max number of process, default cpu number
  -m MODE, --mode MODE  verify or attack (e.g. "verify"), default "verify"
"""


def run(option):
    pass


def option():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, add_help=False)

    parser.add_argument("-h", "--help", action="help",
                        help="Show help message and exit")

    group = parser.add_mutually_exclusive_group()

    group.add_argument("-f", "--target_file",
                        help="target url or host (e.g. \"/tmp/target.txt\")")

    group.add_argument("-t", "--target",
                        help="target url or host (e.g. \"https://www.google.com/\" or"
                             " \"192.168.0.1\" or  \"192.168.0.1/24\" )")

    parser.add_argument("-p", "--poc",
                        help="poc_file  (e.g. \"pocs/01-dz-sqli.py\" or \"all\") ")

    parser.add_argument("-T", "--threads",
                        help="max number of process, default cpu number")

    parser.add_argument("-m", "--mode",
                        help="verify or attack (e.g. \"verify\"), default \"verify\"")

    args = parser.parse_args()
    try:
        if sum(map(lambda a: a or 0, args.__dict__.values())) == 0:
            print(usage)
            
    except Exception as e:

        return args.__dict__

