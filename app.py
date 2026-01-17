import streamlit as st

st.set_page_config(
    page_title="Do Meditate",
    page_icon="🧘",
    layout="centered"
)

if "role" not in st.session_state:
    st.session_state.role = None

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.title("🧘 Do Meditate")
st.caption("A simple wellness app inspired by heart-based practices")
st.divider()

# ROLE SELECTION
if st.session_state.role is None:
    st.subheader("Select your role")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Student"):
            st.session_state.role = "student"

    with col2:
        if st.button("Abhyasi"):
            st.session_state.role = "abhyasi"

    with col3:
        if st.button("Preceptor"):
            st.session_state.role = "preceptor"

    st.stop()

# LOGIN
st.subheader(f"Login as {st.session_state.role.capitalize()}")

if st.session_state.role == "student":
    st.text_input("Email")
    st.text_input("Password", type="password")
else:
    st.text_input("ID Number")
    st.text_input("Password", type="password")

if st.button("Login"):
    st.session_state.logged_in = True
    st.success("Login successful!")

# HOME
if st.session_state.logged_in:
    st.divider()
    st.subheader("Home")

    if st.session_state.role == "student":
        st.write("• Relaxation")
        st.write("• Free Books")
        st.write("• Kids Stories")
    else:
        st.write("• Relaxation")
        st.write("• Meditation")
        st.write("• Cleaning")
        st.write("• Journal")
        st.write("• Books & Stories")
