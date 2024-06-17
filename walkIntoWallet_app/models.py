from django.db import models

class Income(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=14, decimal_places = 2)
    source = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self) :
        return f"{self.date} - {self.source} - {self.amount}"

class Expense(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.category} - {self.amount}"
    
class Budget(models.Model):
    month = models.DateField()
    income_goal = models.DecimalField(max_digits=14, decimal_places=2)
    expense_limit = models.DecimalField(max_digits=14, decimal_places=2)

    def __str__(self):
        return f"{self.month} - Income Goal: {self.income_goal}, Expense Limit: {self.expense_limit}"
    