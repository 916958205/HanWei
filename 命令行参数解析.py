import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--length",default=10,type=int,help="changdu")
parser.add_argument("--width",default=5,type=int,help="kuandu")
args = parser.parse_args()
area = args.length * args.width
print ("mianji=",area)