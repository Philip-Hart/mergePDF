from PyPDF2 import PdfFileMerger
import os

merger = PdfFileMerger()

#path_to_files = r'pdfs/'
path_to_files = input('\nInsert path to pdfs as [dir]/ (Must be in parent dir of [dir]: ')

for root, dirs, file_names in os.walk(path_to_files):
    file_names.sort()
    for file_name in file_names:
        merger.append(path_to_files + file_name)

output_path = input('\nInsert output path as [dir]/[pdf_name].pdf (Must be in parent dir of [dir]): ')
dir_path = output_path.rsplit("/", 1)[0]
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

merger.write(output_path)
merger.close

