# Python-chatroom
A python based public chat room where users can create rooms and talk to each other. It is built using the python frame work streamlit and firebase as the database storage.

# How to run
1) pip install pyrebase
2) pip install streamlit
3) Use the command streamlit run chat-firebase.py to run the application.

# Flow:
1- The public room is first accessed and the user can post messages by inputing their username and the message.

2- The messages are roomspecific and the user has to change rooms to view specific messages.

3- The user can change their room by using the sidebar.

4- New rooms can also be created using the sidebar. However the users should ensure that the room they are creating is unique as no two rooms can have the same name. 