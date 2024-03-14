from docx2pdf import convert

# Word 파일을 PDF로 변환
# convert("sample.docx", "sample_output.pdf")

def convert_docx_to_pdf(docx_name_with_path, output_pdf_name_with_path):
    convert(docx_name_with_path, output_pdf_name_with_path)


if __name__ == "__main__":
    convert_docx_to_pdf("sample.docx", "sample_output.pdf")
    