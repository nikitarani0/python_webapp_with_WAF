from fastapi import APIRouter
from .models import User
from .utils import hash_password

router = APIRouter()

@router.post("/register")
def register_user(user: User):
	hashed_pass = hass_password(user.password)
	return {
	  "username": user.username,
	  "hashed_password": hashed_pass
	}
@router.get("/check")
def check():
	return {"status": "Auth module working"}
