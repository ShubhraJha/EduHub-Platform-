from database.dbc import get_db_con


def get_lectures(batch_id):

    db = get_db_con()
    cur = db.cursor()

    cur.execute("""

        SELECT *

        FROM lectures

        WHERE batch_id=%s

        ORDER BY lecture_no

    """,(batch_id,))

    rows = cur.fetchall()

    cur.close()
    db.close()

    return rows