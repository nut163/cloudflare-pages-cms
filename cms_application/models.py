```python
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

class Website(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    pages = db.relationship('Page', backref='website', lazy=True)

    def __init__(self, name):
        self.name = name
        self.pages.append(Page(label='Home'))

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(100), nullable=False)
    website_id = db.Column(db.Integer, db.ForeignKey('website.id'), nullable=False)
    contents = db.relationship('Content', backref='page', lazy=True)

    def __init__(self, label, website_id):
        self.label = label
        self.website_id = website_id

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    active_status = db.Column(db.Boolean, default=True)
    start_date = db.Column(db.DateTime, default=func.now())
    end_date = db.Column(db.DateTime, nullable=True)
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'), nullable=False)

    def __init__(self, title, body, page_id, active_status=True, end_date=None):
        self.title = title
        self.body = body
        self.page_id = page_id
        self.active_status = active_status
        self.end_date = end_date
```