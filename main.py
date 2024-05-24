import qrcode
from PIL import Image

def generar_codigo_qr(texto_o_url, nombre_archivo):
    # Crear objeto QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Agregar los datos al objeto QRCode
    qr.add_data(texto_o_url)
    qr.make(fit=True)

    # Crear una imagen QR
    imagen_qr = qr.make_image(fill_color="black", back_color="white")

    # Guardar la imagen QR
    imagen_qr.save(nombre_archivo)

if __name__ == "__main__":
    texto_o_url = input("Introduce el texto o la URL para generar el código QR: ")
    nombre_archivo = input("Introduce el nombre del archivo de imagen para guardar el código QR (incluye la extensión, por ejemplo, 'codigo_qr.png'): ")

    generar_codigo_qr(texto_o_url, nombre_archivo)
    print(f"¡Se ha generado el código QR y se ha guardado en {nombre_archivo}!")
