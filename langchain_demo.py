
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

template = ChatPromptTemplate.from_messages([
    ("system", "you are a calculator that responds with math only"),
    ("human", "answer this math question: what is two plus two?"),
    ("ai", "2+2=4"),
    ("human", "answer this math question: {question}?")
])

# initialize the model
model = OllamaLLM(model="gemma2:2b")

# create a chain to pass the prompt template into the LLM.
# a chain connects calls to different components
llm_chain = template | model 
# print(llm_chain.to_json())

# invoke this chain on the question variable
response = llm_chain.invoke(
    {"question": "what is square root of 25"}
)
print(response)