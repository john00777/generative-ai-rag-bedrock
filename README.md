# generative-ai-rag-bedrock
A Retrieval-Augmented Generation (RAG) Q&amp;A system using Amazon Bedrock, LangChain, and RAGAS with guardrails for safety and quality evaluation.
# 🧠 Generative AI Project: RAG-Based Q&A System using Amazon Bedrock

This project was completed as part of the **Amazon Bedrock Generative AI Bootcamp** on AWS Skill Builder. It demonstrates how to build a production-grade **RAG (Retrieval-Augmented Generation)** system with safety guardrails, model evaluation, and secure question answering using Amazon Bedrock services.

## ✅ Project Overview

This project showcases:
- 🗃️ A **Knowledge Base** integrated with Amazon Bedrock
- 🔍 Query reformulation to improve retrieval accuracy
- 🧠 **Retrieval-Augmented Generation (RAG)** using the `RetrieveAndGenerate` API
- 🧪 Evaluation using **RAGAS** metrics (faithfulness, context precision, hallucination, etc.)
- 🔐 Implementation of **Guardrails** for safe and responsible GenAI outputs

## 📚 Tools & Technologies

| Tool | Purpose |
|------|---------|
| Amazon Bedrock | LLM access, RAG pipeline |
| LangChain | Q&A chain construction |
| AmazonKnowledgeBasesRetriever | To fetch relevant documents |
| Titan / Claude / Mistral models | LLM generation |
| RAGAS | Evaluation metrics |
| Python | Custom scripting and chain control |
| AWS Skill Builder Lab | Hosted environment for experimentation |

## 🧪 Evaluation Metrics (RAGAS)

Evaluated responses based on:
- Answer Relevancy
- Context Recall / Precision
- Faithfulness (truthfulness)
- Hallucination Rate
- Answer Semantic Similarity
- Fluency and Coherence
- Relevance Score

## 🔐 Guardrails

Set up using Amazon Bedrock Guardrails:
- PII detection
- Policy violation filter (hate, violence, abuse, etc.)
- Regular expressions
- Contextual grounding
- Enforced vs Unenforced mode testing



