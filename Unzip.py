import gzip
import glob
import os.path
source_dir = "C:\Users\srinivasanravi\Downloads"
dest_dir = "C:\Users\srinivasanravi\Desktop"

for src_name in glob.glob(os.path.join(source_dir, '*.gz')):
    base = os.path.basename(src_name)
    dest_name = os.path.join(dest_dir, base[:-3])
    with gzip.open(src_name, 'rb') as infile:
        with open(dest_name, 'wb') as outfile:
            for line in infile:
                outfile.write(line)

