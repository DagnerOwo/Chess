import pygame
class Player:
    def __init__(self, name, password, email):
        self.name = name
        self.__password = password
        self.email = email

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password):
        print("Contraseña modificada.")
        self.__password = password
    
