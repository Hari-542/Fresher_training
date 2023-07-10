from pypdf import PdfReader,PdfWriter,PdfMerger
from pathlib import Path
import pypdfium2 as pdfium
from PIL import Image
import copy

#merge pdf
curr_dir=Path.cwd() 
pdf_merger=PdfMerger()
for path in curr_dir.glob('*.pdf'):
    pdf_merger.append(path)

pdf_merger.write('merge.pdf')

#read pdf
pdf_path=Path('merge.pdf')
pdf_reader=PdfReader(pdf_path)
# for page in pdf_reader.pages:
#     print(page.extract_text())

#extract pdf
for i,page in enumerate(pdf_reader.pages[0:3]):
    pdf_writer=PdfWriter()
    pdf_writer.add_page(page)
    pdf_writer.write('extract{}.pdf'.format(i))

#crop pdf
pdf_writer1=PdfWriter()
page1=pdf_reader.pages[0]
copy_file=copy.deepcopy(page1)
print(copy_file.mediabox)
copy_file.mediabox.upper_right=[550,0]
copy_file.mediabox.upper_left=[50,810]
pdf_writer1.add_page(copy_file)
pdf_writer1.write("crop.pdf")

#rotate pdf
pdf_writer2=PdfWriter()
for page in pdf_reader.pages:
    page.rotate(180)
    pdf_writer2.add_page(page)
pdf_writer2.write('rotate.pdf')

# pdf to jpeg

filepath = "sample.pdf"
pdf = pdfium.PdfDocument(filepath)
for i in range(len(pdf)):
    page = pdf[i]
    pil_image = page.render(scale=4).to_pil()
    pil_image.save(("pdf_to_image{}.jpg").format(i))

#image to pdf
image1 = Image.open('pdf_to_image0.jpg')
outputImage = image1
outputImage.save('image_to_pdf.pdf')