from database.dbc import get_db_con


def get_batch_fee(batch_id):
    db = get_db_con()
    cur = db.cursor()

    cur.execute(
        "SELECT base_fee FROM batches WHERE batch_id=%s",
        (batch_id,)
    )

    fee = cur.fetchone()

    cur.close()
    db.close()

    return fee["base_fee"]


def insert_enrollment(student_id, batch_id, fee):
    db = get_db_con()
    cur = db.cursor()

    cur.execute("""
        INSERT INTO enrollments
        (
            student_id,
            batch_id,
            base_fee_snapshot,
            discount_amount,
            final_fee,
            status
        )

        VALUES
        (%s,%s,%s,%s,%s,%s)
    """,
    (
        student_id,
        batch_id,
        fee,
        0,
        fee,
        "pending"
    ))

    enrollment_id = cur.lastrowid

    db.commit()

    cur.close()
    db.close()

    return enrollment_id


def insert_payment(enrollment_id, amount, txn_id):
    db = get_db_con()
    cur = db.cursor()

    cur.execute("""
        INSERT INTO payments
        (
            enrollment_id,
            amount,
            txn_id,
            status
        )

        VALUES
        (%s,%s,%s,%s)
    """,
    (
        enrollment_id,
        amount,
        txn_id,
        "success"
    ))

    db.commit()

    cur.close()
    db.close()


def get_student_courses(student_id):

    db = get_db_con()

    cur = db.cursor()

    cur.execute("""

    SELECT

    c.course_id,

    c.name AS course_name,

    b.batch_id,

    b.name AS batch_name,

    b.image,

    b.start_date,

    b.end_date

    FROM enrollments e

    JOIN batches b
    ON e.batch_id=b.batch_id

    JOIN courses c
    ON b.course_id=c.course_id

    WHERE

    e.student_id=%s

    AND e.status='active'

    """,(student_id,))

    rows = cur.fetchall()

    cur.close()

    db.close()

    return rows
def activate_enrollment(enrollment_id):

    db = get_db_con()
    cur = db.cursor()

    cur.execute(
        "UPDATE enrollments SET status='active' WHERE enrollment_id=%s",
        (enrollment_id,)
    )

    db.commit()

    cur.close()
    db.close()