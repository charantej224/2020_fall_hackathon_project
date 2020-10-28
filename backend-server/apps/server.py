from flask import Flask, jsonify
from flask import request
from services.search_query import search_for_youtube, search_for_google

app = Flask(__name__)


@app.route('/api/v1/article/post', methods=['POST'])
def get_summary():
    print(request.json)
    return jsonify({'tasks': 'tasks'})


@app.route('/api/v1/article/answer', methods=['POST'])
def get_answer():
    return jsonify({'tasks': 'tasks'})


@app.route('/api/v1/article/score', methods=['POST'])
def get_score():
    return jsonify({'tasks': 'tasks'})


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
