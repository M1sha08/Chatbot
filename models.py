""" models.py """

from app import db

from datetime import datetime
from typing import Optional

class Chat(db.Model):
  pid = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.Text, nullable=False)
  timestamp = db.Column(db.DateTime, default=datetime.utcnow)

  chat_content = db.relationship("ChatContent", backref="chat", lazy=True, cascade="all, delete-orphan")
  # Note: relationship is allowing to access Chat content e.g.: Chat_obj.chat_content
  # backref creates shortcut, and is allowing to access parent chat e.g.: ChatContent_obj.Chat
  # chat_content is loaded only when trying to access the chat_content attribute
  # cascade='...' ensures to delete all the ChatContent data when user deltes the Chat 

  def __init__(self, pid: int, title: str, timestamp: Optional[datetime] = None) -> None:
    self.pid = pid
    self.title = title
    self.timestamp = timestamp

class ChatContent(db.Model):
  pid = db.Column(db.Integer, primary_key=True)
  sender = db.Column(db.Text, nullable=False)
  content = db.Column(db.Text, nullable=False)
    
  chat_id = db.Column(db.Integer, db.ForeignKey("chat.pid"), nullable=False)
  # This column creates the link back to the Chat table. The format db.ForeignKey('tablename.column_name') 
  # links this message to its parent chat session. It ensures every message belongs to an existing chat    

  timestamp = db.Column(db.DateTime, default=datetime.utcnow)

  def __init__(self, sender: str, content: str, chat_id: int, timestamp: Optional[datetime] = None) -> None:
    self.sender = sender
    self.content = content
    self.chat_id = chat_id
    self.timestamp = timestamp