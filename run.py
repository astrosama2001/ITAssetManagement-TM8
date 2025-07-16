
from smartasset.app.app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    db.create_all()
    if not User.query.filter_by(username='admin').first():
        db.session.add(User(username='admin', password=generate_password_hash('admin123'), role='admin'))
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
