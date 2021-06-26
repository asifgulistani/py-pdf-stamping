import glob, os
import sys
import PyPDF2


dirname = os.path.dirname(__file__) #<-- absolute dir the script is in

# rel_path = "2091/data.txt"
# abs_file_path = os.path.join(dirname, rel_path)

# print(dirname + "/files")
for file in os.listdir(dirname + "/files"):
    if file.endswith(".pdf"):

        input_file = dirname + "/files/" + file
        output_file = dirname + "/output/" + file
        watermark_file = os.path.join(dirname, "stamp_with_sign.pdf")

        with open(input_file, "rb") as filehandle_input:
            # read content of the original file
            pdf = PyPDF2.PdfFileReader(filehandle_input)
            
            with open(watermark_file, "rb") as filehandle_watermark:
                # read content of the watermark
                watermark = PyPDF2.PdfFileReader(filehandle_watermark)
                
                # get first page of the original PDF
                first_page = pdf.getPage(0)
                second_page = pdf.getPage(1)
                
                # get first page of the watermark PDF
                first_page_watermark = watermark.getPage(0)
                
                # merge the two pages
                first_page.mergePage(first_page_watermark)
                
                # create a pdf writer object for the output file
                pdf_writer = PyPDF2.PdfFileWriter()
                
                # add page
                pdf_writer.addPage(first_page)
                pdf_writer.addPage(second_page)
                
                with open(output_file, "wb") as filehandle_output:
                    # write the watermarked file to the new file
                    pdf_writer.write(filehandle_output)

print('done');
sys.exit()

