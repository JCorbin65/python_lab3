import lab_chat as lc
def get_username():
    username = input("Please enter your username: ").strip()
    return username.upper()
def get_group():
    group = input("Please enter the group you would like to join: ".strip())
    return group.upper()
def get_message():
    chat_message = input("Enter a message: ".strip())
    return chat_message
def initialize_chat():
    node = get_username()
    group = get_group()
    lc.get_peer_node(node)
    lc.join_group(node, group)
    channel = lc.get_channel(node, group)
    return channel
def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")

while True:
    start_chat()
