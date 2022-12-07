from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# create database in sqlalchemy
engine = create_engine('sqlite:///musicMatch.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)
    db_session.commit()

# create a users table within database to store user data
class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True} 

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def __init__(self, first_name=None, last_name=None, email=None, username=None, password=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User {self.id, self.username!r}>'

