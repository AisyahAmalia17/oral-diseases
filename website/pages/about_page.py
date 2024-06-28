import streamlit as st
from PIL import Image
from st_social_media_links import SocialMediaIcons
import base64
from io import BytesIO

st.set_page_config(
    page_title="About",
)

st.markdown("<h1 style='text-align: center; color: white;'>ABOUT PAGE</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: white;'>SENYUMMU</h1>", unsafe_allow_html=True)

st.write("""
         Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
         labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
         reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
         """)

st.markdown("<h2 style='text-align: center; color: white;'>OUR TEAM</h1>", unsafe_allow_html=True)

st.write(""" ## DATA """)

columns = st.columns((1,1,1))

with columns[0]:
    img = Image.open("website/assets/Gishel.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write("Gishelawati")
    col1, col2 = st.columns([1,1])
    with col1:
        social_media_links = ["https://www.linkedin.com/in/gishelawati-129982201/"]
        social_media_icons = SocialMediaIcons(social_media_links)
        social_media_icons.render()
    with col2:
        st.markdown(
            """<a href="https://mail.google.com/mail/u/0/?tf=cm&fs=1&to=gishelawati01@gmail.com">
            <img src="data:image/png;base64,{}" width="25">
            """.format(base64.b64encode(open("website/assets/gmailicon.png", "rb").read()).decode()),
            unsafe_allow_html=True,)
    st.divider()

with columns[0]:
    img = Image.open("website/assets/kageyama.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Adi Kurniawan """)
    col1, col2 = st.columns([1,1])
    with col1:
        social_media_links = ["https://www.linkedin.com/in/adi-kurniawan-b65a2579"]
        social_media_icons = SocialMediaIcons(social_media_links)
        social_media_icons.render()
    with col2:
        st.markdown(
            """<a href="https://mail.google.com/mail/u/0/?tf=cm&fs=1&to=adikurniawan917@gmail.com">
            <img src="data:image/png;base64,{}" width="25">
            """.format(base64.b64encode(open("website/assets/gmailicon.png", "rb").read()).decode()),
            unsafe_allow_html=True,)
    st.divider()
    
with columns[1]:
    img = Image.open("website/assets/kageyama.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Bagus Akhlaq""")
    col1, col2 = st.columns([1,1])
    with col1:
        social_media_links = ["https://www.linkedin.com/in/bagus-akhlaq"]
        social_media_icons = SocialMediaIcons(social_media_links)
        social_media_icons.render()
    with col2:
        st.markdown(
            """<a href="https://mail.google.com/mail/u/0/?tf=cm&fs=1&to=bagusakhlaq@gmail.com">
            <img src="data:image/png;base64,{}" width="25">
            """.format(base64.b64encode(open("website/assets/gmailicon.png", "rb").read()).decode()),
            unsafe_allow_html=True,)
    st.divider()
with columns[2]:
    img = Image.open("website/assets/Nibras.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Nibras Alfaruqiyah""")
    col1, col2 = st.columns([1,1])
    with col1:
        social_media_links = ["https://www.linkedin.com/in/nibras-alfaruqiyah-web-developer-data/"]
        social_media_icons = SocialMediaIcons(social_media_links)
        social_media_icons.render()
    with col2:
        st.markdown(
            """<a href="https://mail.google.com/mail/u/0/?tf=cm&fs=1&to=alfaruqiyah.nibras@gmail.com">
            <img src="data:image/png;base64,{}" width="25">
            """.format(base64.b64encode(open("website/assets/gmailicon.png", "rb").read()).decode()),
            unsafe_allow_html=True,)
    st.divider()
with columns[2]:
    img = Image.open("website/assets/kageyama.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Azhani Syahputra""")
    col1, col2 = st.columns([1,1])
    with col1:
        social_media_links = ["https://www.linkedin.com/in/gishelawati-129982201/"]
        social_media_icons = SocialMediaIcons(social_media_links)
        social_media_icons.render()
    with col2:
        st.markdown(
            """<a href="https://mail.google.com/mail/u/0/?tf=cm&fs=1&to=gishelawati01@gmail.com">
            <img src="data:image/png;base64,{}" width="25">
            """.format(base64.b64encode(open("website/assets/gmailicon.png", "rb").read()).decode()),
            unsafe_allow_html=True,)
    st.divider()

    img = Image.open("/workspaces/codespaces-blank/image/our team/Gishel.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Gishelawati """)
with columns[0]:
    img = Image.open("/workspaces/codespaces-blank/image/our team/kageyama.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Adi Kurniawan """)
with columns[1]:
    img = Image.open("/workspaces/codespaces-blank/image/our team/kageyama.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Bagus Akhlaq""")
with columns[2]:
    img = Image.open("/workspaces/codespaces-blank/image/our team/Nibras.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Nibras Alfaruqiyah""")
with columns[2]:
    img = Image.open("/workspaces/codespaces-blank/image/our team/kageyama.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Azhani Syahputra""")

st.write(""" ## AI """)

columns = st.columns((1,1,1))

with columns[0]:
    img = Image.open("website/assets/Gunung.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Gunung Pambudi Wibisono """)
    col1, col2 = st.columns([1,1])
    with col1:
        social_media_links = ["https://www.linkedin.com/in/gunungpw/"]
        social_media_icons = SocialMediaIcons(social_media_links)
        social_media_icons.render()
    with col2:
        st.markdown(
            """<a href="https://mail.google.com/mail/u/0/?tf=cm&fs=1&to=gunungpambudiw@gmail.com">
            <img src="data:image/png;base64,{}" width="25">
            """.format(base64.b64encode(open("website/assets/gmailicon.png", "rb").read()).decode()),
            unsafe_allow_html=True,)
    st.divider()

with columns[0]:
    img = Image.open("website/assets/Wisnu.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Wisnu Eka Saputra S.""")
    col1, col2 = st.columns([1,1])
    with col1:
        social_media_links = ["https://www.linkedin.com/in/wisnuekasaputra"]
        social_media_icons = SocialMediaIcons(social_media_links)
        social_media_icons.render()
    with col2:
        st.markdown(
            """<a href="https://mail.google.com/mail/u/0/?tf=cm&fs=1&to=wisnuekasaputra@hotmail.com">
            <img src="data:image/png;base64,{}" width="25">
            """.format(base64.b64encode(open("website/assets/gmailicon.png", "rb").read()).decode()),
            unsafe_allow_html=True,)
    st.divider()

with columns[1]:
    img = Image.open("website/assets/kageyama.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Aisyah Amalia Al Fitri""")
    col1, col2 = st.columns([1,1])
    with col1:
        social_media_links = ["https://www.linkedin.com/in/aisyahamaliaalfitri/"]
        social_media_icons = SocialMediaIcons(social_media_links)
        social_media_icons.render()
    with col2:
        st.markdown(
            """<a href="https://mail.google.com/mail/u/0/?tf=cm&fs=1&to=arsyah291200@gmail.com">
            <img src="data:image/png;base64,{}" width="25">
            """.format(base64.b64encode(open("website/assets/gmailicon.png", "rb").read()).decode()),
            unsafe_allow_html=True,)
    st.divider()

with columns[2]:
    img = Image.open("website/assets/Vauwez.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Vauwez Sam El Fareez """)
    col1, col2 = st.columns([1,1])
    with col1:
        social_media_links = ["https://www.linkedin.com/in/samfareez/"]
        social_media_icons = SocialMediaIcons(social_media_links)
        social_media_icons.render()
    with col2:
        st.markdown(
            """<a href="https://mail.google.com/mail/u/0/?tf=cm&fs=1&to=vsefareez@outlook.com">
            <img src="data:image/png;base64,{}" width="25">
            """.format(base64.b64encode(open("website/assets/gmailicon.png", "rb").read()).decode()),
            unsafe_allow_html=True,)
    st.divider()

with columns[2]:
    img = Image.open("website/assets/kageyama.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Irvan Achmad Ashari""")
    col1, col2 = st.columns([1,1])
    with col1:
        social_media_links = ["https://www.linkedin.com/in/maragopan"]
        social_media_icons = SocialMediaIcons(social_media_links)
        social_media_icons.render()
    with col2:
        st.markdown(
            """<a href="https://mail.google.com/mail/u/0/?tf=cm&fs=1&to=irvanachmadashari@gmail.com">
            <img src="data:image/png;base64,{}" width="25">
            """.format(base64.b64encode(open("website/assets/gmailicon.png", "rb").read()).decode()),
            unsafe_allow_html=True,)
    st.divider()
    img = Image.open("/workspaces/codespaces-blank/image/our team/Gunung.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Gunung Pambudi Wibisono """)
with columns[0]:
    img = Image.open("/workspaces/codespaces-blank/image/our team/Wisnu.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Wisnu Eka Saputra S.""")
with columns[1]:
    img = Image.open("/workspaces/codespaces-blank/image/our team/kageyama.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Aisyah Amalia Al Fitri""")
with columns[2]:
    img = Image.open("/workspaces/codespaces-blank/image/our team/Vauwez.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Vauwez Sam El Fareez """)
with columns[2]:
    img = Image.open("/workspaces/codespaces-blank/image/our team/kageyama.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Irvan Achmad Ashari""")