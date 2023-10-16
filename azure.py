import os
from langchain.llms import AzureOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain

from langchain.chains.constitutional_ai.base import ConstitutionalChain
from langchain.chains.constitutional_ai.models import ConstitutionalPrinciple

os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2023-05-15"
os.environ["OPENAI_API_BASE"] = "https://eur06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdaa-azopenai.openai.azure.com%2F&data=05%7C01%7Cchanchappa-gari.pratapreddy%40eviden.com%7C1323f08728d148809c3408dbc56504ce%7C7d1c77852d8a437db8421ed5d8fbe00a%7C0%7C0%7C638320809915529435%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=aKZbhzXNFMd8JvQAenIOPucv%2FELthoN6DSViPBXJ1hI%3D&reserved=0"
os.environ["OPENAI_API_KEY"] = "[613e7dfed67c4d2e89d7cb3c3bc56e01]"

qa_prompt = PromptTemplate(
    template="""You are a Microsoft specialist and know everything about the software it sells.  Your aim is to help operators and employees when using the software.

Question: {question}

Answer:""",
    input_variables=["question"],
)

llm = AzureOpenAI(
    deployment_name="[XXX-XXX]",
    model_name="[XXX-XXX]"
)


qa_chain = LLMChain(llm=llm, prompt=qa_prompt)

ethical_principle = ConstitutionalPrinciple(
    name="Ethical Principle",
    critique_request="The model should only talk about Microsoft related questions and answers because that is it's purpose.",
    revision_request="Rewrite the model's output recipe to be centered about Microsoft's software use and explain why you're not allowed to stray outside of this context.",
)

constitutional_chain = ConstitutionalChain.from_llm(
    chain=qa_chain,
    constitutional_principles=[ethical_principle],
    llm=llm,
    verbose=True,
)

constitutional_chain.run(question="Can I get alerts for Outlook new email?")