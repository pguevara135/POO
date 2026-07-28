class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total
    
    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        title = f'{self.name:*^30}\n'
        items = ''
        for item in self.ledger:
            desc = item['description'][:23]
            amt = f"{item['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"
            total = f"Total: {self.get_balance():.2f}"
        return title + items + total
    

def create_spend_chart(categories):
    title = "Percentage spent by category"

    spent = []
    for cat in categories:
        total = 0
        for item in cat.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        spent.append(total)
    
    total_spent = sum(spent)

    percentages = [(s / total_spent) * 100 for s in spent]

    percentages = [int(p // 10 * 10) for p in percentages]

    chart = title

    for i in range(100, -1, -10):
        line = f"{i:>3}| "
        for p in percentages:
            line += "o  " if p >= i else "   "
        chart += line + "\n"
    
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(cat.name) for cat in categories)
    
    for i in range(max_len):
        line = "     "
        for cat in categories:
            if i < len(cat.name):
                line += cat.name[i] + "  "
            else:
                line += "   "
        chart += line
        if i < max_len - 1:
            chart += "\n"
    
    return chart

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)