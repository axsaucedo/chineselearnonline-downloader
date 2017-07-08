
from urllib.request import urlretrieve
import sys
import os

TOTAL_LESSONS=420
BASE_URL="https://www.chineselearnonline.com/wp-content/uploads/ChineseLearnOnline_"
EXT=".mp3"

def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %*d / %d" % (
            percent, len(str(totalsize)), readsofar, totalsize)
        sys.stderr.write(s)
        if readsofar >= totalsize: # near the end
            sys.stderr.write("\n")
    else: # total size is unknown
        sys.stderr.write("read %d\n" % (readsofar,))

def start_previous_to_last():
    files = os.listdir()
    names = ["".join(f.split(".")[:-1]) for f in files]
    numbers = [n for n in names if n.isdigit()]

    if not numbers:
        return 1

    nums = [int(n) for n in numbers]
    latest = max(nums)
    filename = str(latest).zfill(3)
    file = f"{filename}{EXT}"
    os.remove(file)
    return latest

def download_files(start, total):

    for i in range(start,total+1):
        name = str(i).zfill(3)

        print(f"Downloading {name}{EXT}")

        url = f"{BASE_URL}{name}{EXT}"

        urlretrieve(url, f"{name}{EXT}", reporthook)

if __name__ == "__main__":

    start = start_previous_to_last()
    print(f"Starting from {start}")

    download_files(start, TOTAL_LESSONS)




