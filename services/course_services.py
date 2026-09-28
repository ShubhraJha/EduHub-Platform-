def build_structure(rows):
    data = {}

    for r in rows:
        cat_id = r["category_id"]
        course_id = r["course_id"]

        if cat_id not in data:
            data[cat_id] = {
                "name": r["category_name"],
                "courses": {}
            }

        if course_id:
            if course_id not in data[cat_id]["courses"]:
                data[cat_id]["courses"][course_id] = {
                    "name": r["course_name"],
                    "batches": []
                }

            if r["batch_id"]:
                data[cat_id]["courses"][course_id]["batches"].append({
                    "id": r["batch_id"],
                    "name": r["batch_name"],
                    "image": r["image"],
                    "price": r["base_fee"],
                    "start": r["start_date"],
                    "end": r["end_date"]
})

    return data 