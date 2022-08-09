from app.user.model import User
from app.user.schemas import Userschema
from app.services import BaseCRUDServices

class UserServices(BaseCRUDServices[User,Userschema]):
    def get_by_email(self , email :str ) -> User:
        return self.model.querry.filter_by(email=email).first()

user_services = UserServices(User)