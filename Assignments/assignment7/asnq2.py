# import Flask class from flask module
from flask import Flask, request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

# create a server usinf Flask
server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.post('/soil_moisture')
def create_soil_moisture():
    # extract data form form
    id = request.form.get('id')
    moisture = request.form.get('moisture')
    timestamp = request.form.get('timestamp')

    # create a query to add sensor readings into table
    query = f"insert into soil_moisture values({id}, {moisture},'{timestamp}');"

    #print(query)
    #execute the query 
    executeQuery(query=query)

    return "soil_moisture is added successfully"

@server.get('/soil_moisture')
def retrieve_soil_moisture():
    # create a select query
    query = "select * from soil_moisture;"

    # execute select query
    data = executeSelectQuery(query=query)

    return f"soil_moisture : {data}"

@server.put('/soil_moisture')
def update_soil_moisture():
    # extract data form form
    moisture = request.form.get('moisture')
    humidity = request.form.get('humidity')

    # create a query
    query = f"update soil_moisture SET humidity = '{humidity}' where moisture = '{moisture}';"

    # execute the query
    executeQuery(query=query)

    return "humidity is updated successfully"

@server.delete('/soil_moisture')
def delete_soil_moisture():
    # extract data form form
    moisture = request.form.get('moisture')

    # create a query
    query = f"delete from soil_moisture where moisture = '{moisture}';"

    # execute the query
    executeQuery(query=query)

    return "soil_moisture is deleted successfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)