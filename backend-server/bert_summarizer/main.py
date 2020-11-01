from bert_summarizer.summarizer.summary_bert_question import get_summary_from_bert, get_answer_for_question
import textwrap
from bert_summarizer.bertquestions.bert_cancer_question_answer import  answer_question
wrapper = textwrap.TextWrapper(width=160)

question = 'What is machine learning?'

context = """Machine learning is an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from 
experience without being explicitly programmed. Machine learning focuses on the development of computer programs that can access data and use it learn for 
themselves. The process of learning begins with observations or data, such as examples, direct experience, or instruction, in order to look for patterns in 
data and make better decisions in the future based on the examples that we provide. The primary aim is to allow the computers learn automatically without
 human intervention or assistance and adjust actions accordingly."""

summary = get_summary_from_bert(context)
print("....BERT Summary....")
print(summary)


generated_answer1 = answer_question(question, context)
generated_answer2 = answer_question(question, summary)

print('--------------------------------------------')
print("Abstract Fed to the QA System")
print('--------------------------------------------')
print(wrapper.fill(summary))
print('--------------------------------------------')
print("Question Asked to System")
print('--------------------------------------------')
print(question)
print('system answer given by user from Original Text')
print('--------------------------------------------')
print(generated_answer1)
print('--------------------------------------------')
print(question)
print('system answer given by user from BERT Summary')
print('--------------------------------------------')
print(generated_answer2)




