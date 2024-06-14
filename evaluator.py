import pandas as pd
from ragas import evaluate
from ragas.metrics import (
    answer_relevancy,
    faithfulness,
    context_recall,
    context_precision,
)
from datasets import Dataset

eval_dataset = pd.read_csv("baseline_answers.csv")
eval_dataset = Dataset.from_pandas(eval_dataset)
print(eval_dataset)
result = evaluate(
    eval_dataset,
    metrics=[
        context_precision,
        faithfulness,
        answer_relevancy,
        context_recall,
    ],
)

print(result)

