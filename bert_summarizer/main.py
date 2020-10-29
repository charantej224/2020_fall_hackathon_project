from  bert_summarizer.summarizer.question_answer import get_answer_for_question
from bert_summarizer.summarizer.summary_bert import get_summary_from_bert

question = 'What is machine learning?'

context = """Machine learning is an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from 
experience without being explicitly programmed. Machine learning focuses on the development of computer programs that can access data and use it learn for 
themselves. The process of learning begins with observations or data, such as examples, direct experience, or instruction, in order to look for patterns in 
data and make better decisions in the future based on the examples that we provide. The primary aim is to allow the computers learn automatically without
 human intervention or assistance and adjust actions accordingly."""

summary = get_summary_from_bert(context)
print("....BERT Summary....")
print(summary)
# answer1 = get_answer_for_question(question, context)
# answer2 = get_answer_for_question(question, summary)
# print("Answer from Original Content\n",answer1)
# print("Answer from BERT summary\n",answer2)


# https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/
