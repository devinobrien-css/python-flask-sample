from dataclasses import dataclass
from src import db

@dataclass
class Object(db.Model):
    id: int
    name: str
    description: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return f"Object('{self.name}', '{self.description}')"
