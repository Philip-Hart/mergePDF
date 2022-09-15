# MergePDF: A command line tool for merging PDFs

### Requirements:
1. PyPDF2
Since this is a simple script with one dependency, PyPDF2 may be installed globally using:
> pip install PyPDF2

### Details:
Move merge.py to the directory where you would like to merge pdfs. 
Pdfs you want to merge need to be organized within their own folder
There are two user inputs required: one for where the pdfs you would like to merge are stored, and one where you would like the merged pdf to be stored. I have included examples of appropriate inpute below.
1. Defining the input path:
> Insert path to pdfs as [dir]/ (Must be in parent dir of [dir]: **2022_pdfs/**  
or 
> Insert path to pdfs as [dir]/ (Must be in parent dir of [dir]: **2022/Fall_pdfs/**  

2. Defining the ouput path: 
> Insert output path as [dir]/[pdf_name].pdf (Must be in parent dir of [dir]): */merged_entries.pdf  
or   
> Insert output path as [dir]/[pdf_name].pdf (Must be in parent dir of [dir]): */2022/Fall_pdfs/merged_entries.pdf  
Note: The first example will save the merged pdf in the same directory as where you placed merge.py. The second example illustrates recursively creating a path that previously does not exist in your file system. Using a directory that is already created will also work. 

