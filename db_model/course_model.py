from db.connection import get_db_con

def get_full_data():
    db = get_db_con()
    cur = db.cursor()

    cur.execute("""
    SELECT 
    c.category_id, c.category_name,
    co.course_id, co.name AS course_name,
    b.batch_id, b.name AS batch_name,
    b.base_fee,
    b.start_date,
    b.end_date
FROM categories c
LEFT JOIN courses co ON c.category_id = co.category_id
LEFT JOIN batches b ON co.course_id = b.course_id
ORDER BY c.category_id
    """)

    rows = cur.fetchall()

    cur.close()
    db.close()
    return rows