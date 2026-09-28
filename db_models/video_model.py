from database.dbc import get_db_con


def get_videos(subject_id):

    db = get_db_con()
    cur = db.cursor()

    cur.execute("""
        SELECT
            video_id,
            title,
            video_link
        FROM videos
        WHERE subject_id=%s
    """, (subject_id,))

    rows = cur.fetchall()

    cur.close()
    db.close()

    return rows