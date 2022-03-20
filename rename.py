import os
from dotenv import load_dotenv
from pprint import pprint
import pdb
from notion_client import Client

load_dotenv()

NOTION_TOKEN = os.getenv('NOTION_TOKEN')
notion = Client(auth=NOTION_TOKEN)
list_users_response = notion.users.list()
pprint(list_users_response)
pdb.set_trace()