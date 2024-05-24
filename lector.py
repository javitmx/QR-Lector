import cv2


def leer_codigo_qr(ruta_imagen):
    # Lee la imagen desde la ruta proporcionada
    imagen = cv2.imread(ruta_imagen)

    # Inicializa el detector de códigos QR
    detector = cv2.QRCodeDetector()

    # Detecta y decodifica el código QR en la imagen
    valor, _, _ = detector.detectAndDecode(imagen)

    # Retorna el valor del código QR
    if valor:
        return valor
    else:
        return None


# Ruta de la imagen que contiene el código QR
ruta_imagen = 'prueba.png'

# Llama a la función para leer el código QR
contenido_codigo_qr = leer_codigo_qr(ruta_imagen)

# Imprime el contenido del código QR
if contenido_codigo_qr:
    print("Contenido del código QR:", contenido_codigo_qr)
else:
    print("No se detectó ningún código QR en la imagen.")
