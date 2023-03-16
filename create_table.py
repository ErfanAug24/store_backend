from src import create_app,config,db
app=create_app(configClass=config.Config)

with app.app_context():
    db.create_all()
