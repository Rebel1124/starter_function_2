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

    # try:
    #     # Fetch all documents
    #     documents = db.list_documents(db_id, db_collection_id)

    #     # Loop through and delete each document
    #     for document in documents['documents']:
    #         db.delete_document(db_id, db_collection_id, document['$id'])
    #         # print(f"Deleted document: {document['$id']}")
    # except:
    #     pass


    try:
        # Step 1: Backup Collection Schema
        # print("Fetching collection details...")
        old_collection = db.get_collection(db_id, db_collection_id)

        # Extract collection details
        collection_name = old_collection["name"]
        attributes = old_collection["attributes"]
        permissions = old_collection["$permissions"]

        # print(f"Collection '{collection_name}' backed up successfully.")

        # Step 2: Delete the Existing Collection
        db.delete_collection(db_id, db_collection_id)
        # print(f"Collection '{collection_name}' deleted successfully.")

        # Step 3: Recreate Collection with the Same Name
        new_collection = db.create_collection(db_id, collection_name, permissions)
        new_collection_id = new_collection["$id"]
        # print(f"New collection created: {new_collection_id}")

        # Step 4: Restore Attributes
        for attr in attributes:
            attr_type = attr["type"]
            key = attr["key"]
            required = attr["required"]
            default = attr.get("default", None)

            if attr_type == "string":
                db.create_string_attribute(db_id, new_collection_id, key, 255, required, default)
            elif attr_type == "integer":
                db.create_integer_attribute(db_id, new_collection_id, key, required, default)
            elif attr_type == "boolean":
                db.create_boolean_attribute(db_id, new_collection_id, key, required, default)
            elif attr_type == "float":
                db.create_float_attribute(db_id, new_collection_id, key, required, default)
            elif attr_type == "email":
                db.create_email_attribute(db_id, new_collection_id, key, required, default)
            elif attr_type == "url":
                db.create_url_attribute(db_id, new_collection_id, key, required, default)
            elif attr_type == "enum":
                db.create_enum_attribute(db_id, new_collection_id, key, attr["elements"], required, default)

            # print(f"Restored attribute: {key} ({attr_type})")

        # print(f"✅ Collection '{collection_name}' has been fully recreated with the same structure!")

    except Exception as e:
        pass




    taskNum = str(random.randint(4, 9))
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