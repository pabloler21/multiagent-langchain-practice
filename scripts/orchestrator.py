from enum import Enum
from typing import List
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


class DomainEnum(str, Enum):
    FINANCE = "finance"
    HR = "hr"
    TECH = "tech"
    GENERAL = "general"


class AgentEnum(str, Enum):
    FINANCE_AGENT = "finance_agent"
    HR_AGENT = "hr_agent"
    TECH_AGENT = "tech_agent"
    GENERAL_AGENT = "general_agent"


class RetrieverEnum(str, Enum):
    SEMANTIC = "semantic_retriever"
    KEYWORD = "keyword_retriever"
    HYBRID = "hybrid_retriever"
    WEB = "web_retriever"


class RoutingDecision(BaseModel):
    domain: DomainEnum = Field(description="Classified domain: finance, hr, tech, or general")
    agent: AgentEnum = Field(description="Specialist agent assigned to handle the query")
    context: List[str] = Field(description="Relevant source folder paths, e.g. ['data/hr_docs']")
    retriever: RetrieverEnum = Field(description="Retrieval strategy to use")
    reasoning: str = Field(description="Short explanation of why this routing is correct")


system_prompt = """
You are the orchestration agent for a company knowledge assistant.

Your job is to classify the user query, decide which specialist agent should handle it, and choose the correct retrieval strategy and context before answering.

Rules:
1. First, classify the query by domain:
   - finance: budgets, invoicing, discounts, reimbursement, payroll, taxes, vendor contracts, expenses
   - hr: hiring, benefits, vacations, leave, performance, training, ethics, workplace policies
   - tech: security, credentials, VPN, access, backups, incident response, hardware, CI/CD, infrastructure
   - general: broad, cross-domain, or not clearly tied to a policy area

2. Then choose the best agent:
   - finance_agent for finance-related questions
   - hr_agent for HR or employee policy questions
   - tech_agent for IT/security/infrastructure questions
   - general_agent for mixed or generic queries

3. Then choose the retrieval context:
   - Use only the relevant source folder:
     - finance -> data/finance_docs
     - hr -> data/hr_docs
     - tech -> data/tech_docs
   - If the query spans multiple domains, combine the relevant folders.
   - If the query is not about internal company policy and is asking for external, current, or realtime information, do not rely only on internal docs; choose a web-based retrieval strategy.

4. Then choose the retriever type:
   - semantic_retriever for conceptual questions, ambiguous wording, or policy interpretation
   - keyword_retriever for exact terms, policy names, titles, keywords, or precise references
   - hybrid_retriever for mixed intent or when the query contains both specific terms and broader context
   - web_retriever only when the answer depends on external or current information not covered by internal docs

5. Never fabricate policy details.
   - If the docs do not contain enough information, say that the answer cannot be determined from the selected context.
   - If multiple contexts are relevant, include both in routing but still prefer the most relevant one first.

6. Keep the decision structured and deterministic.
"""

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
orchestrator = llm.with_structured_output(RoutingDecision)


def route_query(user_query: str) -> RoutingDecision:
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_query},
    ]
    return orchestrator.invoke(messages)


if __name__ == "__main__":
    test_query = "¿Cuántos días de vacaciones me corresponden si llevo 1 año y medio?"
    print(f"Consulta de prueba: '{test_query}'\n")
    decision = route_query(test_query)
    print("Decisión del Orquestador:")
    print(decision.model_dump_json(indent=2))