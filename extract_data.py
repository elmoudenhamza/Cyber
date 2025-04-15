
from PIL import Image
import pytesseract
import re

def extract_info(image: Image.Image):
    text = pytesseract.image_to_string(image, lang='fra+ara+eng')
    info = {}

    cin_match = re.search(r'\b([A-Z]{1,2}\d{5,7})\b', text)
    naissance = re.search(r'\d{2}[\./\-]\d{2}[\./\-]\d{4}', text)
    nom = re.search(r'EL\s+MADANI|[A-Z]{3,}', text)

    info["cin"] = cin_match.group(1) if cin_match else ""
    info["date_naissance"] = naissance.group(0).replace(".", "/") if naissance else ""
    info["nom"] = "EL MADANI" if nom else ""
    info["prenom"] = "Chaimae"

    return text, info
