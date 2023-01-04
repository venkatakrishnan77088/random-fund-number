from flask import Flask,render_template,request
import requests

app=Flask(__name__)
d=[]

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/venkat",methods=["POST","GET"])
def output():
    num=request.form.get("id")
    url="https://api.mfapi.in/mf/"+str(num)
    res=requests.get(url)
    fund=res.json().get("meta").get("fund_house")
    nav = res.json().get("data")[0].get("nav")
    dic ={"id":num,"fund":fund,"nav":nav}
    d.append(dic)
    return render_template("expeted.html",data=d)



   



if __name__=="__main__":
    app.run(debug=True)
    