from flask import Flask, jsonify
from flask import request
from services.search_query import search_for_youtube, search_for_google
from services.scoring_pattern import get_sentence_similarity
from services.text_processing import get_summary_from_bert, get_answer_for_question

app = Flask(__name__)


@app.route('/api/v1/article/summary', methods=['POST'])
def get_summary():
    input_request = request.json
    summarized_content = get_summary_from_bert(input_request['content'])
    return jsonify({'summary': summarized_content})


@app.route('/api/v1/article/answer', methods=['POST'])
def get_answer():
    input_request = request.json
    answer = get_answer_for_question(input_request['question'], input_request['content'])
    return jsonify({'answer': answer})


@app.route('/api/v1/article/answer/validate', methods=['POST'])
def validate_answer():
    input_request = request.json
    answer, score = get_sentence_similarity(input_request['user_answer'], input_request['actual_answer'])
    response = {'is_true': answer, 'similarity_score': score}
    return jsonify(response)


@app.route('/api/v1/article/getvideoref', methods=['GET'])
def get_video_reference():
    query_token = request.args.get('query')
    results = search_for_youtube(query_token)
    return jsonify({'youtube_results': results})


@app.route('/api/v1/article/getwebref', methods=['GET'])
def get_web_reference():
    query_token = request.args.get('query')
    results = search_for_google(query_token)
    return jsonify({'web_url_results': results})


if __name__ == '__main__':
    app.run(debug=True)
