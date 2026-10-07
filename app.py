import streamlit as st
import requests

st.markdown(
    """
# Zoologist front

Describe your penguin for us 😊 🐧
"""
)

island = st.selectbox("Island: ", ("Dream", "Biscoe"))
bill_length = st.slider('Bill length (mm): ', 20.0, 70.0, step=5.0, value=51.9)
bill_depth = st.slider('Bill depth (mm): ', 5.0, 30.0, step=1.0, value=19.5)
flipper_length = st.slider('Flipper length (mm): ', 100, 500, step=50, value=206)
body_mass = st.slider('Body mass (g): ', 1500, 6000, step=500, value=3950)
gender = st.selectbox("Gender: ", ("Male", "Female"))

# api_url = "http://127.0.0.1:8000"
api_url = "https://zoo-api-390650046032.europe-west1.run.app"


penguin_props = {
    "island": island,
    "bill_length_mm": bill_length,
    "bill_depth_mm": bill_depth,
    "flipper_length_mm": flipper_length,
    "body_mass_g": body_mass,
    "sex": gender
}

r = requests.get(f"{api_url}/predict", params=penguin_props)
prediction = r.json()

if r.status_code == 200:
    st.write(f"🎊 Your penguin is a: **{r.json()["prediction"]}** 🎊")
else:
    st.write(f"There seems to be some issue... Status: {r.status_code} json: {r.json()}")

url = api_url + f"/predict?island={island}"
url += f"&bill_length_mm={bill_length}&bill_depth_mm={bill_depth}"
url += f"&flipper_length_mm={flipper_length}&body_mass_g={body_mass}"
url += f"&sex={gender}"
st.write("Try it out:", url)

st.write(f"""
    More infos: {api_url}/docs
""")
