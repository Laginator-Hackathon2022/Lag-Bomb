"""PRESENTATION VERSION - NOT FUNCTIONING"""

# Importinator
import webbrowser
from guizero import App, Text
# import zipfile
# import os
# import shutil
# import argparse
from urllib import request

"""THE LAGINATOR - Introducing Lag ...3...2...1..."""

#######################################################################################################

"""Downloads a random file repeatedly from Google"""

def downloadinator():
    while True:
        """Define the remote file to retrieve"""

        remote_url = 'https://www.google.com/robots.txt'

        """Define the local filename to save data"""

        local_file = 'local_copy.txt'

        """Download remote and save locally"""

        request.urlretrieve(remote_url, local_file)

        break

#######################################################################################################

"""Opens file of Rick Astley's Never Gonna Give You Up lyrics and downloads it repeatedly."""

def never_gonninator():
    y = 0
    never = open("nevergonna.txt", "r")
    while True:
        never_file = open(f"nevergonna{y}.txt", "a")
        y = y + 1
        never_file.writelines(never)
        break

#######################################################################################################

"""Writes the starwars scripts (40,000 lines) repeatedly into a txt file."""

def starwars_scriptinator():
    x = 0
    starwarsscript = open("starwars.txt", "r")
    while True:
        new_file = open(f"Starwars{x}.txt", "a")
        x = x + 1
        new_file.writelines(starwarsscript)
        break

#######################################################################################################

"""YOOOOO IT IS THE FAMILY GUY"""

def family_guyinator():
    while True:
        webbrowser.open('https://www.youtube.com/watch?v=K467F4ot0ek')
        break

#######################################################################################################

"""MEMES!!!!"""

def memeinator():
    while True:
        webbrowser.open('https://www.youtube.com/watch?v=nurpA9ra8_8')
        webbrowser.open('https://www.youtube.com/watch?v=eaEMSKzqGAg')
        webbrowser.open('https://www.youtube.com/watch?v=rZAeAaiMq5Y')
        webbrowser.open('https://www.youtube.com/watch?v=vEqtH8EWsIg')
        webbrowser.open('https://www.youtube.com/watch?v=Upsm3E2NUI8')
        webbrowser.open('https://www.youtube.com/watch?v=xZlVuJE28G8')
        webbrowser.open('https://www.youtube.com/watch?v=QZWjtHqLkdM')
        webbrowser.open('https://www.youtube.com/watch?v=kvmxKN_2r9A')
        webbrowser.open('https://www.youtube.com/watch?v=TXhhiz3lR8U')
        webbrowser.open('https://www.youtube.com/watch?v=HtE9CBGaKf4')
        webbrowser.open('https://www.youtube.com/watch?v=l51bHZIVMso')
        webbrowser.open('https://www.youtube.com/watch?v=0WMYL6HuUoI')
        webbrowser.open('https://www.youtube.com/watch?v=1RqzKsZCeEc')
        break

#######################################################################################################

"""Get Rickrolled"""

def rick_rollinator():
    while True:
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        break

    app = App(title="Rick Rollinator")
    text = Text(app, text="YOU GOT RICKROLLED", size=35, color="Red")
    rick_rollinator = "You got RickRolled"
    print(rick_rollinator)

    while True:
        app.display()
        break

#######################################################################################################

starwars_scriptinator()
rick_rollinator()

#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################

