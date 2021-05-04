from flask import Flask, jsonify, request
from sklearn import preprocessing, neighbors
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import pandas as pd

app = Flask(__name__)

@app.route('/calculate', methods=['GET'])
def calculate():
    data = request.args
    # nip = data.get('nip')
    hari = data.get('hari')
    # if nip is None:
    #     return jsonify({'code': 404, 'msg': 'Nip cannot blank.'})
    if hari is None:
        return jsonify({'code': 404, 'msg': 'Hari cannot blank.'})
    df = pd.read_csv("Dataset-training.csv", header=None)
    df.columns = ['NIP', 'Staf-Proses', 'Kategori']
    df = df.loc[df['Staf-Proses'] <= int(hari)]
    Y = df['Kategori']
    X = df[['Staf-Proses']]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
    clf = neighbors.KNeighborsClassifier()
    clf.fit(X_train, Y_train)
    pred = clf.predict(X_test)
    classifi = classification_report(Y_test, pred, output_dict=True)
    return jsonify({'code': 200, 'result': classifi})

if __name__ == '__main__':
    app.run(host='0.0.0.0')