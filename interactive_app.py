import streamlit as st
import time

if "photo" not in st.session_state:
    st.session_state["photo"]="not done"
    
col1, col2, col3 = st.columns([1,2,1])

col1.markdown(" # 432 1 Music ")
col1.markdown(" Interactive App! ")

st.slider("Slider", min_value=10, max_value=100, value=10, step=1)


def change_photo_state():
    st.session_state["photo"]="done"
    
uploaded_photo = col2.file_uploader("Upload a photo", on_change=change_photo_state)
camera_photo = col2.camera_input("Take a photo", on_change=change_photo_state)

if st.session_state["photo"] == "done":
    progress_bar = col2.progress(0)

    for perc_completed in range(100):
        time.sleep(0.05)
        progress_bar.progress(perc_completed+1)

    col2.success("photo upload successfully")

    col3.metric(label="Temperature", value="60 C", delta="3 C")

    with st.expander("Click to read more"):
        st.write("Hello, here are more details on this topic if you interested in.")
        
        if uploaded_photo is None:
            st.image(camera_photo)
        else:
            st.image(uploaded_photo)