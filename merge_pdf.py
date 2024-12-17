import os
import sys
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs_alternately(pdf1_path, pdf2_path, output_path):
    pdf1 = PdfReader(open(pdf1_path, 'rb'))
    pdf2 = PdfReader(open(pdf2_path, 'rb'))
    writer = PdfWriter()

    max_pages = max(len(pdf1.pages), len(pdf2.pages))

    for i in range(max_pages):
        if i < len(pdf1.pages):
            writer.add_page(pdf1.pages[i])
        if i < len(pdf2.pages):
            writer.add_page(pdf2.pages[i])

    with open(output_path, 'wb') as f:
        writer.write(f)

if __name__ == "__main__":
    if getattr(sys, 'frozen', False):
        # PyInstaller로 패키징된 실행 파일인 경우
        current_folder = os.path.dirname(sys.executable)
    else:
        # 일반적인 파이썬 스크립트인 경우
        current_folder = os.path.dirname(os.path.abspath(__file__))

    pdf1_path = os.path.join(current_folder, '1.pdf')
    pdf2_path = os.path.join(current_folder, '2.pdf')
    output_path = os.path.join(current_folder, 'compare.pdf')

    merge_pdfs_alternately(pdf1_path, pdf2_path, output_path)
