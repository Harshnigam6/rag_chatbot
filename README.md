# Rag system to chat with pdfs

## Dataset Generation
We have used ChatGpt-4o to generate a synthetic data bassed on a given pdf. The prompts used for generating the dataset are stored in dir `dataset_generation_helper`.

TODO: To look into llamaindex/langchain dataset generation API and check if I can use custom prompts within their methods. Current dataset generation was done manually so this can be automated for scaling.

### Dataset Sample
Below is a sample row from the dataset used in the RAG system:

| Question                                                        | Answer                                                        | Topic          | Dataset Type |
|-----------------------------------------------------------------|---------------------------------------------------------------|----------------|--------------|
| What does the insurance cover in case of fire damage to my car? | Fire damage to your car is covered under the main policy.     | Fire and Theft | qa           |

### Dataset Column Explanation
The dataset consists of the following columns:

- **Question**: This column contains the questions to be posed to the language model. These questions are crafted based on specific topics or scenarios.

- **Answer**: This column includes the answers corresponding to the questions. These answers are used to train the model on accurate information retrieval.

- **Topic**: The topic column indicates the subject area under which the question and answer fall, helping to contextualize the conversation.

- **Dataset Type**: This column classifies the types of scenarios tested in the dataset. Each type is crucial for training the model to handle different kinds of user queries effectively. The types include:
  - **qa**: Simple question-answering scenario where the answer can be directly pulled from one section or topic.
  - **hallucination_check**: Challenges the model with questions that cannot be answered based on the given context. The model should identify the lack of context and inform the user accordingly, rather than fabricating an answer.
  - **cross_reference**: Scenarios where the answer may need to be inferred from different sections or topics.
  - **retrieval**: Focuses on queries about references, where the user asks under which topic or section they can find specific content.
