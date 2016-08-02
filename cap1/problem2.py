def create_values():
    sales_record = [155, 182, 192, 220, 320, 110, 166, 185, 190]
    *traiding_qtr, current_qtr = sales_record
    middle_qtr = sum(traiding_qtr) / len(traiding_qtr)
    print(middle_qtr, current_qtr)

create_values()
