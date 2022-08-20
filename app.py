from flask import Flask , render_template , request , redirect ,flash

app = Flask(_name_)

@app.route("/" , methods=['GET' , 'POST'])
def faceDetection():
    return "Works"

if _name_ == "_main_" :
    app.run(debug= True)