from unicodedata import name
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
from app import db
import mysql.connector
import json
from dotenv import load_dotenv
import os

load_dotenv()


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(80))
    cpf = db.Column(db.Integer)

class Equipamento(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    tipo_equipamento = db.Column(db.String(80))

class Defeito(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    tipo_defeito = db.Column(db.String(80))

class Parecer (db.Model):
    id = db.Column(db.Integer, primary_key= True)
    cliente = Cliente.id
    equipamento = Equipamento.id
    defeito = Defeito.id






