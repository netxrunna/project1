import json
from flask import Flask, request, redirect, url_for
from backup import folder
from data import get, stats

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True


@app.route('/log')
def log():
    try:
        startdate = request.args.get('startdate')
        enddate = request.args.get('enddate')

        logs = get(startdate, enddate)
        response = logs
        #response = json.loads(str(response))
        #response = json.dumps(response, indent=2)
        #return json.dumps(response, indent=2)
        return response
    except ValueError:
        response = "Dates were not in the expected format."
        return response, 400


@app.route('/stat')
def stat():
    statistics = stats()
    response = statistics
    return response

@app.route('/backup', methods=['POST'])
def backup(): 

    folder_to_backup = request.json["path"]
    try:
        if folder_to_backup is None:
            response = "Please specify a folder or file to backup!"
            return response, 400

        folder(folder_to_backup)
        response = "Backup Completed"
        return response, 201
    except ValueError:
        response = "Error 404 -  No folder or file found at path: " + folder_to_backup
        return response, 404
    
@app.route('/')
def home():
    return(redirect(url_for('backup')))


if __name__ == '__main__':
    app.run(host='0.0.0.0')