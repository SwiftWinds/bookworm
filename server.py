from flask import Flask, request, jsonify
from factlister import eventLister

app = Flask(__name__)

@app.route('/get-dates', methods=['POST'])
def get_dates():
    req_data = request.get_json()
    text = req_data['text']
    subject = req_data['subject']

    return jsonify({
        'summary': eventLister(text, subject)
    })

if __name__ == "__main__":
    app.run()