
import json
from flask import Flask,request,render_template
from werkzeug.utils import secure_filename
from sample_sheet import SampleSheet


app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def func():
    print("=======")
    return render_template('file1.html')

@app.route('/result',methods = ['POST'])
def result():
    print("+++++++++++")
    request.method == 'POST'
    result = request.files['file']
    path = result.filename
    result.save(secure_filename(path))
    sample_Sheet = SampleSheet(path)
    data = sample_Sheet.to_json()
    data1 = json.loads(data)
    headers = data1.get('Header')
    tabledata = data1.get('Data')
    keys = tabledata[0].keys()

    return render_template('temp.html',tabledata = tabledata,headers = headers, keys=keys)

    
if __name__ == "__main__":
    app.run(debug=True)

