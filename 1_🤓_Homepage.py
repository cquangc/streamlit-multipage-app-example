import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Main Page")
st.sidebar.success("Select a page above.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)
    
if st.button("Click to go to Projects Page"):
    st.markdown("https://cquangc-streamlit-multipage-app-example-1--homepage-uxb8vo.streamlit.app/Projects", unsafe_allow_html=True)
