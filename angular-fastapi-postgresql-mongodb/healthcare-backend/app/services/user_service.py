from app.repository.user_repository import UserRepository
from app.core.security import hash_password, verify_password, create_access_token

class UserService:

    def __init__(self):
        self.repo = UserRepository()

    def register(self, db, user):
        user.password = hash_password(user.password)
        return self.repo.create(db, user)
     
    def login(self, db, form_data):
        db_user = self.repo.get_by_username(db, form_data.username)

        if not db_user:
            raise Exception("User not found")

        if not verify_password(form_data.password, db_user.password):
            raise Exception("Invalid password")

        token = create_access_token({"sub": db_user.username})
        return {
            "access_token": token,
            "token_type": "bearer"
        }