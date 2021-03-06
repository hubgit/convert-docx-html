import os, shutil, subprocess, tempfile
from flask import Flask, request, send_file, abort

app = Flask(__name__)

@app.route('/<tool>', methods=['POST'])
def convert(tool):
    working_dir = tempfile.mkdtemp()
    input_path = os.path.join(working_dir, 'input.docx')

    request.files['input'].save(input_path)

    if tool == 'pandoc':
        output_path = os.path.join(working_dir, 'output.html')
        command = ['pandoc', input_path, "-o", output_path]
    elif tool == 'calibre':
        output_path = os.path.join(working_dir, 'output.htmlz')
        command = ['/opt/calibre/ebook-convert', input_path, output_path]
    elif tool == 'mammoth':
        output_path = os.path.join(working_dir, 'output.html')
        command = ['mammoth', input_path, output_path]
    else:
        abort('Unknown tool')

    res = subprocess.Popen(command, stdout=subprocess.PIPE)

    output, error = res.communicate()

    if error:
        abort(error)
        return "Error"

    else:
        return send_file(output_path, mimetype='text/html') # TODO: attachment with filename?

    # shutil.rmtree(working_dir)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
