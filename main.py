from uuid import uuid4
from build_graph import graph
from langgraph.types import Command

config = {'configurable': {'thread_id':"1"}}

while True:
    question = input("Users: ")
    if question == 'exit':
        break
    response = graph.invoke({'messages':[{'role': 'user', 'content': question}]}, config)

    shown = 0

    while '__interrupt__' in response:
        for m in response['messages'][shown:]:
            if m.type == 'ai':
                print("AI:", m.content)
                
        shown = len(response['messages'])
        print("AI:", response['__interrupt__'][0].value)
        answer = input('User: ')
        response = graph.invoke(Command(resume=answer), config)

    for m in response['messages'][shown:]:
        if m.type == 'ai':
            print("AI:", m.content)
            

    shown = len(response['messages'])