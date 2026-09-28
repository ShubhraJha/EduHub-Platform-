from database.dbc import get_db_con


# =========================
# DASHBOARD STATISTICS
# =========================

def get_admin_stats():

    db = get_db_con()
    cur = db.cursor()

    stats = {}

    cur.execute("SELECT COUNT(*) AS total FROM users")
    stats["users"] = cur.fetchone()["total"]

    cur.execute("SELECT COUNT(*) AS total FROM students")
    stats["students"] = cur.fetchone()["total"]

    cur.execute("SELECT COUNT(*) AS total FROM teachers")
    stats["teachers"] = cur.fetchone()["total"]

    cur.execute("SELECT COUNT(*) AS total FROM courses")
    stats["courses"] = cur.fetchone()["total"]

    cur.execute("SELECT COUNT(*) AS total FROM batches")
    stats["batches"] = cur.fetchone()["total"]

    cur.execute("SELECT COUNT(*) AS total FROM subjects")
    stats["subjects"] = cur.fetchone()["total"]

    cur.execute("SELECT COUNT(*) AS total FROM enrollments")
    stats["enrollments"] = cur.fetchone()["total"]

    cur.execute("SELECT COUNT(*) AS total FROM payments")
    stats["payments"] = cur.fetchone()["total"]

    cur.close()
    db.close()

    return stats


# =========================
# ALL STUDENTS
# =========================
def get_all_students():

    db = get_db_con()
    cur = db.cursor()

    cur.execute("""
        SELECT
            s.student_id,
            s.stu_name,
            s.student_phone,
            s.parent_phone,
            s.gender,
            s.dob
        FROM students s
        ORDER BY s.student_id DESC
    """)

    students = cur.fetchall()

    cur.close()
    db.close()

    return students



# =========================
# ALL ENROLLMENTS
# =========================

def get_all_enrollments():

    db = get_db_con()
    cur = db.cursor()

    cur.execute("""
        SELECT
            e.enrollment_id,
            e.student_id,
            s.stu_name,
            e.batch_id,
            b.name AS batch_name,
            e.base_fee_snapshot,
            e.discount_amount,
            e.final_fee,
            e.status,
            e.enrolled_at
        FROM enrollments e

        LEFT JOIN students s
        ON e.student_id = s.student_id

        LEFT JOIN batches b
        ON e.batch_id = b.batch_id

        ORDER BY e.enrollment_id DESC
    """)

    enrollments = cur.fetchall()

    cur.close()
    db.close()

    return enrollments


# =========================
# ALL COURSES
# =========================

def get_all_courses():

    db = get_db_con()
    cur = db.cursor()

    cur.execute("""
        SELECT
            c.course_id,
            c.name AS course_name,
            cat.category_name,
            COUNT(b.batch_id) AS batch_count
        FROM courses c

        LEFT JOIN categories cat
        ON c.category_id = cat.category_id

        LEFT JOIN batches b
        ON c.course_id = b.course_id

        GROUP BY
            c.course_id,
            c.name,
            cat.category_name

        ORDER BY c.course_id DESC
    """)

    courses = cur.fetchall()

    cur.close()
    db.close()

    return courses


# =========================
# ALL BATCHES
# =========================

def get_all_batches():

    db = get_db_con()
    cur = db.cursor()

    cur.execute("""
        SELECT
            b.batch_id,
            b.name AS batch_name,
            b.base_fee,
            b.start_date,
            b.end_date,
            c.name AS course_name
        FROM batches b

        JOIN courses c
        ON b.course_id = c.course_id

        ORDER BY b.batch_id DESC
    """)

    batches = cur.fetchall()

    cur.close()
    db.close()

    return batches


# =========================
# ALL TEACHERS
# =========================

def get_all_teachers():

    db = get_db_con()
    cur = db.cursor()

    cur.execute("""
        SELECT
            t.teacher_id,
            t.name,
            t.phone_number,
            t.experience_yrs,
            t.qualifications
        FROM teachers t

        ORDER BY t.teacher_id DESC
    """)

    teachers = cur.fetchall()

    cur.close()
    db.close()

    return teachers
# =========================
# ALL PAYMENTS
# =========================

def get_all_payments():

    db = get_db_con()
    cur = db.cursor()

    cur.execute("""
        SELECT
            p.payment_id,
            p.enrollment_id,
            p.amount,
            p.txn_id,
            p.status,
            e.student_id,
            s.stu_name,
            b.name AS batch_name
        FROM payments p

        LEFT JOIN enrollments e
        ON p.enrollment_id = e.enrollment_id

        LEFT JOIN students s
        ON e.student_id = s.student_id

        LEFT JOIN batches b
        ON e.batch_id = b.batch_id

        ORDER BY p.payment_id DESC
    """)

    payments = cur.fetchall()

    cur.close()
    db.close()

    return payments