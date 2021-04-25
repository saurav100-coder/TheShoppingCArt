from django.db import models

SEASON_CHOICES = (
    ('0', "All Season"),
    ('1', "Spring 1 March"),
    ('2', "Summer 1 June"),
    ('3', "Autumn 1 September"),
    ('4', "Winter 1 December"),
)

CATEGORY_CHOICES = (
    ('Electronics', 'Electronics'),
    ('TV & Appliances', 'TV & Appliances'),
    ('Men', 'Men'),
    ('Women', 'Women'),
    ('Baby & Kids', 'Baby & Kids'),
    ('Computers', 'Computers'),
    ('Phones & Tablets', 'Phones & Tablets'),
    ('Books', 'Books'),
    ('Accessories', 'Accessories'),
    ('Others', 'Others'),
    ('More', 'More'),
)

electronic_choices = (
    ('Washing Machine', 'Washing Machine'),
    ('Refrigerators', 'Refrigerators'),
    ('Mixer Grinder & Juicer', 'Mixer Grinder & Juicer'),
    ('Others', 'Others'),
)

men_choices = (
    ('Jeans', 'Jeans'),
    ('Trousers', 'Trousers'),
    ('Shirts', 'Shirts'),
    ('T-Shirts', 'T-Shirts'),
    ('Shoes', 'Shoes'),
    ('Accessories', 'Accessories'),
)

women_choices = (
    ('Saree', 'Saree'),
    ('Jeans', 'Jeans'),
    ('Tops', 'Tops'),
    ('Shirts', 'Shirts'),
    ('T-Shirts', 'T-Shirts'),
    ('Shoes', 'Shoes'),
    ('Accessories', 'Accessories'),
)

kids_choices = (
    ('0', 'upto 2yrs'),
    ('1', 'upto 5yrs'),
    ('2', 'upto 10yrs'),
    ('3', 'upto 15yrs'),
    ('4', 'above 15yrs'),
)

computer_choices = (
    ('PC', 'PC'),
    ('Laptops', 'Laptops'),
    ('Accessories', 'Accessories'),
    ('Others', 'Others'),
)

class Seller(models.Model):
    seller_id = models.IntegerField(
        primary_key=True, blank=False, auto_created=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12)
    description = models.TextField(max_length=500)
    address = models.TextField(max_length=500)
    password = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.seller_id

class Customer(models.Model):
    customer_id = models.IntegerField(
        primary_key=True, blank=False, auto_created=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.TextField(max_length=500)
    password = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True, editable=False)

    def __str__(self):
        return str(self.customer_id)


class Product(models.Model):
    product_id = models.IntegerField(
        primary_key=True, blank=False, auto_created=True)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.IntegerField(blank=False)
    is_discount = models.BooleanField(default=False)
    discount = models.IntegerField()
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    season = models.CharField(max_length=100)
    year = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'product/', blank=True)   #need to install pillow to store image

    def __str__(self):
        return self.product_id


class Order(models.Model):
    orderid = models.IntegerField(
        primary_key=True, blank=False, auto_created=True)
    status1 = models.CharField(max_length=150)
    status2 = models.CharField(max_length=150)
    status3 = models.CharField(max_length=150)
    status4 = models.CharField(max_length=150)
    invoice = models.IntegerField()
    no_of_items = models.IntegerField()
    order_date = models.DateField(auto_now_add=True)
    shipping_date = models.DateField(auto_now_add=False)
    shipping_address = models.TextField(max_length=250)
    is_shipped = models.BooleanField(default=False)

    productid = models.ForeignKey(Product, on_delete=models.CASCADE)
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sellerid = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.orderid
