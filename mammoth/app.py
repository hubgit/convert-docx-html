import os, shutil, subprocess, tempfile
from flask import Flask, request, send_file, abort

app = Flask(__name__)

@app.route('/', methods=['POST'])
def convert():
    working_dir = tempfile.mkdtemp()
    input_path = os.path.join(working_dir, 'input.docx')
    output_path = os.path.join(working_dir, 'output.html')

    request.files['input'].save(input_path)

    res = subprocess.Popen(['mammoth', input_path, output_path], stdout=subprocess.PIPE)

    output, error = res.communicate()

    if error:
        abort(error)
        return "Error"

    else:
        return send_file(output_path, mimetype='text/html')

    # shutil.rmtree(working_dir)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
