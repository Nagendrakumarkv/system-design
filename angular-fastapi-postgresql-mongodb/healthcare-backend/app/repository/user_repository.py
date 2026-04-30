from app.models.user_model import User

class UserRepository:

    def create(self, db, user):
        db_user = User(username=user.username, password=user.password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def get_by_username(self, db, username):
        return db.query(User).filter(User.username == username).first()