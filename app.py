from flask import Flask,jsonify 
from firebase import firebase

app=Flask(__name__)
firebase = firebase.FirebaseApplication('https://shophome-8b5ad.firebaseio.com', None)

@app.route("/")
def index():
    result = firebase.get('/', None)
    return jsonify(result)


count = 0
@app.route('/api/put', methods=['GET', 'POST'])
def fireput():
    form = FirePut()
    If form.validate_on_submit():
        global count
        count += 1
        putData = {"Name" : form.name.data, "phonenumber" : form.phonenmber.data, "product" : form.product.data,"email":form.email.data}
        firebase.put("/users", "user" + str(count), putData)
        return render_template("api-put-result.html", form=form, putData=putData)
    return render_template("My-Form.html")

if __name__ == "__main__":
    app.run(debug=True)
