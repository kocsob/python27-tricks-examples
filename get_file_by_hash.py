import hashlib
import argparse
import os
import shutil
import sys

default_search_dir = os.getcwd()
parser = argparse.ArgumentParser(description='Get file by hash value in directory')
parser.add_argument('hash', action = 'store', help = "Hash value")
parser.add_argument('-s', '--searchdir', action = 'store', default = default_search_dir, help = "Search directory (default: %s)" % default_search_dir)
parser.add_argument('-c', '--copy', action = 'store', default = None, help = "Copy file in the directory")
args = parser.parse_args()

hash = args.hash.upper()
if len(hash) == 32:     # MD5 digest size is 16 bytes (32 hex digits)
    hash_function = hashlib.md5
elif len(hash) == 40:   # SHA1 digest size is 20 bytes (40 hex digits)
    hash_function = hashlib.sha1
elif len(hash) == 56:   # SHA224 digest size is 28 bytes (56 hex digits)
    hash_function = hashlib.sha224
elif len(hash) == 64:   # SHA256 digest size is 32 bytes (64 hex digits)
    hash_function = hashlib.sha256
elif len(hash) == 98:   # SHA384 digest size is 48 bytes (98 hex digits)
    hash_function = hashlib.sha384
elif len(hash) == 128:  # SHA512 digest size is 64 bytes (128 hex digits)
    hash_function = hashlib.sha512
else:
    print "Not supported hash type."
    sys.exit(1)

for (dirpath, dirnames, filenames) in os.walk(args.searchdir):
    for filename in filenames:
        hasher = hash_function()
        file_path = os.path.join(dirpath, filename)
        with open(file_path, 'rb') as fopen:
            for chunk in iter(lambda: fopen.read(128 * hasher.block_size), b''):
                hasher.update(chunk)
            if (hasher.hexdigest().upper() == hash):
                print "File found on the path: %s" % (file_path)
                if args.copy is not None: 
                    shutil.copyfile(file_path, os.path.join(args.copy, filename))
                sys.exit(0)