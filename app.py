
import streamlit as st
from PIL import Image
from extract_data import extract_info
from anapec_bot import remplir_formulaire_anapec
from emploi_bot import remplir_formulaire_emploi
from cnss_bot import remplir_formulaire_cnss

st.set_page_config(layout="centered")
st.title("بوت تعبئة الاستمارات المغربية (نسخة تجريبية)")

service = st.selectbox("اختر الخدمة", [
    "تسجيل ANAPEC",
    "تسجيل Emploi-Public",
    "تسجيل CNSS"
])

uploaded_file = st.file_uploader("ارفع صورة البطاقة الوطنية", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="صورة البطاقة", use_column_width=True)

    extracted_text, info = extract_info(image)
    st.text_area("النصوص المستخرجة:", extracted_text, height=200)

    st.write("### البيانات المستخرجة:")
    st.json(info)

    if st.button("ابدأ تعبئة الاستمارة"):
        if service == "تسجيل ANAPEC":
            remplir_formulaire_anapec(info)
        elif service == "تسجيل Emploi-Public":
            remplir_formulaire_emploi(info)
        elif service == "تسجيل CNSS":
            remplir_formulaire_cnss(info)
