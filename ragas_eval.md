# RAGAS Evaluation Summary

**RAGAS** (Retrieval-Augmented Generation Assessment Scores) is a framework used to evaluate the performance of RAG pipelines.

## Key Metrics:
- **Faithfulness**: Is the LLM answer consistent with the retrieved documents?
- **Answer Relevance**: Does the answer address the question?
- **Context Precision**: How useful was the context in the answer?
- **Context Recall**: Did we retrieve everything necessary?
- **F1 Score**: Combines precision and recall.

## Example Use Case
You can use RAGAS to test your RAG-based Q&A system with real or synthetic queries and check if the system retrieves the right documents and generates high-quality answers.
