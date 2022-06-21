
from flask import Flask,jsonify,request
import csv

all_articles=[]
with open("shared_articles.csv",encoding="utf8") as f:
    reader=csv.reader(f)
    data=list(reader)
    all_articles=data[1:]
    
like_articles=[]
not_like_articles=[]

app=Flask(__name__)  
@app.route("/get-all-articles")
def get_all_movies():
    return jsonify({
        "data":all_articles[0],
        "status":"success"
    })
    
@app.route("/like-articles",methods=["POST"])
def like_articles():
    articles=all_articles[0]
    all_articles=all_articles[1:]
    like_articles.append(articles)
    return jsonify({
        "status":"success"
    })   
    
        
@app.route("/unlike-articles",methods=["POST"])
def unlike_articles():
    articles=all_articles[0]
    all_articles=all_articles[1:]
    unlike_articles.append(articles)
    return jsonify({
        "status":"success"
    })   
    

          
if __name__ =="__main__":
    app.run()
    
    