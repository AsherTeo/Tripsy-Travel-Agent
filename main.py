from uuid import uuid4
from build_graph import graph

config = {'configurable': {'thread_id':"1"}}

while True:
    question = input("Users: ")
    if question == 'exit':
        break
    response = graph.invoke({'messages':[{'role': 'user', 'content': question}]}, config)

    print("AI", response['messages'][-1].content)