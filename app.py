from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader

# =====================================================================
# CONFIGURACIÓN DE TAMAÑOS POR PORCENTAJE (Ejemplo: 0.50 = 50%, 1.20 = 120%)
# =====================================================================
PORCENTAJE_LOGO = 0.65   # Modifica este valor para agrandar o achicar el logo
PORCENTAJE_FIRMA = 0.65  # Modifica este valor para agrandar o achicar la firma
# =====================================================================

# 1. Configuración del lienzo
c = canvas.Canvas("example.pdf", pagesize=letter)
width, height = letter
margen = 1 * cm

# --- LOGO EN LA PARTE SUPERIOR DERECHA ---
# Leemos las dimensiones originales del logo
logo_img = ImageReader("logo.png")
logo_orig_w, logo_orig_h = logo_img.getSize()

# Calculamos el tamaño final aplicando el porcentaje
logo_w = logo_orig_w * PORCENTAJE_LOGO
logo_h = logo_orig_h * PORCENTAJE_LOGO

# Posición basándose en las nuevas dimensiones calculadas
logo_x = width - margen - logo_w
logo_y = height - margen - logo_h

c.drawImage(logo_img, logo_x, logo_y, width=logo_w, height=logo_h, mask='auto')


# --- TEXTOS CON ALINEACIONES ---
# c.drawCentredString(width / 2, 700, "Hello, World! (Centrado)")
# 1. Activamos la fuente Helvetica en negrita (Bold) con tamaño de letra 12
c.setFont("Helvetica-Bold", 12)
c.drawCentredString(width / 2, 700, "Hello, World! (Centrado)")

# 2. Restauramos la fuente a Helvetica normal para el resto del documento
c.setFont("Helvetica", 10)

c.drawString(margen, 650, "This is an aligned string example. (Izquierda)")
c.drawCentredString(width / 2, 600, "This is another aligned string example. (Centro)")
c.drawRightString(width - margen, 550, "This is yet another aligned string example. (Derecha)")


# --- FIRMA AL FINAL EN EL CENTRO ---
# Leemos las dimensiones originales de la firma
firma_img = ImageReader("firma.png")
firma_orig_w, firma_orig_h = firma_img.getSize()

# Calculamos el tamaño final aplicando el porcentaje
firma_w = firma_orig_w * PORCENTAJE_FIRMA
firma_h = firma_orig_h * PORCENTAJE_FIRMA

# Posición: Centrado horizontalmente y pegado al margen inferior
firma_x = (width / 2) - (firma_w / 2)
firma_y = margen

c.drawImage(firma_img, firma_x, firma_y, width=firma_w, height=firma_h, mask='auto')


# Guardamos el archivo
c.save()

print("PDF generado exitosamente con tamaños por porcentaje.")
