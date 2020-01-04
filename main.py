import PyPDF2

watermark_file = input('The name(or relative path) of the watermark file: ')

file_to_watermark = input(
    'The name(or relative path) of the file you want to watermark: ')

output_file = "watermarked.pdf"

# read content of the pdf to add watermark 2
pdf = PyPDF2.PdfFileReader(open(file_to_watermark, 'rb'))
# Create the PDF writer
pdf_writer = PyPDF2.PdfFileWriter()
# read content of the watermark PDF
watermark = PyPDF2.PdfFileReader(open(watermark_file, "rb")).getPage(0)

for i in range(pdf.getNumPages()):
    current_page = pdf.getPage(i)
    current_page.mergePage(watermark)

    pdf_writer.addPage(current_page)

with open(output_file, "wb") as output:
    # write the watermarked file to the new file
    pdf_writer.write(output)
