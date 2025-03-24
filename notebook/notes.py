from datetime import datetime
import sqlalchemy as sa
import sqlalchemy.orm as so
from notebook import db
from notebook.model import Note, Comment


def retrieve_note(name: str):
    query = sa.select(Note).where(Note.name == name)
    return db.session.scalars(query).one()


def add_note(name: str, content: str):
    db.session.add(Note(name=name, content=content))
    try:
        db.session.commit()
        return True
    except sa.exc.IntegrityError as e:
        db.session.rollback()
        return False


def add_comment(content: str, note: Note):
    db.session.add(Comment(content=content, note=note))
    try:
        db.session.commit()
        return True
    except sa.exc.IntegrityError as e:
        db.session.rollback()
        return False


def delete_note(note: Note):
    db.session.delete(note)
    try:
        db.session.commit()
        return True
    except sa.exc.IntegrityError as e:
        db.session.rollback()
        return False


def list_notes():
    query = sa.select(Note.name)
    return db.session.scalars(query).all()


def find_notes(keyword: str):
    query = sa.union(
        sa.select(Note.name).where(
            sa.or_(Note.name.regexp_match(keyword),
                   Note.content.regexp_match(keyword),
                   )),
            sa.select(Note.name).join(Comment.note).where(
                Comment.content.regexp_match(keyword)))
    return db.session.scalars(query).unique()


def feedback(success: bool, message: str):
    if success:
        return message
    else:
        return "An error occured. Please try again."
