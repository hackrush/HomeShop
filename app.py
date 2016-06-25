from flask import Flask,jsonify ,render_template
from firebase import firebase
from forms import FirePut

app=Flask(__name__,template_folder="./templates")
firebase = firebase.FirebaseApplication('https://shophome-8b5ad.firebaseio.com', None)
app.secret_key = 'this is a secet key dudes'
@app.route("/")
def index():
    result = firebase.get('/', None)
    print( jsonify(result))
    return render_template("index.html")


count = 0
@app.route('/api/put', methods=['GET', 'POST'])
def fireput():
    form = FirePut()
    #if form.validate_on_submit():
    global count
    count += 1
    putData = {"Name" : form.name.data, "phonenumber" : form.phonenumber.data, "product" : form.product.data,"email":form.email.data}
    firebase.put("/", "" + str(count), putData)
    return render_template("file.html", form=form, putData=putData)
    print (form.name.data)
    return render_template('users.html',form=form)

if __name__ == "__main__":
    app.run(debug=True)
