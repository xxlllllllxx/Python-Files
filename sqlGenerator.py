
import random

list_remarks = [
    "Share Capital",
    "Monthly Dues",
    "Mutual Funds Payable",
    "Certification Fee",
    "Loan Receivable - Pastdue",
    "--------------- - Current",
    "Change Motor - Entrance",
    "--------------- - Motor",
    "Clearance Fee",
    "Miscelleneous Income",
    "Sales Trapal",
    "AIR-Stricker",
    "Penalties",
    "Interest Receivable",
    "Cash in Bank",
    "Rental Fee: Franchise",
    "Transfer Fees",
    "Membership Fee",
    "Seminar Fee"
]

list_deposit = [
    70384.10, 114480, 12920, 3950, 71672, 168919.80, 204875, 2000, 12900, 26304, 3600, 5010, 115828, 22928.20, 80000, 1500, 19200, 1500, 300
]


def generate_random_deposit(base_amount):
    return base_amount + random.randint(-1000, 1000)


statement = "INSERT INTO tbl_payment_details (id, ledger_id, isDownPayment, div_pat, ledger_type, date, reference_no, deposit, penalties, remarks, balance, isDeleted) VALUES \n"
with open('output.sql', 'w') as file:
    statement = ""
    for x in range(12, 13):
        statement += "INSERT INTO tbl_payment_details (id, ledger_id, isDownPayment, div_pat, ledger_type, date, reference_no, deposit, penalties, remarks, balance, isDeleted) VALUES \n"

        arg_date = x
        starting_num = (arg_date - 1) * 20
        sum = 0
        for i in range(19):
            deposit = abs(generate_random_deposit(list_deposit[i]))
            date = f"""2022-{arg_date}-01 00:00:00"""
            statement += f"({starting_num + i + 2}, -1, 0, 0, 'RECAP', '{
                date}', NULL, {deposit}, 0, '{list_remarks[i]}', 0, 0),\n"
            sum = sum + deposit
        formatted_string = "{:.2f}".format(sum)
        statement += f"({starting_num+1}, -1, 0, 0, 'RECAP', '{
            date}', NULL, {formatted_string}, 0, 'Cash On Hand', 0, 0);"
        statement += "\n"

    file.write(statement)
