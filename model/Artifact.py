import uuid
from sqlalchemy.orm import Mapped, mapped_column, Session
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, Integer
from model.SchemaBase import Base



class Artifact(Base):
    __tablename__ = 'artifact'

    id: Mapped[str] = mapped_column(primary_key=True, default=uuid.uuid4)
    cnn_id: Mapped[Integer] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String(50))
    type: Mapped[str] = mapped_column(String(15))
    description: Mapped[str] = mapped_column(String, nullable=True, default=None)
    description_src: Mapped[str] = mapped_column(String, nullable=True, default=None)

    def __repr__(self) -> str:
        return f'Artifact(id:{self.id}, cnn_id={self.cnn_id}, name={self.name}, type={self.type}, description_src={self.description_src})'