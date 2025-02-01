# */15  * * * *

# from appwrite.client import Client
# from appwrite.services.databases import Databases

# # Initialize Appwrite client
# client = Client()
# client.set_endpoint("https://YOUR_APPWRITE_SERVER/v1")  # Update with your Appwrite endpoint
# client.set_project("YOUR_PROJECT_ID")  # Replace with your project ID
# client.set_key("YOUR_API_KEY")  # Replace with your Appwrite API key

# # Initialize database service
# databases = Databases(client)

# # Define database and collection IDs
# DATABASE_ID = "YOUR_DATABASE_ID"
# COLLECTION_ID = "YOUR_COLLECTION_ID"

# try:
#     # Step 1: Backup Collection Schema
#     # print("Fetching collection details...")
#     old_collection = databases.get_collection(DATABASE_ID, COLLECTION_ID)

#     # Extract collection details
#     collection_name = old_collection["name"]
#     attributes = old_collection["attributes"]
#     permissions = old_collection["$permissions"]

#     # print(f"Collection '{collection_name}' backed up successfully.")

#     # Step 2: Delete the Existing Collection
#     databases.delete_collection(DATABASE_ID, COLLECTION_ID)
#     # print(f"Collection '{collection_name}' deleted successfully.")

#     # Step 3: Recreate Collection with the Same Name
#     new_collection = databases.create_collection(DATABASE_ID, collection_name, permissions)
#     new_collection_id = new_collection["$id"]
#     # print(f"New collection created: {new_collection_id}")

#     # Step 4: Restore Attributes
#     for attr in attributes:
#         attr_type = attr["type"]
#         key = attr["key"]
#         required = attr["required"]
#         default = attr.get("default", None)

#         if attr_type == "string":
#             databases.create_string_attribute(DATABASE_ID, new_collection_id, key, 255, required, default)
#         elif attr_type == "integer":
#             databases.create_integer_attribute(DATABASE_ID, new_collection_id, key, required, default)
#         elif attr_type == "boolean":
#             databases.create_boolean_attribute(DATABASE_ID, new_collection_id, key, required, default)
#         elif attr_type == "float":
#             databases.create_float_attribute(DATABASE_ID, new_collection_id, key, required, default)
#         elif attr_type == "email":
#             databases.create_email_attribute(DATABASE_ID, new_collection_id, key, required, default)
#         elif attr_type == "url":
#             databases.create_url_attribute(DATABASE_ID, new_collection_id, key, required, default)
#         elif attr_type == "enum":
#             databases.create_enum_attribute(DATABASE_ID, new_collection_id, key, attr["elements"], required, default)

#         # print(f"Restored attribute: {key} ({attr_type})")

#     # print(f"✅ Collection '{collection_name}' has been fully recreated with the same structure!")

# except Exception as e:
#     pass

