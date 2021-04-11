from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        "id":1,
        "phone":863452197,
        "name":"Akash Maity",
        "address":"Sriniketan, Bolpur ,Birbhum, West Bengal",
    },
    {
        "id":2,
        "phone":943682157,
        "name":"Soumyajit Saha",
        "address":"Jambuni, Bolpur ,Birbhum, West Bengal",
    },
    {
        "id":3,
        "phone":763219548,
        "name":"Anuradaha Saha",
        "address":"Rail Maidan, Bolpur ,Birbhum, West Bengal",
    },
    {
        "id":4,
        "phone":856431927,
        "name":"Anirudha",
        "address":"Santiniketan, Bolpur ,Birbhum, West Bengal",
    },
    
]

@app.route("/add-data", methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the details for the contact"
        },400)
    
    contact = [
        {
            "id":contacts[-1]["id"] + 1,
            "phone":request.json["phone"],
            "name":request.json.get("name",""),
            "address":request.json.get("address","")
        }
    ]
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message":"The contact has been added successfully!"
    })

@app.route("/get-data")
def get_contact():
    return jsonify({
        "data":contacts
    })

if __name__ == "__main__":
    app.run(debug=True)