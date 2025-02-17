from flask import Flask, request, send_file, jsonify
import treepoem
import io

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"message": "DataMatrix API is running. Use /datamatrix endpoint."})


@app.route('/datamatrix', methods=['GET'])
def generate_datamatrix():
    data = request.args.get('data', '')
    if not data:
        return jsonify({"error": "Missing 'data' parameter"}), 400

    img = treepoem.generate_barcode(barcode_type="datamatrix", data=data)
    img_stream = io.BytesIO()
    img.convert("RGB").save(img_stream, format="PNG")
    img_stream.seek(0)

    return send_file(img_stream, mimetype='image/png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
