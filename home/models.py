from email import message
import email
from email.policy import default
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User,auth

# Create your models here.
# models me class bante hain jise table ka code bhi kaha ja skta hain 
# class banne par make migration wala code enter karna padta hain table banane ya edit karne k liye
#

class Book_Category(models.Model):
    cat_id = models.CharField(max_length=10,null=True)
    category_name =models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.category_name


class Book_Deatails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=200,null =True ,blank=True)
    book_title = models.CharField(max_length=200,null =True ,blank=True)
    isbn = models.CharField(max_length=13,null=True ,blank=True)
    city = models.CharField(max_length=60,null=True ,blank=True)
    book_author = models.CharField(max_length=200,null =True ,blank=True)
    book_category = models.CharField(max_length=200,null =True ,blank=True)
    book_language = models.CharField(max_length=200,null =True ,blank=True)
    book_des = models.TextField(null =True ,blank=True)
    is_active = models.BooleanField(null= True ,blank=True ,default= False)
    book_img = models.ImageField(upload_to='bookimg/', default='bookimg/default.jpg', max_length=200,null =True ,blank=True)

    def _str_(self):
        return str(self.id)



class SendRequest(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book_Deatails,on_delete=models.CASCADE)
    book_owner = models.CharField(max_length=200)
    message = models.TextField(null = True, blank=True)

REQ_STATUS =(
    ('pending','pending'),
    ('accepted','accepted'),
    ('rejected','rejected'),
    ('success','success'),
)

class Book_request(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=2)
    book_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    req_date = models.DateTimeField(auto_now_add=True)
    req_status = models.CharField(max_length=200,default='pending' ,choices = REQ_STATUS)



MSG_STATUS =(
    ('pending','pending'),
    ('accepted','accepted'),
    ('denied','denied'),
)

class Send_Message(models.Model):
    cuser = models.CharField(max_length=255)
    ruser = models.CharField(max_length=255)
    book = models.ForeignKey(Book_Deatails,on_delete=models.CASCADE,null=True,blank=True)
    msg = models.TextField(null=True,blank=True)
    status = models.CharField(max_length=50, default='pending', choices=MSG_STATUS)
    postdate = models.DateTimeField(auto_now_add=True)

class Donate_Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200, null=True, blank=True)
    qtybook = models.CharField(max_length=200, null=True, blank=True)
    address = models.TextField( null=True, blank=True)
    contact_no = models.CharField(max_length=20,null=True, blank=True)
    pickdate = models.DateField( null=True, blank=True)
    

# class Book_Deatails(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     email = models.CharField(max_length=200,null =True ,blank=True)
#     book_title = models.CharField(max_length=200,null =True ,blank=True)
#     isbn = models.CharField(max_length=13,null=True ,blank=True)
#     city = models.CharField(max_length=60,null=True ,blank=True)
#     book_author = models.CharField(max_length=200,null =True ,blank=True)
#     book_category = models.CharField(max_length=200,null =True ,blank=True)
#     book_language = models.CharField(max_length=200,null =True ,blank=True)
#     book_des = models.TextField(null =True ,blank=True)
#     is_active = models.BooleanField(null= True ,blank=True ,default= False)
#     book_img = models.ImageField(upload_to='bookimg/', default='bookimg/default.jpg', max_length=200,null =True ,blank=True)

#     def _str_(self):
#         return str(self.id)
