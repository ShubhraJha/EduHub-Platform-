from database.dbc import get_db_con

def get_student(student_id):
    db = get_db_con()
    cur = db.cursor()

    cur.execute(
        "SELECT * FROM students WHERE student_id=%s",
        (student_id,)
    )

    student = cur.fetchone()

    cur.close()
    db.close()

    return student


def create_student(student_id, name, student_phone,
                   parent_phone, gender, dob, address):

    db = get_db_con()
    cur = db.cursor()

    cur.execute("""
        INSERT INTO students
        (student_id, stu_name, student_phone,
         parent_phone, gender, date_of_birth, address)

        VALUES(%s,%s,%s,%s,%s,%s,%s)
    """,
    (
        student_id,
        name,
        student_phone,
        parent_phone,
        gender,
        dob,
        address
    ))

    db.commit()

    cur.close()
    db.close()


    
