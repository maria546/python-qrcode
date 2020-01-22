import pyqrcode as df
# .png
# .eps
# .svg
qr = df.create("https://www.innovation.com.pk")
qr.png("qrcode1.png")
qr.svg("qrcode2.svg")
qr.eps("qrcode3.eps")
import pyqrcode
qr = pyqrcode.create("https://www.innovation.com.pk")
qr.png("maria.png",scale = 8)


