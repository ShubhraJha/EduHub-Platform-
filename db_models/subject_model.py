from database.dbc import get_db_con


def get_subjects(course_id):

    db = get_db_con()
    cur = db.cursor()

    cur.execute("""
        SELECT
            s.subject_id,
            s.name,
            s.image
        FROM course_subject cs

        JOIN subjects s
        ON cs.subject_id = s.subject_id

        WHERE cs.course_id = %s
    """, (course_id,))

    rows = cur.fetchall()

    cur.close()
    db.close()

    return rows