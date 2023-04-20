import os 
from App.venv.main import app, db

port = int(os.environ.get('PORT', 5555))
if __name__ == "__main__":
    with app.app_context():         
        db.create_all()
    app.run(host='0.0.0.0', port=port, debug=False) #Изменить с true на false когда закончим