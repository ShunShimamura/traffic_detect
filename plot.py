import pylab
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("result")
args = parser.parse_args()

xs = []
ys = []
for line in open(args.result):
    print line
    data = json.loads(line)
    xs.append(data["iteration"])
    ys.append(data["error"])
pylab.xlabel("iteration")
pylab.ylabel("error")
pylab.plot(xs, ys)
pylab.show()