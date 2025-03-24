from datetime import datetime
import sqlalchemy as sa
import sqlalchemy.orm as so
from notebook import db

class Note(db.Model):
    __tablename__ = "note"

    nid: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(nullable=False, unique=True)
    content: so.Mapped[str] = so.mapped_column(nullable=False)
    comments: so.Mapped[list["Comment"]] = so.relationship("Comment", back_populates="note", cascade="all, delete")

    def __repr__(self):
        return f"Note({self.nid}, {self.name}, {self.content}, {self.comments})"

class Comment(db.Model):
    __tablename__ = "comment"

    cid: so.Mapped[int] = so.mapped_column(primary_key=True)
    date: so.Mapped[datetime] = so.mapped_column(default=lambda: datetime.now(), nullable=True)
    content: so.Mapped[str] = so.mapped_column(nullable=False)
    parent: so.Mapped[int] = so.mapped_column(sa.ForeignKey("comment.cid"), nullable=True)
    nid: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Note.nid))
    note: so.Mapped["Note"] = so.relationship("Note", back_populates="comments")

    def __repr__(self):
        return f"Coment({self.date}, {self.content})"
