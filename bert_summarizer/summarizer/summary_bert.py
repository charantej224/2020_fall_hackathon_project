from newspaper import fulltext
import requests
from summarizer import Summarizer

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


