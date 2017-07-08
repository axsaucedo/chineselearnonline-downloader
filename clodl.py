
from urllib.request import urlretrieve
import sys, os, shutil

FOLDER="download"
TOTAL_LESSONS=420
AUDIO_EXT=".mp3"
FILE_EXT=".pdf"

def url_audio(name):
    return f"https://www.chineselearnonline.com/wp-content/uploads/ChineseLearnOnline_{name}{AUDIO_EXT}"

def url_vocab(name):
    return f"https://www.chineselearnonline.com/premium/CLO_{name}_Vocab.pdf"

def url_pinyin(name):
    return f"https://www.chineselearnonline.com/premium/CLO_{name}_Comp_P.pdf"

def url_simplified(name):
    return f"https://www.chineselearnonline.com/premium/CLO_{name}_Comp_S.pdf"

def url_traditional(name):
    return f"https://www.chineselearnonline.com/premium/CLO_{name}_Comp_T.pdf"

def url_english(name):
    return f"https://www.chineselearnonline.com/premium/CLO_{name}_Comp_E.pdf"

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
    files = os.listdir("FOLDER")
    numbers = [n for n in files if n.isdigit()]

    if not numbers:
        return 1

    nums = [int(n) for n in numbers]
    latest = max(nums)
    foldername = str(latest).zfill(3)

    # Remove the latest one as it may be incomplete / corrupted
    shutil.rmtree(foldername)

    return latest

def create_folder_if_not_exists(fname):
    if not os.path.exists(fname):
        return os.makedirs(fname)

def download_audio(num, base):

    name = str(num).zfill(3)

    print(f"Downloading {name}{AUDIO_EXT}")

    url = url_audio(name)

    BASE_FILE_URL_V=""

    urlretrieve(url, f"{folder_name}/{name}{AUDIO_EXT}", reporthook)

def download_files(num, folder_name):

    name = str(num).zfill(3)
    print(f"Downloading {name} files")
    v = url_vocab(name)
    p = url_pinyin(name)
    s = url_simplified(name)
    t = url_traditional(name)
    e = url_english(name)

    urlretrieve(v, f"{folder_name}/{name}_Vocab{FILE_EXT}", reporthook)
    urlretrieve(p, f"{folder_name}/{name}_Pinyin{FILE_EXT}", reporthook)
    urlretrieve(s, f"{folder_name}/{name}_Simplified{FILE_EXT}", reporthook)
    urlretrieve(t, f"{folder_name}/{name}_Traditional{FILE_EXT}", reporthook)
    urlretrieve(e, f"{folder_name}/{name}_English{FILE_EXT}", reporthook)

if __name__ == "__main__":

    create_folder_if_not_exists(FOLDER)

    start = start_previous_to_last()
    print(f"Starting from {start}")

    for i in range(start, TOTAL_LESSONS + 1):
        fname = str(num).zfill(3)
        base_folder = f"{FOLDER}/{fname}"

        download_audio(i, base_folder)
        download_files(i, base_folder)





