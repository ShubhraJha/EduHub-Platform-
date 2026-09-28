from db_models.student_model import get_student

def is_profile_complete(student_id):
    student = get_student(student_id)

    if not student:
        return False

    if student["stu_name"] == "":
        return False

    return True