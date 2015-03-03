from insights import app

if __name__=='__main__':
    #from utility import db_create
    app.run(host='0.0.0.0', port=8080,debug=True)
    