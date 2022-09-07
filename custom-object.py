# Python Object representing a purchase for a given amount

class Purchase(object):
    def __init__(self, amount):
        self.amount = amount

    def calculateTax (self, taxPercent):
        return self.amount * taxPercent/100.0

    def calculateTip(self, tipPercent):
        return self.amount * (tipPercent/100.0)

    def calculateTotal(self, taxPercent, tipPercent):
        return self.amount * (1 + taxPercent/100.0 + tipPercent/100.0)


# Create a purchase object given an amount
purchase = Purchase(100.0)

# Set the tax and tip percentages/variables
taxPercent = 7.5
tipPercent = 20.0

# calculating Tax and Tip
tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)

#Displaying format
print('Tax', tax)
print('Tip', tip)
print('Total:', purchase.calculateTotal(taxPercent, tipPercent))