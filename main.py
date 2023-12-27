from fitz import fitz
from PIL import Image

def convert_pdf_to_images(pdf_path, image_folder):
    # Abre o arquivo PDF
    pdf_document = fitz.open(pdf_path)

    # Itera sobre as páginas do PDF
    for page_number in range(pdf_document.page_count):
        # Obtém a página atual
        page = pdf_document[page_number]

        # Obtém a imagem da página como Pixmap
        pixmap = page.get_pixmap()

        # Converte o Pixmap para uma imagem PIL
        image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)

        # Salva a imagem no diretório de destino
        image.save(f"{image_folder}/page_{page_number + 1}.png")

    # Fecha o arquivo PDF
    pdf_document.close()

# Caminho do arquivo PDF de entrada
pdf_path = 'pdffiles/romilson-lemes-cordeiro_pythonBrazil2023.pdf'

# Pasta de saída para as imagens
output_folder = "filesResult"

# Cria a pasta de saída se não existir
import os
os.makedirs(output_folder, exist_ok=True)

# Chama a função para converter o PDF em imagens
convert_pdf_to_images(pdf_path, output_folder)

print("Conversão concluída.")
