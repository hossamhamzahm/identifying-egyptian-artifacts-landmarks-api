from database import engine
from Artifact import Artifact
from sqlalchemy.orm import Session
from model.SchemaBase import Base
import os
import json





artifacts = []
class_name_path = os.path.join(os.path.dirname(__file__), "..", "data", "class_name.json")
info_path = os.path.join(os.path.dirname(__file__), "..", "data", "data_set_info")


def drop_artifacts():
    Artifact.__table__.drop(engine)


def load_artifacts():
    with open(class_name_path, "r") as classes_f:
        classes = json.load(classes_f)
        
        for id in classes:
            description_path = os.path.join(info_path, f'{classes[id]}.txt')
            description = None
            description_src = None
            
            if os.path.exists(description_path):
                with open(description_path, "r", encoding='cp1252') as info_f:
                    [description, description_src] = info_f.readlines()
                    description = description.strip()
                    description_src = description_src.strip()
                    description_src = description_src.split(' ')[1]

            artifact =  Artifact(name=classes[id], cnn_id=eval(id), type="artifact", description=description, description_src=description_src)
            artifacts.append(artifact)


def seed_artifacts():
    with Session(engine) as session:
        # session.query(Artifact).delete()
        session.add_all(artifacts)
        session.commit()





def read_artifacts():
    with Session(engine) as session:
        for row in session.query(Artifact).filter(Artifact.cnn_id >= 0).all():
            print(row)


if __name__ == "__main__":
    drop_artifacts()
    Base.metadata.create_all(engine)

    load_artifacts()
    seed_artifacts()
    artifact =  Artifact(name="Unknown", cnn_id=-1, type="artifact", description="Undetected class. Please upload a clearer image.")
    with Session(engine) as session:
            session.add(artifact)
            session.commit()


    # read_artifacts()