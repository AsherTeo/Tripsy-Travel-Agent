from uuid import uuid4
from build_graph import graph
from langgraph.types import Command

config = {'configurable': {'thread_id':"1"}}

while True:
    question = input("Users: ")
    if question == 'exit':
        break
    response = graph.invoke({'messages':[{'role': 'user', 'content': question}]}, config)

    while '__interrupt__' in response:
        print("AI:", response['__interrupt__'][0].value)
        answer = input('User: ')
        response = graph.invoke(Command(resume=answer), config)
    print("AI:", response['messages'][-1].content)