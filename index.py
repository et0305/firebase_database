import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


from flask import Flask, render_template, request
from datetime import datetime, timezone, timedelta
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>曾子宇Python讀取Firestore</h1>"
    homepage += "<br><a href=/read>讀取Firestore資料</a><br>"
    return homepage

@app.route("/read")
def read():
    cond  = input("請輸入您要查詢的課程關鍵字：")
    db = firestore.client()
    collection_ref = db.collection("111")
    docs = collection_ref.get()
    result = ""
    for doc in docs:
        dict = doc.to_dict()
        if cond in dict["Course"]:
            #print("{}老師開的{}課程,每週{}於{}上課".format(dict["Leacture"], dict["Course"],  dict["Time"],dict["Room"]))
            result += dict["Leacture"] + "老師開的" + dict["Course"] + "課程,每週"
            result += dict["Time"] + "於" + dict["Room"] + "上課\n"
        else:
            result += "抱歉，查無相關條件的選修課程"
            break
    print(result)

if __name__ == "__main__":
    app.run()