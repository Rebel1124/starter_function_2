# from appwrite.client import Client
# from appwrite.services.users import Users
# from appwrite.exception import AppwriteException
# import os

# # This Appwrite function will be executed every time your function is triggered
# def main(context):
#     # You can use the Appwrite SDK to interact with other services
#     # For this example, we're using the Users service
#     client = (
#         Client()
#         .set_endpoint(os.environ["APPWRITE_FUNCTION_API_ENDPOINT"])
#         .set_project(os.environ["APPWRITE_FUNCTION_PROJECT_ID"])
#         .set_key(context.req.headers["x-appwrite-key"])
#     )
#     users = Users(client)

#     try:
#         response = users.list()
#         # Log messages and errors to the Appwrite Console
#         # These logs won't be seen by your end users
#         context.log("Total users: " + str(response["total"]))
#     except AppwriteException as err:
#         context.error("Could not list users: " + repr(err))

#     # The req object contains the request data
#     if context.req.path == "/ping":
#         # Use res object to respond with text(), json(), or binary()
#         # Don't forget to return a response!
#         return context.res.text("Pong")

#     return context.res.json(
#         {
#             "motto": "Build like a team of hundreds_",
#             "learn": "https://appwrite.io/docs",
#             "connect": "https://appwrite.io/discord",
#             "getInspired": "https://builtwith.appwrite.io",
#         }
#     )



# from main import client,db_id ,db_collection_id
# from db import project_id, api_key, db_id, db_collection_id
from appwrite.client import Client
from appwrite.services.databases import Databases

# from pydantic import BaseModel, Field
from datetime import datetime

import os
import random
import secrets

# class TodoCreateModel(BaseModel):
#     title: str
#     content: str
#     date_added: str =Field(default = datetime.now().date())

def taskNumDef():
    taskNumA = random.randint(5, 9)
    taskNumB = random.randint(5, 9)

    num = taskNumA + taskNumB

    return num



def main(context):
    

    client = Client()

    project_id = os.environ['APPWRITE_PROJECT_ID']
    api_key = os.environ['APPWRITE_API_KEY']
    db_id = os.environ['APPWRITE_DB_ID']
    db_collection_id = os.environ['APPWRITE_COLLECTION_ID']

    client = (client
        .set_endpoint('https://cloud.appwrite.io/v1') # Your API Endpoint
        .set_project(project_id)                # Your project ID
        .set_key(api_key)          # Your secret API key
    )

    db = Databases(client)

    try:
        # Fetch all documents
        documents = db.list_documents(db_id, db_collection_id)

        # Loop through and delete each document
        for document in documents['documents']:
            db.delete_document(db_id, db_collection_id, document['$id'])
            # print(f"Deleted document: {document['$id']}")
    except:
        pass


    # taskNum = str(random.randint(4, 9))
    taskNum=taskNumDef()
    dateNow=datetime.now().date()
    dateString = dateNow.strftime('%Y-%m-%d, %H:%M:%S')

    tasks = ['make bed', 'build app', 'go for drive', 'call mum', 'make breakfast', 'go to the beach']
    chooseTask = random.choice(tasks)

    to_do = {
        'title': "Task "+taskNum,
        'content': chooseTask,
        'date_added': dateString
    }

    db.create_document(
        database_id= db_id,
        collection_id= db_collection_id,
        document_id=secrets.token_hex(8),
        data=to_do
    )

    return context.res.empty()