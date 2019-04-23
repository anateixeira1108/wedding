import os

class Config:
	#SECRET_KEY = os.environ.get('SECRET_KEY')
	SECRET_KEY =  '02f3df4ba2cd178d3990f92978146be64'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	#SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')