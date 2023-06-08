import os
from models import Dog, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Specify the path to the SQLite database file
db_file = 'dogs.db'
# Create an engine to connect to the database
engine = create_engine(f"sqlite:///{db_file}", echo=True, future=True)

# Create the tables if they don't exist
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)

def create_table(Base, engine):
    Base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()
    session.close()
    session.bind.dispose()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    return session.query(Dog).get(id)

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name==name, Dog.breed==breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()

if __name__ == '__main__':
    # Create a session
    session = Session()

    # Perform database operations
    dog = Dog(name='Fido', breed='Labrador')
    save(session, dog)

    # Close the session and the connection
    session.close()
    engine.dispose()

    # Remove the database file
    os.remove(db_file)
