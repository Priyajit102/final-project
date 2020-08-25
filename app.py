from sklearn.ensemble import GradientBoostingRegressor
from flask import Flask, render_template, request
import pickle

# from joblib import dump, load

app = Flask(__name__)
lr = pickle.load(open('lr.pkl', 'rb'))


# model = pickle.load(open('model.pkl','rb'))
# jb_model = joblib.load(open('jb_model.joblib','rb'))
# clf = load('filename.joblib')

@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/predict", methods=["POST"])
def predict():
    """
    iput = [x for x in request.form.values()]
    X_test = [np.array(iput)]
    """

    location = int(request.form.get('location'))
    total_sqft = float(request.form.get('total_sqft'))
    bath = float(request.form.get('bath'))
    bhk = int(request.form.get('bhk'))
    price_per_sqft = float(request.form.get('price_per_sqft'))
    X_test = [[location, total_sqft, bath, bhk, price_per_sqft]]

    # gbr_pred = model.predict(X_test)
    # gbr_pred = gbr_pred*100000
    # gbr_op = round(gbr_pred[0], 2)

    lr_pred = lr.predict(X_test)
    lr_pred = lr_pred * 100000
    lr_op = round(lr_pred[0], 2)

    # jb_pred = jb_model.predict(X_test)
    # jb_pred = jb_pred*100000
    # jb_op = round(jb_pred[0], 2)

    # clf_pred = clf.predict(X_test)
    # clf_pred = clf_pred*100000
    # clf_op = round(clf_pred[0], 2)

    return render_template('index.html', out_put="Price in linear model will be Rs. {}".format(lr_op))


if __name__ == "__main__":
    app.run(debug=True)
