import pyrebase
import streamlit as st

firebaseConfig={
    "apiKey": "AIzaSyDShqNzmUvV8CCbXLF5fLZ_A6rkViah7JM",
    "authDomain": "pychat-d129b.firebaseapp.com",
    "projectId": "pychat-d129b",
    "storageBucket": "pychat-d129b.appspot.com",
    "messagingSenderId": "771636659275",
    "appId": "1:771636659275:web:cb156358536d048adfb9ce",
    "databaseURL": "https://pychat-d129b-default-rtdb.firebaseio.com/"
}

firebase= pyrebase.initialize_app(firebaseConfig)
names = set()
db=firebase.database()

if 'room_key' not in st.session_state:
    st.session_state['room_key'] = 'public'

room = st.session_state['room_key']
result = db.child('messages').get()
rooms = db.child('rooms').get()
# r = {"rooms":'public'}
# db.child('rooms').push(r)
if rooms.each() is not None: 
        for i in rooms.each():
            names.add(i.val()['rooms'])


st.title(room+' chat room')
if result.each() is not None: 
    for i in result.each():
        if i.val()['room']==room:
            st.text(i.val()['name']+" : "+i.val()['message'])
else:
    st.text("No messages yet")

user = st.text_input('User')
message = st.text_input('Enter the message')
data = {"name":user,"message":message,"room":room}
if st.button('Submit',key=1):
    db.child('messages').push(data)
    st.experimental_rerun()


with st.sidebar:
    option = st.selectbox(
    'What would you like to do?',
    ('Create a private room', 'Join a private room'))
    if option == 'Create a private room':
        st.title('Enter name of the room to create')
        room_name = st.text_input("").strip()
        if st.button('Submit',key=2):
            if room_name not in names:
                r = {"rooms":room_name}
                db.child('rooms').push(r)
                st.text(room_name+" successfully created")
                st.session_state['room_key'] = room_name
            else:
                st.text("The room "+room_name+" already exists")
   
    if option == 'Join a private room':
        st.title('Enter name of the room')
        room_name = st.text_input("")
        if st.button('Submit',key=3):
            if room_name not in names:
                st.text("The room "+room_name+" does not exist")
            else:
                st.session_state['room_key'] = room_name