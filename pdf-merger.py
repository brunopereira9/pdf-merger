import PyPDF2 
 
pdf1File = open('_files/pdf_1.pdf', 'rb')
pdf2File = open('_files/pdf_2.pdf', 'rb')
pdf3File = open('_files/pdf_3.pdf', 'rb')

filesName = ['_files/pdf_1.pdf', '_files/pdf_2.pdf', '_files/pdf_3.pdf']

pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdf3Reader = PyPDF2.PdfFileReader(pdf3File)
 
pdfWriter = PyPDF2.PdfFileWriter()
for pdfFile in filesName:
  pdfReader = PyPDF2.PdfFileReader(pdfFile)
  for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

 
pdfOutputFile = open('MergedFiles.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
 
pdfOutputFile.close()