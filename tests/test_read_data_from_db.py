from utilities.db_helper import DbHelper


def test_db_data(config):

    data = DbHelper.execute_query(config, "SELECT * FROM automation2026.student_details;")
    print(data)
    for row in data:
        print(row)