import textwrap
from services.bert_question_answer import answer_question
from summarizer import Summarizer


def get_summary_from_bert(input_content):
    """
    Name: get_summary_from_bert
    :param input_content - String
    :return summary String.
    """
    body = ''' machine learning is the application of Artificial Intelligence'''
    model = Summarizer()
    result = model(body)
    summary = "".join(result)
    return summary


def get_answer_for_question(question, content):
    wrapper = textwrap.TextWrapper(width=160)
    generated_answer = answer_question(question, content)
    return generated_answer
