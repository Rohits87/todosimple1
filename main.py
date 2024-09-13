from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, JWTManager
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)

# Configuring MongoDB and JWT
app.config['MONGO_URI'] = 'mongodb+srv://rohits87:AlWDmwaqGYv0s6aD@todoapp.tm229.mongodb.net/?retryWrites=true&w=majority&appName=todoapp'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

mongo = PyMongo(app)
jwt = JWTManager(app)

# Routes (register, login, tasks, etc.) - use the backend code I shared earlier
