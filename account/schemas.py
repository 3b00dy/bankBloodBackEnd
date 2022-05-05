from typing import Optional
import datetime
from ninja import Schema
from pydantic import EmailStr, Field


class AccountCreate(Schema):
    first_name: str
    last_name: str
    email: EmailStr
    password1: str = Field(min_length=8)
    password2: str = Field(min_length=8)
    address: str
    bloodType: str
    birthdate: datetime.date
    gender: str
    phoneNumber:int


class AccountOut(Schema):
    first_name: str
    last_name: str
    email: EmailStr
    address: str = None
    bloodType: str = None
    birthdate: datetime.date = None
    gender: str = None
    phoneNumber:int


class TokenOut(Schema):
    access: str


class AuthOut(Schema):
    token: TokenOut
    account: AccountOut


class SigninSchema(Schema):
    email: EmailStr
    password: str


class AccountUpdate(Schema):
    first_name: str
    last_name: str
    email: EmailStr
    address: str
    bloodType: str
    birthdate: datetime.date
    gender: str


class ChangePasswordSchema(Schema):
    old_password: str
    new_password1: str
    new_password2: str
