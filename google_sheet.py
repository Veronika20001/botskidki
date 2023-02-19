import gspread


# Указываем путь к JSON
gc = gspread.service_account(filename='test_project.json')
# Открываем тестовую таблицу
sht2 = gc.open_by_url("https://docs.google.com/spreadsheets/d/14NAoZHBGyoolEZD-XFARC1Fm1HbDBaeRV-gkDRe5Usc/edit#gid=0")
worksheet = sht2.sheet1
list_of_lists = worksheet.get_all_values()[1:]  # all rows

categories = worksheet.col_values(9)
trademark = worksheet.col_values(1)[1:]


dict_ = dict()
for category in categories[1:]:
    # print(category)
    for list1 in list_of_lists:
        # print(list1[0])
        if category == list1[8]:
            dict_.update({category: list1[0]})


# print(dict_)

def get_cell(worksheet, name):
    cell_list = worksheet.findall(name)
    return list(worksheet.row_values(a.row) for a in cell_list)
