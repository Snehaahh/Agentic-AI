from langchain_core.prompts import ChatPromptTemplate
from llm_config import llm, parser



prompt = ChatPromptTemplate.from_messages([
("system",
"You are a chatbot assistant for an e-commerce website. "
"Answer using the website context and product data provided."),
("human",
"User Question:\n{question}\n\n"
"Available Products:\n{products}\n\n"
"Give a clear and correct answer.")
])

def run_chain(question, products):

  chain = prompt | llm | parser
  return chain.invoke({
"question": question,
"products": products
})