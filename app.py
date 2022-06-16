
from flask import Flask, render_template, request, redirect,flash,url_for,jsonify
import os,time
from werkzeug.utils import secure_filename
from difflib import SequenceMatcher
from pyclass.CheckCondition import CheckCondition

from pyclass.CheckInputForm import CheckInputForm
from pyclass.Compile import Compile
from pyclass.FileOperation import FileOperation
from pyclass.Isolate import Isolate
from pyclass.SeparateFile import SeparateFile
import random



app = Flask(__name__)

# Set File extension variable
py = "py"  # For python
java = "java"  # For java
c = "c"  # For c
lang_list = ['py', 'java', 'c']
check_list = ['input','no-input','exact-match','ignore-space','sensitive','insensitive']
UPLOAD_FOLDER = '/var/local/lib/isolate/0/box'
ALLOWED_EXTENSIONS = {'txt', 'md'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#--------------------Start urls--------------------#
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/checktext')
def checktext():
    return render_template('checktext.html')

@app.route('/checkfile')
def checkfile():
    return render_template('checkfile.html')

@app.route('/text', methods=['POST'])
def text():
    if request.method == 'POST':
        #Set sandbox
        id_sandbox = random.randrange(0,1000)
        sandbox = Isolate(id_sandbox)

        #Recieve data
        if 'text' in request.form and request.form.get('text') != '':
            textmd = request.form['text']
        else:
            return 'Text is undefined.'
        has_ipf = False
        if 'inputfile' in request.files and request.files.get('inputfile').filename!= '':
            print('has input file')
            has_ipf = True
            ipf_req = request.files['inputfile']
        
        #Init Sanbox
        sandbox.init()

        #Error If text null
        if textmd == '':
            sandbox.clean()
            return jsonify(ERROR="Text is empty")
        #Continue
        else:
            text_to_seperate = SeparateFile(id_sandbox,'text.txt')
            k = text_to_seperate.separate(textmd=textmd)

        #Check data return error if not vaild
        cipf = CheckInputForm(k)
        if(cipf.isInValid()):
            sandbox.clean()
            return cipf.getErrorRes()
        
        #Setting files
        codefile = FileOperation(id_sandbox, cipf.getFilename())
        codefile.writeFile(cipf.getCode().strip())
        if has_ipf:
            ipf = FileOperation(id_sandbox,ipf_req.filename)
            ipfn = secure_filename(ipf_req.filename)
            app.config['UPLOAD_FOLDER'] = ipf.getIsopath()+ipfn
            ipf_req.save(app.config['UPLOAD_FOLDER'])
        else:
            ipf = FileOperation(id_sandbox,'inputfile.txt')
            ipf.writeFile(cipf.getInput())
    
        #Compile file and run
        option = cipf.getRunOperation()
        cp_program = Compile(id=id_sandbox,filename=cipf.getFilename(),inputfilename=ipf.getFilename(),language=cipf.getLanguage(),mem=option.get('mem'),time=option.get('time'))
        status_c,result_c = cp_program.run()
        #if error
        if not status_c:
            return result_c
        
        #Check
        check_result = CheckCondition(rsc=result_c,dict_k=k)
        check_result.check()
        sandbox.clean()
        return check_result.getDictAnswer()

@app.route('/file', methods=['POST'])
def file():
    if request.method == 'POST':
        #Set sandbox
        id_sandbox = random.randrange(0,1000)
        sandbox = Isolate(id_sandbox)

        #Init Sanbox
        sandbox.init()
        
        #Recieve data
        has_ipf = False
        if 'file' in request.files and request.files.get('file').filename!= '':
            f_req = request.files['file']
            mdf = FileOperation(id=id_sandbox,filename=f_req.filename)
            mdfn = secure_filename(f_req.filename)
            app.config['UPLOAD_FOLDER'] = mdf.getIsopath()+mdfn
            f_req.save(app.config['UPLOAD_FOLDER'])
        else:
            return 'File upload is undefined.'
        print(request.files.get('inputfile').filename)
        if 'inputfile' in request.files and request.files.get('inputfile').filename!= '':
            print('has input file')
            has_ipf = True
            ipf_req = request.files['inputfile']
        
        #Error If text null
        if mdf.readFile() == '':
            sandbox.clean()
            return jsonify(ERROR="Text is empty")
        #Continue
        else:
            text_to_seperate = SeparateFile(id_sandbox,f_req.filename)
            # print(text_to_seperate.readFile())
            # return {}
            k = text_to_seperate.separate()
            print(k)
        #Check data return error if not vaild
        cipf = CheckInputForm(k)
        if(cipf.isInValid()):
            sandbox.clean()
            return cipf.getErrorRes()
        
        #Setting files
        codefile = FileOperation(id_sandbox, cipf.getFilename())
        codefile.writeFile(cipf.getCode().strip())
        if has_ipf:
            ipf = FileOperation(id_sandbox,ipf_req.filename)
            ipfn = secure_filename(ipf_req.filename)
            app.config['UPLOAD_FOLDER'] = ipf.getIsopath()+ipfn
            ipf_req.save(app.config['UPLOAD_FOLDER'])
        else:
            ipf = FileOperation(id_sandbox,'inputfile.txt')
            ipf.writeFile(cipf.getInput())
        
        #Compile file and run
        option = cipf.getRunOperation()
        cp_program = Compile(id=id_sandbox,filename=cipf.getFilename(),inputfilename=ipf.getFilename(),\
            language=cipf.getLanguage(),mem=option.get('mem'),time=option.get('time'))
        status_c,result_c = cp_program.run()
        #if error
        if not status_c:
            return result_c
        
        #Check
        check_result = CheckCondition(rsc=result_c,dict_k=k)
        check_result.check()
        sandbox.clean()
        return check_result.getDictAnswer()

#--------------------End urls--------------------#
if __name__ == '__main__':
    # when deploy debug=false
    app.run(threaded=True,debug=True,port=5001)
