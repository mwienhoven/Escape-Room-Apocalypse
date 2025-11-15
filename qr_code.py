import qrcode

# Vraag de gebruiker om een URL
data = input("Voer de URL in die je wilt omzetten naar een QR-code: ")

# QR-code genereren
qr = qrcode.QRCode(
    version=1,  # grootte van de QR-code (1 = kleinste)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # foutcorrectieniveau
    box_size=10,  # grootte van elk vakje
    border=4,  # dikte van de rand
)

qr.add_data(data)
qr.make(fit=True)

# Afbeelding aanmaken
img = qr.make_image(fill_color="black", back_color="white")

# Opslaan als bestand
img.save("docs/qrcode.png")

print("✅ QR-code opgeslagen als docs/qrcode.png")
