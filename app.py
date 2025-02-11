from flask import Flask, jsonify, request
import os
import subprocess

app = Flask(__name__)

LABS_DIR = './labs'

@app.route('/labs', methods=['GET'])
def list_labs():
    labs = []
    for root, _, files in os.walk(LABS_DIR):
        for file in files:
            if file.endswith('.clab.yml'):
                labs.append({
                    'name': os.path.relpath(root, LABS_DIR) + '/' + file,
                    'path': os.path.join(root, file)
                })
    return jsonify(labs)

@app.route('/launch', methods=['POST'])
def launch_lab():
    lab_path = request.args.get('path')
    if lab_path:
        try:
            subprocess.run(['sudo', 'containerlab', 'deploy', '-t', lab_path], check=True)
            return jsonify({'message': f'Lab {lab_path} launched successfully.'})
        except subprocess.CalledProcessError as e:
            return jsonify({'message': f'Failed to launch lab {lab_path}: {str(e)}'}), 500
    return jsonify({'message': 'No lab path specified.'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)