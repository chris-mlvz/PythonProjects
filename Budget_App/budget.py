from typing_extensions import TypedDict


class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = float()
        self.output = str()

    def deposit(self, amount, description=''):
        self.ledger.append(
            {"amount": amount, "description": description})
        self.balance += amount
        return True

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append(
                {"amount": -amount, "description": description})
            self.balance -= amount
        return self.check_funds(amount)

    def get_balance(self):
        return self.balance

    def transfer(self, amount, another_budget):
        if self.withdraw(amount, "Transfer to " + another_budget.name):
            another_budget.deposit(amount, "Transfer from " + self.name)
        return self.check_funds(amount)

    def check_funds(self, amount):
        if self.balance - amount >= 0:
            return True
        elif self.balance - amount < 0:
            return False

    def __str__(self):
        # * Print Object
        self.output = self.name.center(30, '*') + '\n'
        for i in self.ledger:
            description = "{:.23}".format(i["description"])
            amount = "{:.2f}".format(i["amount"])
            amount = "{:.7}".format(amount)
            self.output += "{:<23}{:>7}\n".format(description, amount)
        self.output += 'Total: ' + str(self.balance)
        return self.output


def create_spend_chart(categories):
    # Variables
    total = float()
    dict_avg_categories = dict()
    dict_names_categories = dict()
    dict_o_categories = dict()
    list_axisx = list()
    list_axisbar = list()
    dashes = str()
    dict_lines_print = dict()
    final_print = str()
    dashes_print = str()
    list_max_name = list()
    len_max_name = int()
    dict_names_print = dict()

    # Total withdraw
    for item in categories:
        total += item.ledger[1]["amount"]

    # % of each categorie and lists
    for item in categories:
        dict_avg_categories[item.name] = round(
            (item.ledger[1]["amount"] * 100) / total)
        dict_names_categories[item.name] = list(item.name[::-1])
        list_temporal_o = []
        for i in range(0, 101, 10):
            if i <= dict_avg_categories[item.name]:
                list_temporal_o.append("o")
                dict_o_categories[item.name] = list_temporal_o
    # # print(dict_avg_categories)
    # # print(dict_o_categories)
    # # print(dict_names_categories)

    # List axisx
    for i in range(0, 101, 10):
        list_axisx.append(i)
        list_axisbar.append('|')
    list_axisx.sort(reverse=True)
    # # print(list_axisx, list_axisbar)

    # list of dahes
    for i in range(len(categories)):
        dashes += '-' * 3
    dashes += '-'
    # # print(list_dashes)

    # * Drawing chart
    first_line = "Percentage spent by category\n"

    for i in range(11):
        axisx_print = "{:>3}{}".format(list_axisx[i], list_axisbar[i])
        dict_lines_print[i] = axisx_print
        for item in categories:
            if list_axisx[i] <= dict_avg_categories[item.name]:
                dict_lines_print[i] += f" {dict_o_categories[item.name].pop()} "
            else:
                dict_lines_print[i] += "   "
        dict_lines_print[i] += " \n"
    # # print(dict_lines_print)

    # Drawing dashes
    dashes_print = f"    {dashes}\n"

    # Drawing names of categories
    list_max_name = [len(item.name) for item in categories]
    len_max_name = max(list_max_name)

    for i in range(len_max_name):
        spaces_print = '    '
        dict_names_print[i] = spaces_print
        for item in categories:
            if len(dict_names_categories[item.name]) > 0:
                dict_names_print[i] += f" {dict_names_categories[item.name].pop()} "
            else:
                dict_names_print[i] += "   "
        dict_names_print[i] += " \n"

    # return final print
    final_print += first_line
    for i in dict_lines_print.values():
        final_print += i
    final_print += dashes_print
    for i in dict_names_print.values():
        final_print += i
    final_print = final_print.rstrip("\n")
    return final_print


# food = Category("Food")
# entertainment = Category('Entertainment')
# # business = Category('Business')
# # # otro = Category('Otro')


# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# food.transfer(20, entertainment)
# actual = str(food)
# expected = f"*************Food*************\ndeposit                 900.00 \nmilk, cereal, eggs, bac -45.67 \nTransfer to Entertainme -20.00 \nTotal: 834.33"
# # assertEqual(actual, expected, 'Expected different string representation of object.')


# print(actual)
# print(expected)
# print(len(actual))
# print(len(expected))

# if actual == expected:
#     print('yeah')
# else:
#     print(('Ouch'))
