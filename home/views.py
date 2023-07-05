from multiprocessing import context
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from home.models import *
from django.db.models import Q
from django.core.files.storage import FileSystemStorage

from home.models import Book_Category, Book_Deatails
# Create your views here.
# models.py me banaye hue class/table ke function yaha bante hain jiske ander models k class k 
# objects bante hain aur objects ki help se tables me se data fetch aur store karaya jata hain
#  
#  


def index(request):
    # return HttpResponse("hello world")
    return render(request,"index.html")





def books(request):
    books = Book_Deatails.objects.filter(is_active = True)
    # user = auth_user.objects.filter(is_active = True)
       
    if 'q' in request.GET:

        q = request.GET['q']

        squery = Q(Q(book_title__icontains = q) | Q(book_author__icontains = q) | Q(city__icontains = q))
        books = Book_Deatails.objects.filter(squery)

    # cat aur CATID wali query by default run hogi

    cat = Book_Category.objects.all()
    CATID = request.GET.get('categories')

    # books wale page pe category ke bar pe click karne par if CATID wale block me enter karega 
    # aur category wisw books fetch karega

    if CATID:
        catName = Book_Category.objects.get(id = CATID).category_name
        books = Book_Deatails.objects.filter(Book_Category = CATID)
        return render(request,'Books.html',{'books':books,'Book_Category':cat,'catName':catName})
    

    # user_id = Book_Deatails.objects.get(user_id )
    # user_email = User.objects.get(id = user_id).email
    return render(request,'Books.html',{"books":books,'Book_Category':cat})



def book_details(request,bid):
    if request.method =="GET":  
         
         books = Book_Deatails.objects.all()
         book = books.get(id = bid)

    if request.method =='POST':
        cuser = request.POST.get('cuser')
        ruser = request.POST.get('ruser')
        selectedbook = request.POST.get('selectedbook')
        msgText = request.POST.get('message')
        print(cuser)
        print(ruser)
        print(selectedbook)
        print(msgText)
        messages.success(request,"hiiiiiiiiiiiiiiiiiiiiiiiiiiii")

    return render(request,'book_details.html',{"book":book})

def sendmsg(request):
    if request.user.is_authenticated:
  
        if request.method =='POST':
            cuser = request.POST.get('cuser')
            ruser = request.POST.get('ruser')
            selectedbook = request.POST.get('selectedbook')
            selectedbookobj = Book_Deatails.objects.get(id=selectedbook)
            msgText = request.POST.get('message')
    

            msgobj = Send_Message.objects.create(
                cuser = cuser,
                ruser = ruser,
                book = selectedbookobj,
                msg = msgText,
            )

            msgobj.save()
            messages.success(request,"Request Sent Successfully")
            return redirect("/profile/")
            
        return redirect("/books/")
    else:
        messages.error(request, "Login to Continue...")
        return redirect("/login/")
        

