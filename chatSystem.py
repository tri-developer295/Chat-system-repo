# mini - project using the concept of oops
# mini -  chat system

class Message:
    Message_counter = 1 # used to give message to unique id

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.id = Message.Message_counter
        Message.Message_counter += 1 # Assign the current counter value to the message

    def __str__(self):
        return f"({self.id}) {self.sender.username} : {self.content}"

class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None # keeps track of which chatroom you are in

    def join_chatroom(self, chatroom):
        if self.chatroom:
            print(f"{self.username} is already in chat room")
        
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.username} is already in {chatroom.name}")
    
    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} is not in chatroom")
        else:
            self.chatroom.remove_user(self)
            print(f"{self.username} left {self.chatroom.name}")
            self.chatroom = None

    def send_message(self, content):
        if not self.chatroom:
            print(f"{self.username} cannot send a message(in a chatroom)")
        else:
            self.chatroom.brodcast(self, content)

class Chatroom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self, user):
        self.users.append(user)
    
    def remove_user(self, user):
        self.users.remove(user)

    def brodcast(self, sender, content):
        message = Message(sender, content)
        self.messages.append(message)
        print(message)

    def show_chat_history(self):
        print(f"\nIn chat history of {self.name} : ")
        for msg in self.messages:
            print(msg)
        print()
    
if __name__ == "__main__":
    room = Chatroom("python launge")

    u1 = User("Alice")
    u2 = User("Bob")
    u3 = User("charlie")

    u1.join_chatroom(room)
    u2.join_chatroom(room)

    u1.send_message("Hello everyone!")
    u2.send_message("Hi Alice!")

    u3.join_chatroom(room)
    u3.send_message("Hey guys, what's up")

    room.show_chat_history()

    u1.leave_chatroom()
    u2.leave_chatroom()
    u3.leave_chatroom()