# def zip_bombinator(): #DO NOT RUN FUNCTION
#     """2MB of compressed data = 1TB decompressed"""
#
#     def generate_dummy_file(filename, size):
#         with open(filename, 'w') as dummy:
#             dummy.write((size * 1024 * 1024) * '0')
#
#     def make_copies_and_compress(zf, infile, n_copies):
#         for i in range(n_copies):
#             extensionator = infile[infile.rfind('.') + 1:]
#             basename = infile[:infile.rfind('.')]
#             f_name = '%s-%d.%s' % (basename, i, extensionator)
#             shutil.copy(infile, f_name)
#             zf.write(f_name, compress_type=zipfile.ZIP_DEFLATED)
#             os.remove(f_name)
#
#     def add_file_to_zip(zf, path, include_dir=True):
#         """Add directory to zip file"""
#         if os.path.isfile(path):
#             zf.write(path, compress_type=zipfile.ZIP_DEFLATED)
#         elif os.path.isdir(path):
#             for root, dirs, files in os.walk(path):
#                 arc_root = root
#                 if not include_dir:
#                     arc_root = root[len(path):]
#                     if arc_root.startswith(os.sep):
#                         arc_root = arc_root[1:]
#                 for file in files:
#                     zf.write(os.path.join(root, file), arcname=os.path.join(arc_root, file))
#
#     def make_zip_flat(size, out_file, include_dirs, include_files):
#         """
#         Creates flat zip file without nested zips.
#         Zip contains n files each of size size/n and is saved in out_file.
#         """
#         dummy_name_format = 'dummy{}.txt'
#
#         files_nb = int(size / 100)
#         file_size = int(size / files_nb)
#         last_file_size = size - (file_size * files_nb)
#
#         if os.path.isfile(out_zip_file):
#             os.remove(out_zip_file)
#
#         zf = zipfile.ZipFile(out_file, mode='w', allowZip64=True)
#
#         # Include selected dirs
#         for f in include_dirs:
#             add_file_to_zip(zf, f, include_dir=False)
#         for f in include_files:
#             add_file_to_zip(zf, f)
#
#         # Generate and add dummy big files
#         if files_nb > 0:
#             for i in range(files_nb):
#                 dummy_name = dummy_name_format.format(i)
#                 if i == 0:
#                     generate_dummy_file(dummy_name, file_size)
#                 else:
#                     os.rename(dummy_name_format.format(i - 1), dummy_name)
#                 zf.write(dummy_name, compress_type=zipfile.ZIP_DEFLATED)
#             os.remove(dummy_name)
#
#         if last_file_size > 0:
#             dummy_name = dummy_name_format.format(files_nb)
#             generate_dummy_file(dummy_name, last_file_size)
#             zf.write(dummy_name, compress_type=zipfile.ZIP_DEFLATED)
#             os.remove(dummy_name)
#         zf.close()
#         return files_nb * file_size
#
#     def get_files_depth_and_size(total_size):
#         files_nb = 1
#         file_size = 10
#         actual_size = files_nb ** files_nb * file_size
#         while actual_size < total_size:
#             # depth
#             inc_files_nb = files_nb + 1
#             if inc_files_nb ** inc_files_nb * file_size < total_size:
#                 files_nb = inc_files_nb
#             # file size
#             new_file_size = int(total_size / (files_nb ** files_nb))
#             if new_file_size > 2 * file_size:
#                 file_size *= 2
#             elif new_file_size == file_size:
#                 file_size += 1
#             else:
#                 file_size = new_file_size
#             actual_size = files_nb ** files_nb * file_size
#         return files_nb, file_size
#
#     def make_zip_nested(size_MB, out_zip_file, include_dirs, include_files):
#         """
#         Creates nested zip file (zip file of zip files of zip files etc.).
#         """
#         if size_MB < 500:
#             print('Warning: too small size, using flat mode.')
#             return make_zip_flat(size_MB, out_zip_file)
#
#         depth, file_size = get_files_depth_and_size(size_MB)
#         actual_size = depth ** depth * file_size
#         print('Warning: Using nested mode. Actual size may differ from given.')
#
#         # Prototype zip file
#         dummy_name = 'dummy.txt'
#         generate_dummy_file(dummy_name, file_size)
#         zf = zipfile.ZipFile('1.zip', mode='w', allowZip64=True)
#         zf.write(dummy_name, compress_type=zipfile.ZIP_DEFLATED)
#         zf.close()
#         os.remove(dummy_name)
#
#         for i in range(1, depth + 1):
#             zf = zipfile.ZipFile('%d.zip' % (i + 1), mode='w', allowZip64=True)
#             make_copies_and_compress(zf, '%d.zip' % i, depth)
#             os.remove('%d.zip' % i)
#             if i == depth:
#                 # Include selected dirs
#                 for f in include_dirs:
#                     add_file_to_zip(zf, f, include_dir=False)
#                 for f in include_files:
#                     add_file_to_zip(zf, f)
#             zf.close()
#         if os.path.isfile(out_zip_file):
#             os.remove(out_zip_file)
#         os.rename('%d.zip' % (depth + 1), out_zip_file)
#         return actual_size
#
#     def help_epilog():
#         return """mode of compression options:
#          flat - flat zip file with contents
#          nested - nested zip file, zip of zips of zips ... (much smaller) """
#
#     def check_size(value):
#         ivalue = int(value)
#         if ivalue < 100:
#             raise argparse.ArgumentTypeError("%s is an invalid value (< 100)." % value)
#         return ivalue
#
#     def parser():
#         parser = argparse.ArgumentParser(description='Creates ZIP bomb archive.',
#                                          formatter_class=argparse.RawDescriptionHelpFormatter, epilog=help_epilog())
#         parser.add_argument('-d', '--dirs', action='store',
#                             help='add directory contents to ZIP file. multiple directories separated with comma',
#                             default='')
#         parser.add_argument('-f', '--files', action='store',
#                             help='add files (can be directory) to ZIP file. multiple files separated with comma',
#                             default='')
#         parser.add_argument('mode', help='mode of compression. see choices description below',
#                             choices=('flat', 'nested'))
#         parser.add_argument('size', help='decompression size in MB', type=check_size)
#         parser.add_argument('out_zip_file', help='path to destination file')
#
#         return parser.parse_args()
#
#     if __name__ == '__main__':
#
#         args = parser()
#
#         out_zip_file = args.out_zip_file
#
#         include_dirs = [d.strip() for d in args.dirs.strip().split(',') if d != '']
#         include_files = [d.strip() for d in args.files.strip().split(',') if d != '']
#
#         if args.mode == 'flat':
#             actual_size = make_zip_flat(args.size, out_zip_file, include_dirs, include_files)
#         else:
#             actual_size = make_zip_nested(args.size, out_zip_file, include_dirs, include_files)
#         print('Compressed File Size: %.2f KB' % (os.stat(out_zip_file).st_size / 1024.0))
#         print('Size After Decompression: %d MB' % actual_size)
