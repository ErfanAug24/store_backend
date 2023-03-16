from src import create_app,config

app=create_app(config.Config)

if __name__=='__main__':
    app.run(debug=True,port=5000)