from sqlalchemy.orm import Session
from model.database import engine
from model.Artifact import Artifact



def find_all() -> [] :
    with Session(engine) as session:
        return session.query(Artifact).all()



def find_by_cnn_id(cnn_id: int) -> object:
    with Session(engine) as session:
        return session.query(Artifact).filter(Artifact.cnn_id == cnn_id).one_or_none()




def find_by_id(id: str) -> object:
    with Session(engine) as session:
        return session.query(Artifact).filter(Artifact.id == id).one_or_none()



def find_by_name(name: str) -> []:
    with Session(engine) as session:
        return session.query(Artifact).where(Artifact.name.ilike(f'%{name}%')).all()