def signup(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.create_user(
            first_name = fname,
            last_name = lname,
            username = username,
            email = email,
            password = password,
        )

        user.save()
        messages.success(request,"You Have Registered Successfully....")


    return render(request,'signup.html')

def edit(request):
    edit_user = User.objects.get(id = request.POST.get('userid'))
    return render(request,'edit.html',{"eu":edit_user})

def edit_process(request):
    if request.method =="POST":
        edituser = User(
            id = request.POST.get('userid'),
            username = request.POST.get('username'),
            first_name = request.POST.get('fname'),
            last_name = request.POST.get('lname'),
            email = request.POST.get('email'),
            password = request.POST.get('password'),

        )

        edituser.save()
        return redirect('/profile/')

def login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            User.username = username
            messages.success(request,User.username + '  You Have Login Successfully....')
            return redirect('/')
        else:
            messages.error(request,'Worng Username or Password....')

    return render(request,'login.html')

def request(request):
    if request.user.is_authenticated:

        if request.method =="POST":
            reqbook = request.POST.get('reqbook')
            reqauth = request.POST.get('reqauthor')

            reqbook = Book_request(
                user = request.user,
                book_name = reqbook,
                author_name = reqauth,
            )

            reqbook.save()
            messages.success(request,'Book Request Sent Successfully....')
        return render(request,'request.html')
    else:
        messages.error(request,"Please Login To Request a Book....")
        return redirect('/login/')

def add_book(request):
    user = request.user
    if user.is_authenticated:
       

        if request.method == 'POST':
           
            if request.FILES.get('book_img'):
                pro_pic = request.FILES.get('book_img')
                fs = FileSystemStorage()
                imgUrl = fs.save( 'bookimg/'+pro_pic.name,pro_pic) 


                book_title = request.POST.get('book_title')
                book_author = request.POST.get('book_author')
                book_category = request.POST.get('book_category')
                book_language = request.POST.get('book_language')
                book_des = request.POST.get('book_des')
                isbn = request.POST.get('isbn')
                city = request.POST.get('city')
              
                emailid = User.objects.get(username = request.user).email
                
                book = Book_Deatails(
                    user = request.user,
                    email = emailid,
                    book_title = book_title,
                    book_author = book_author,
                    book_category = book_category,
                    book_language = book_language,
                    book_des = book_des,
                    book_img =imgUrl,
                    isbn = isbn,
                    city = city
                )
                book.save()
                messages.success(request,"Book Added Successfully....")
                return redirect('add_book')
            else:
                book_title = request.POST.get('book_title')
                book_author = request.POST.get('book_author')
                book_category = request.POST.get('book_category')
                book_language = request.POST.get('book_language')
                book_des = request.POST.get('book_des')
                isbn = request.POST.get('isbn')
                city = request.POST.get('city')
              

                book = Book_Deatails(
                    user = request.user,
                    email = emailid,
                    book_title = book_title,
                    book_author = book_author,
                    book_category = book_category,
                    book_language = book_language,
                    book_des = book_des,
                    isbn = isbn,
                    city = city
                )
                book.save()
                messages.success(request,"Book Added Successfully.... ")
                return redirect('add_book')

    else:
        messages.error(request,"Please Login To Add a Book....")
        return redirect('/login/')

    categories = Book_Category.objects.all()
    return render(request,'add_book.html',{'book_category':categories})    



def profile(request):
    user = request.user
    reqbookcount = Book_request.objects.filter(user = user).count()
    addbookcount = Book_Deatails.objects.filter(user=  user).count()
    donatebookcount = Donate_Book.objects.filter(user= user).count()
    allbook = Book_Deatails.objects.filter(user=  user).all()
    addbookcountred = Book_Deatails.objects.filter(user=  user,is_active = 1).count()
    msgreq = Send_Message.objects.filter(cuser = request.user.username)
    msgrev = Send_Message.objects.filter(ruser = request.user.username)


    context ={
        "reqbookcount":reqbookcount,
        "addbookcount":addbookcount,
        "donatebookcount":donatebookcount,
        "addbookcountred":addbookcountred,
        "allbook":allbook,
        "msgreq":msgreq,
        "msgrev":msgrev,
        "flag":flag


    }
    return render(request,'profile.html',context)



def user_book_list(request):
    user = request.user
    booklist = Book_Deatails.objects.filter(user = user)
    return render(request,"user_book_list.html",{"booklist":booklist})

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~my shit~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def book_name(request):
#     user = request.user
#     booklist = Book_Deatails.objects.filter(user = user)
#     return render(request,"profile.html",{"booklist":booklist})

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~my shit~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def user_request(request):
    user = request.user
    bookrequest = Book_request.objects.filter(user = user)
    return render(request,"user_request.html",{"bookrequest":bookrequest})

def logout(request):
    auth.logout(request)
    messages.success(request,"You Have Logout Successfully....")
    return redirect('/')       

# to remove the book from profile

# def remove_book(request,sbid): 
#     DELID = sbid
#     delBook = Book_Deatails.objects.filter(id = DELID)
#     delBook.delete() 
#     return redirect('/savedbook/')

bookuid = ""
def active(request):
    global bookuid
    if request.method =='GET':
        bookuid = request.GET.get('book_uid')
        ubook = Book_Deatails.objects.get(id = bookuid)
 
    if request.method == 'POST':
        updatestatus = Book_Deatails(
            id = request.POST.get('id'),
            user = request.user,
            email = request.user.email,
            book_title = request.POST.get('book_title'),
            isbn = request.POST.get('isbn'),
            city = request.POST.get('city'),
            book_author = request.POST.get('book_author'),
            book_category = request.POST.get('book_category'),
            book_language = request.POST.get('book_language'),
            book_des = request.POST.get('book_des'),
            is_active = request.POST.get('is_active'),
            book_img = request.POST.get('book_img'),
        )
        updatestatus.save()
        return redirect('/user_book_list/')
    return render(request,'active.html',{'ubook':ubook})


def donate(request):
    
    # user = request.user
    if request.user.is_authenticated:
        if request.method == 'POST':
            qtybook = request.POST.get('qtybook')
            book_name = request.POST.get('book_name')
            pick_date = request.POST.get('pick_date')
            address = request.POST.get('address')
            contact_no = request.POST.get('contact_no')

            donate = Donate_Book(
                user = request.user,
                book_name = book_name,
                qtybook = qtybook,
                address = address,
                contact_no = contact_no,
                pickdate = pick_date
            )

            donate.save()
            messages.success(request, "Book added in pick-up list Successfully..")
            return redirect('/profile/')

        else:       
            return render(request,'donate.html')
    else:
        messages.error(request, "Please Login To Continue..")
        return redirect('/login/')

    # return render(request, 'donate.html')


def donate_list(request):
    user = request.user
    donate_list = Donate_Book.objects.filter(user=user)
    count = donate_list.count()
    return render(request,"donate_list.html",{"donate_list":donate_list,"count":count})



flag = False
def accepted(request):
    if request.method =='POST':
        reqid = request.POST.get('reqid')
        status = request.POST.get('accept')
        statusobj = Send_Message.objects.get(id = reqid)
        statusobj.status = status
        statusobj.save()
        return redirect('/profile/')


def deny(request):
    if request.method =='POST':
        reqid = request.POST.get('reqid')
        status = request.POST.get('deny')
        statusobj = Send_Message.objects.get(id = reqid)
        statusobj.status = status
        statusobj.save()
        return redirect('/profile/')

