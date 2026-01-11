To set up you need to:
1. Create the PostgreSQL database locally. Run all the scripts from sql folder. Start with schema, then seed, then proceed with all other.
2. Run Visual Studio Code. Ensure you have installed at least Python 3.10. 
3. Install additional libraries: FastAPI, Uvicorn, SQLAlchemy, Psycopg2-binary, Psycopg, Jinja2(if you do not want to install them globally, create a virtual environment first)
4. Change the password and database name and port in database.py
5. Run the app with a command: uvicorn main:app --reload    (Make sure you are in the app folder!)
6. Enjoy!

Reflections:
We have really enjoyed working on this project. We espacially liked thinking about what functions might be useful for our users. Unfortunately, we have not been able to implement all of the things we came up with, but we focused on the most crucial ones. This project allowed us to improve our skills in databases, programming and web development. 