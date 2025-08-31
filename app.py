
import os
from flask import Flask, flash, request, redirect, url_for,render_template,send_from_directory
from rembg import remove
from flask import send_file

app = Flask(__name__,template_folder='templates')


@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        file = request.files['file']
        file.save(file.filename)
        v=str(file.filename)
        try:
            with open(v, 'rb') as i:
                with open("static/assets/images/lucos.jpg", 'wb') as o:
                    input = i.read()
                    output = remove(input, force_return_bytes=True)
                    o.write(output)

            return render_template("index.html",result=output)
        except:
            return render_template("index.html")
    return render_template("index.html")



    
        
if __name__== "__main__":
    app.run(debug=True)