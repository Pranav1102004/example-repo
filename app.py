import streamlit as st
from PIL import Image


st.title("Pranav")
st.header("Sharma")
st.subheader("kya bolti public")
st.text("hnji kya hall hai")
st.success("kamyab")
st.info("lelo bhai")
st.warning("khatra hai bhai")
st.error("galti kaise kari bkl")
st.write("likra hoon bhai")
st.write(range(1,10))
if st.checkbox("tik mar bhai"):
	st.text("7 crore lele bkl")

status = st.radio("select gender:" ,('male','female','others'))
if(status == 'male'):
	st.success('male')
elif(status == 'female'):
	st.success('female')
else:
	st.error('specify your planet')

hobby = st.multiselect("hobbies:",['dance','laundiabaji','bakchodi','bherapan'])

button = st.button('daba de bhai ')
if(button):
	st.text('bkl kaise dabara')	
	
name = st.text_input('nam likh bhai','dhang sai likhiyo nahi to teri **')
level = st.slider("select kr bkl",1,5)
st.text(f"selcted {level}")	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
