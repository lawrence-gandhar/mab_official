PRODUCT_TYPE = (
    (0, 'GOODS'),
    (1, 'SERVICES'),
    (2, 'BUNDLE'),
)

PRODUCT_TYPE_DICT = {
    0: 'GOODS',
    1: 'SERVICES',
    2: 'BUNDLE',
}
    


UNITS = (
    (0, 'Kilogram'),
    (1, 'Grams'),
    (2, 'Ounce'),
    (3, 'Pound'),
    (4, 'Tons'),
    (5, 'Metric Tons'),
    (6, 'Carat'),
    (7, 'Furlong'),
    (8, 'Inches'),
    (9, 'Foot'),
    (10, 'Yard'),
    (11, 'Mile'),
    (12, 'Meter'),
    (13, 'Millimetres '),
    (14, 'Square Feet'),
    (15, 'Square Metre'),
    (16, 'Centimetre'),
    (17, 'Bucket'),
    (18, 'Bag'),
    (19, 'Bowl'),
    (20, 'Box'),
    (21, 'Card'),
    (22, 'Case'),
    (23, 'Carton'),
    (24, 'Dozen'),
    (25, 'Each'),
    (26, 'Gallon'),
    (27, 'Gross'),
    (28, 'Kit'),
    (29, 'Set'),
    (30, 'Sheet'),
    (31, 'Tube'),
    (32, 'Pack'),
    (31, 'Teaspoon'),
    (33, 'Tablespoon'),
    (34, 'Cup'),
    (35, 'Pint'),
    (36, 'Quart'),
    (37, 'Milliliter'),
    (38, 'Liter'),
)

PRODUCT_STOCK_NOTIFICATION_TRIGGERS = (
    (0, '5 DAYS AGO'),
    (1, '1 WEEK AGO'),
    (2, '10 DAYS AGO'),
    (3, '2 WEEKS AGO'),
    (4, '1 MONTH AGO'),
    (5, '45 DAYS AGO'),
    (6, '2 MONTHS AGO'),
    (7, '3 MONTHS AGO'),
    (8, '6 MONTHS AGO'),
    (9, '1 YEAR AGO'),
)


#****************************************************************************
#   INVOICE FREQUENCY
#****************************************************************************
INVOICE_FREQUENCY = (
    (0, 'WEEKLY'),
    (1, 'MONTHLY'),
    (2, 'QUARTERLY'),
    (2, 'HALF-YEARLY'),
    (2, 'YEARLY'),
)

#****************************************************************************
#   INVOICE TYPE
#****************************************************************************
INVOICE_TYPE = (
    (0, 'One Time'), 
    (1, 'Recurring'),
)


#****************************************************************************
#   SALES ACCOUNT 
#****************************************************************************
SALES_ACCOUNT_DICT = {
    0:"Discount",
    1:"General Income",
    2:"Interest Income",
    3:"Late Fee Income",
    4:"Other Charges",
    5:"Sales",
    6:"Shipping Charges",
}

SALES_ACCOUNT_CHOICES = (
    ("Income",(
            (0, "Discount"),
            (1, "General Income"),
            (2, "Interest Income"),
            (3, "Late Fee Income"),
            (4, "Other Charges"),
            (5, "Sales"),
            (6, "Shipping Charges"),
        ),
    ),
)