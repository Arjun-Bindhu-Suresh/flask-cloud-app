from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_cloud():
    return jsonify({"message": "✅ Build executed with custom service account!"})




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
