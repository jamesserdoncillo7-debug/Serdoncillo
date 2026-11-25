import streamlit as st

st.write("sup boi!")
st.title("this is the app title")
st.header("this is the header")
st.markdown("this is the markdown")
st.subheader("this is the subheader")
st.caption("this the caption")
st.code("x = 2021")
st.latex(r''' a+a r^1+a r^2+a r^3+a ''')

#st.image("C:\Users\CompLab\Downloads\MC.jpg", caption="Dream Shii!")

st.checkbox('yes please!')
st.button('touch me!')
st.radio('gay?', ['male', 'female', 'yes queen'])
st.selectbox('fruit?', ['apple', 'banana', 'orange'])
st.multiselect('planet?', ['jupiter', 'mars', 'neptune'])
st.select_slider('whos a good boy?', ['me', 'not me', 'Im gay'])
st.slider('bingo', 0, 50)

st.number_input('pick a number',0,10)
st.text_input('e sure jud')
st.date_input('birthday')
st.time_input('recess na!')
st.text_area('description')
st.file_uploader('send nodes')
st.color_picker('color bro')