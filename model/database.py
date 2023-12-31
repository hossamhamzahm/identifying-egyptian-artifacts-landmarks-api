from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


# db_name = "artifacts_db"
# db_host = "localhost"
# db_user = "user"
# db_pass = "user_passwd"
# db_port = 5432
# db_url = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'


load_dotenv()
supabase_db_url = os.getenv('SUPABASE_DB_URL')
supabase_db_url = supabase_db_url.replace('"', '')
print("\n\n\n\n")
print(supabase_db_url, "\n\n\n\n")
engine = create_engine(supabase_db_url, echo=True)