# schemas helps to serialize and also convert mongodb format json to our UI needed format
#this goal of this module is to convert the data from the database to the format that the API will return to the client
def student_entity(db_item) -> dict:
    return {
        "id": str(db_item["_id"]),
        "name": db_item["student_name"],
        "email": db_item["student_email"],
        "phone": db_item["student_phone"]
    }

def list_of_students_entity(db_items_list) -> list:
    return [student_entity(item) for item in db_items_list]
    