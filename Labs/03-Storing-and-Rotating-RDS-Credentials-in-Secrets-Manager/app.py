from flask import Flask
from flaskext.mysql import MySQL
from flask import jsonify


def hardcoded_credentials():

  return dict(username='username', password='password', host='rds-endpoint')


def configure_app(credentials):

  app.config['MYSQL_DATABASE_USER'] = credentials['username']
  app.config['MYSQL_DATABASE_PASSWORD'] = credentials['password']
  app.config['MYSQL_DATABASE_HOST'] = credentials['host']
  app.config['MYSQL_DATABASE_DB'] = 'information_schema'


app = Flask(__name__)
mysql = MySQL()
mysql.init_app(app)


@app.route('/')
def db_connect():
  credentials = hardcoded_credentials()
  try:
    configure_app(credentials)
    conn = mysql.connect()
    
    return jsonify(db_status="CONNECTED", credentials=credentials)

  except Exception as error:
    return jsonify(db_status="DISCONNECTED",
                credentials=credentials,
                error_message=str(error))


if __name__ == '__main__':
 # Make the server publicly available by default
  app.run(debug=True, host='0.0.0.0')
