import io
import json
from flask import Flask, jsonify, request
import pandas as pd
from flask import make_response

df_team = pd.read_csv('DE.csv',sep=',',low_memory=False)
print(df_team)
app = Flask(__name__)
@app.route('/', methods = ['GET'])
def hello_world():
    try:
     if(request.method == 'GET'):
        return "<h1>Hello, This is Ghart dost page. Now go your home</h1> "    


    except FileNotFoundError:
        return({
            'Status': 404,
            'error':'Resource error'
        })
def get_data():
    # read the CSV file into a string
    with open('DE.csv', 'r') as f:
        data = f.read()

    # use io.StringIO to convert the string to a "file-like" object
    data_file = io.StringIO(data)

    # read the data_file object into a DataFrame
    df = pd.read_csv(data_file)
    return df
    
@app.route('/id/<int:usrid>',methods = ['GET'])
def retunbyid(usrid):
    if(request.method == 'GET'):

        # df_team = df_team.to_json(orient='records')
        # return jsonify(df_team.to_dict(orient = 'records'))
            # read the CSV file into a DataFrame
        if usrid <= 9:
            
            df = pd.read_csv('DE.csv')
            df = df.loc[df.id==usrid]
            json_string = df.to_json(orient='records')
            parsed_json = json.loads(json_string)


            # convert the DataFrame to an HTML table
            html = df.to_html()

            # create a response object with the HTML table as the body
            response = make_response(html)

            # set the content type of the response to "text/html"
            response.headers["Content-Type"] = "text/html"

            # return the response object
            return jsonify({
                "data": parsed_json
            })
        else:
          return jsonify({'status':'404',
            'message':'userId not found'})     
            
            
    else:
        return jsonify({'status':'404',
            'message':'userId not found'})      



if __name__ == '__main__':
    # app.run(host="0.0.0.0",port=8080)
    app.run()