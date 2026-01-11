from sqlalchemy import create_engine
#!!!! You need to first set up the database locally
# before usage please make sure to change it to your password and database name 
db_url = "postgresql+psycopg://postgres:password@localhost:5432/new_db"
engine = create_engine(db_url)


