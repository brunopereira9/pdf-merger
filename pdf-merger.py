import PyPDF2 

filesName = ['_files/pdf_1.pdf', '_files/pdf_2.pdf', '_files/pdf_3.pdf']

pdfWriter = PyPDF2.PdfFileWriter()
for pdfFile in filesName:
  pdfReader = PyPDF2.PdfFileReader(pdfFile)
  for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

 
pdfOutputFile = open('_files/MergedFiles.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
 
pdfOutputFile.close()