import streamlit as st

container1, container2 = st.container, st.container

key = 0

if key:
    with container1:
        st.title('Container 1')

else:
    with container2:
        st.title('Container 2')