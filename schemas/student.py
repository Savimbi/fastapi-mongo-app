

def student_entity(item) -> dict:
    return {
        'id': str(item['_id']),
        'name': item['student_name'],
        'email': item['student_email'],
        'phone': item['student_phone']
    }

def list_of_student_entity(db_item_list) -> list:
    student_list =[]
    for item in db_item_list:
        student_list.append(student_entity(item))
    return  student_list