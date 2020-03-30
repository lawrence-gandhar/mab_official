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
    (1, 'grams'),
    (2, 'ounce'),
    (3, 'pound'),
    (4, 'tons'),
    (5, 'metric tons'),
    (6, 'carat'),
    (7, 'furlong'),
    (8, 'Inches'),
    (9, 'foot'),
    (10, 'yard'),
    (11, 'mile'),
    (12, 'Meter'),
    (13, 'Millimetres '),
    (14, 'square feet'),
    (15, 'square metre'),
    (16, 'centimetre'),
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
    (31, 'teaspoon'),
    (33, 'tablespoon'),
    (34, 'cup'),
    (35, 'pint'),
    (36, 'quart'),
    (37, 'milliliter'),
    (38, 'liter'),
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