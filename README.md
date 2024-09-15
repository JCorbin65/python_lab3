# def get_peer_node(username):   
Function name is get_peer_node\
username: The peer node on the user's end\
This function creates a variable "n" which is\
Defined as the variable "username" after being\
passed the function "Pyre". "n" is then initialized\
with start and lasty returns "n".

# def join_group(node, group):
node: The node that the user wants to connect to\
group:The peer group that the user wants to join\
This function calls the join function from node and\
and it passes it the value of group and prints\
a confirmation.

# def chat_task(ctx, pipe, n, group):\
function name is chat_task

ctx: This is a ZeroMQ Connection Context\
pipe: This is a communications pipe polled by ZeroMQ for messages.\
n: This is the peer to peer node the user's chat app is connected as\
group: This is the peer chat group the user wishes to join

The chat_task method does not return anything, it appears to be the send/receive manager.

# def get_channel(node, group)
node: The node that the user wants to connect to\
group:The peer group that the user wants to join\
