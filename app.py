from flask import Flask,jsonify,request
app=Flask(__name__)
tasks = [
    {
        "id":3,
        "title":"buy groceries",
        "description":"milk,cheese,pizza,fruit,vegetable",
        "done":False
    },
    {
      "id":2,
      "title":'learn python',
      "description":"need to learn good python tutorial on web",
      "done":False
      
        
    }
]
@app.route('/')
def hello_world():
    return "HelloWorld"

@app.route('/add-data',methods=['POST'])

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)

    task = {
        "id":tasks[-1]["id"]+1,
        "title":request.json["title"],
        "description":request.json("description",""),
        "done":False
    }
    tasks.append(tasks)
    return jsonify({
        "status":"success",
        "message":"tasks added successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })


if(__name__=='__main__'):
    app.run(debug=True)
