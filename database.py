import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load your Supabase URL and Key from the hidden .env file
load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

# Create the Supabase client that your app.py will use
supabase: Client = create_client(url, key)