from unittest.mock import MagicMock, patch
from langchain.messages import AIMessage
import model_llm
from uuid import uuid4 
from build_graph import graph 

def test_chatbot():
    fake_llm = MagicMock()
    fake_llm.invoke.return_value = AIMessage(content= "You should eat chicken rice")

    with patch.object(model_llm, "load_llm", fake_llm):
        config = {'configurable': {"thread_id": {uuid4()}}}
        response = graph.invoke({'messages': [{"role": "user", "content": "What should i eat ?"}]}, config)

        assert response['messages'][-1].content == "You should eat chicken rice"