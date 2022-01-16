

DataControl_example1 = {
    # SELECT * FROM people WHERE id > 2
    'user': 'winuser',
    'table': 'people',   # your table
    'action': 'select',  # select update delete insert
    'id': '*',
    'chg_type': 'NULL',   # varchar or int or NULL
    'chg_name': 'id',
    'chg_ope': '=',
    'chg_detail': '2'
}

DataControl_example2 = {
    # INSERT INTO people () people (goods, price, ...) VALUES ('dcard', 50, ...)
    'user': 'winuser',
    'table': 'people',
    'action': 'insert',
    'id': 'NULL',
    'chg_type': 'NULL',
    'chg_name': 'NULL',
    'chg_ope': 'NULL',
    'chg_detail': 'NULL'
}

Data_example2 = {
    'goods': 'banana',
    'price': 20,
    'category': '水果',
    'spendTime': '12/25',
    'remark': 'banana pie'
}

DataControl_example3 = {
    # DELETE FROM people WHERE id = 2
    'user': 'winuser',
    'table': 'people',
    'action': 'select',
    'id': '2',
    'chg_type': 'NULL',
    'chg_name': 'NULL',
    'chg_ope': 'NULL',
    'chg_detail': 'NULL'
}

DataControl_example4 = {
    # UPDATE  people SET goods='pineapple' WHERE id = 1
    'user': 'winuser',
    'table': 'people',
    'action': 'select',
    'id': '1',
    'chg_type': 'varchar',   # varchar or int
    'chg_name': 'goods',
    'chg_ope': '=',
    'chg_detail': 'pineapple'
}
