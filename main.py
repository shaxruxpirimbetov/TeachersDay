from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
ids = 1
data = []

@app.route("/")
def index_view():
	return render_template("index.html")

@app.route("/data/", methods=["GET", "POST"])
def data_route():
	global ids
	if request.method == "POST":
		first_name = request.json.get("first_name")
		last_name = request.json.get("last_name")
		grade = request.json.get("grade")
		
		data.append({
			"id": ids,
			"first_name": first_name,
			"last_name": last_name,
			"grade": grade
		})
		ids += 1
		return jsonify({"ok": True}), 201
	return jsonify(data), 200

if __name__ == "__main__":
	app.run()