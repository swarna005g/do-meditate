import streamlit as st
import time

st.set_page_config(
    page_title="Do Meditate",
    page_icon="🧘",
    layout="centered"
)

# ---------------- SESSION ----------------
if "role" not in st.session_state:
    st.session_state.role = None
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "screen" not in st.session_state:
    st.session_state.screen = "role"

# ---------------- TITLE ----------------
st.title("🧘 Do Meditate")
st.caption("A simple wellness app inspired by heart-based practices")
st.divider()

# ---------------- ROLE ----------------
if st.session_state.screen == "role":
    st.subheader("Select your role")

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("Student"):
            st.session_state.role = "student"
            st.session_state.screen = "login"
    with c2:
        if st.button("Abhyasi"):
            st.session_state.role = "abhyasi"
            st.session_state.screen = "login"
    with c3:
        if st.button("Preceptor"):
            st.session_state.role = "preceptor"
            st.session_state.screen = "login"

# ---------------- LOGIN ----------------
elif st.session_state.screen == "login":
    st.subheader(f"Login as {st.session_state.role.capitalize()}")

    if st.session_state.role == "student":
        st.text_input("Email")
    else:
        st.text_input("ID Number")

    st.text_input("Password", type="password")

    if st.button("Login"):
        st.session_state.logged_in = True
        st.session_state.screen = "home"

# ---------------- HOME ----------------
elif st.session_state.screen == "home":
    st.subheader("Home")

    if st.button("🧘 Relaxation"):
        st.session_state.screen = "relaxation"

    if st.session_state.role != "student":
        st.button("🧠 Meditation", disabled=True)
        st.button("🧹 Cleaning", disabled=True)

    st.divider()
    if st.button("Logout"):
        st.session_state.screen = "role"
        st.session_state.logged_in = False
        st.session_state.role = None

# ---------------- RELAXATION ----------------
elif st.session_state.screen == "relaxation":
    st.subheader("🌿 Relaxation")

    st.write("""
    Sit comfortably.  
    Close your eyes gently.  
    Relax your body from head to toe.  
    Let your thoughts settle naturally.
    """)

    if st.button("Start Relaxation"):
        with st.spinner("Relaxing..."):
            time.sleep(60)  # 1 minute demo
        st.success("Relaxation complete 🌸")

        if st.session_state.role != "student":
            st.text_area("Write your experience (optional)")

    if st.button("Back to Home"):
        st.session_state.screen = "home"

