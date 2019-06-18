from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import base64
import os

class Video(db.Model):
	id = db.Column(db.String(15), primary_key=True)
	title = db.Column(db.String(100), index=True)
	date = db.Column(db.DateTime)
	views = db.Column(db.Integer)
	likeCount = db.Column(db.Integer)
	dislikeCount = db.Column(db.Integer)
	favoriteCount = db.Column(db.Integer)
	commentCount = db.Column(db.Integer)
	channel_id = db.Column(db.String(30))
	description_id = db.Column(db.Integer, db.ForeignKey("description.id"))
	description = db.relationship("Description", foreign_keys=[description_id])
	comments = db.relationship("Comment", lazy='dynamic')
	caption = db.relationship("Caption", lazy='dynamic')

	def __repr__(self):
		return '<Video id={}, title={}>'.format(self.id, self.title)

class Description(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.Text)
	video_id = db.Column(db.String(15), db.ForeignKey("video.id"))

	def __repr__(self):
		return'<body= {}>'.format(self.body)

class Comment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.Text)
	video_id = db.Column(db.String(15), db.ForeignKey("video.id"))

	def __repr__(self):
		return '<body= {}>'.format(self.body)

class Caption(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.Text)
	video_id = db.Column(db.String(15), db.ForeignKey("video.id"))

	def __repr__(self):
		return '<body= {}>'.format(self.body)

class Admin(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), unique=True)
	token = db.Column(db.String(32), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	def get_token(self):
		now = datetime.utcnow()
		self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
		db.session.add(self)
		return self.token

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	@staticmethod
	def check_token(token):
		admin = Admin.query.filter_by(token=token).first()
		if admin is None:
			return None
		return admin

