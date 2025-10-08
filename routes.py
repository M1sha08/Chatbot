from flask import render_template, redirect, url_for, request
from app import db
from models import Chat, ChatContent

def register_routes(app):

  @app.route("/")
  def homepage():
    
    chats = db.session.execute(
      db.select(Chat).order_by(Chat.timestamp)
    ).scalars().all()

    return render_template("homepage.html", chats=chats)
  
  @app.route("/chat/<int:chat_id>")
  def chat(chat_id):
    
    if request == "POST":
      
      user_message = request.form.get("usr_msg", "").strip()

      if user_message:
        try:
          new_user_message = ChatContent(
            sender="User",
            content=user_message,
            chat_id=chat_id
          ) 
          db.session.add(new_user_message)
          
          bot_response = ""
          new_bot_message = ChatContent(
            sender="Bot",
            content =bot_response,
            chat_id=chat_id
          )
          db.session.add(new_bot_message)

          db.session.commit()

        except Exception as e:
          db.session.rollback()
          print(f"ERROR: Failed to save messages. Details: {e}")

      return redirect(url_for("chat", chat_id=chat_id))
    
    messages = db.session.execute(
      db.select(Chat).filder_by(chat_id=chat_id).order_by(Chat.timestamp)
    ).scalars().all()

    return render_template("chat.html", chat_id=chat_id, messages=messages)
