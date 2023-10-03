import streamlit as st

# page config
st.set_page_config(page_title='Main',
                   layout='wide',
                   page_icon=pass)

# text formatting
st.header('This is Header')
st.subheader('Subheader')
st.caption('Write caption here')
st.text('plain text')
st.write('plain text 2')

st.markdown("""
Using markdown
# Title
## header
### subheader 1
#### subheader 2
""")

st.success('success message')
st.warning('warning message')
st.error('error message')
st.write('hello')