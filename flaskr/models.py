# coding: utf-8
from flaskr import db
from sqlalchemy import *

class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(Integer, primary_key=True)
    title = db.Column(Text)
    text = db.Column(Text)

    def __repr__(self):
        return "<Entry id{} = title={!r}>".format(self.id,self.title)

def init():
    db.create_all()