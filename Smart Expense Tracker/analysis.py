from collections import defaultdict
import matplotlib.pyplot as plt

def monthly_summary(data, month):
    total = 0
    for exp in data:
        if exp["date"].startswith(month):
            total += exp["amount"]
    return total

def category_summary(data, month): 
    categories = defaultdict(float)

    for exp in data:
        if exp["date"].startswith(month):
            categories[exp["category"]] += exp["amount"]

    return categories

def highest_category(categories):
    return max(categories, key=categories.get)

def show_pie_chart(categories):
    labels = categories.keys()
    values = categories.values()

    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Expense Distribution")
    plt.show()
