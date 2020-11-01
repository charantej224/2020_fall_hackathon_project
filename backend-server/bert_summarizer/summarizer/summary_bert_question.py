from newspaper import fulltext
import requests
from summarizer import Summarizer
import textwrap
from bert_summarizer.bertquestions.bert_cancer_question_answer import  answer_question

def get_summary_from_bert(input_content):
    """
    Name: get_summary_from_bert
    :param input_content - String
    :return summary String.
    """
    model = Summarizer()
    result = model(input_content, min_length=30, max_length=600)
    summary = "".join(result)
    return summary

def get_answer_for_question(question, context):
    wrapper = textwrap.TextWrapper(width=160)
    generated_answer = answer_question(question, context)
    return generated_answer