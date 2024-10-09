from flask import Flask

app=Flask(__name__)                 #Create an instance of flask class {app is now an object}

@app.get("/")                       #Flask decorator to map routes to view functions
def get_home():                     #Flask view function
    me={                            #Python dictionary {key-value pairs}
        "first_name":"Juan",
        "last_name":"Montiel",
        "hobbies":"Play chess",
        "is_online":True
    }
    return me                       #when you return a dict in Flask it is converted to JSON
