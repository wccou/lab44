#coding=utf-8
from django.shortcuts import render
from bname.models import Book
from writer.models import Author
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
	bname_list = Book.objects.all()
	return render_to_response('index.html',{'bname_list':bname_list})
	
def search_form(request):
	bname_list = Book.objects.all()
	return render_to_response('search_form.html',{'bname_list':bname_list})
	
def search(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		writers = Author.objects.filter(Name__icontains=q)
		for i in writers:
			books = Book.objects.filter(AuthorID__icontains=i.AuthorID)
			return render_to_response('search_results.html',{'books':books,'query':q})
	return HttpResponse('没有该作者！')
	
def book(request,bookISBN):
	book_list=Book.objects.all()
	for book in book_list:
		if book.ISBN==bookISBN :
			return render_to_response('bookinfor.html',{'book':book})
			
def Autho(request,bookAuthorID):
	Author_list = Author.objects.all()
	for Au in Author_list:
		if Au.AuthorID==bookAuthorID:
			return render_to_response('Authorinfor.html',{'Au':Au})
			
			
def delete(request,bookISBN):
	book_list = Book.objects.all()
	for book in book_list:
		if book.ISBN==bookISBN:
			Book.objects.get(ISBN=bookISBN).delete()
			return  render_to_response('deleteresult.html')

def change(request,bookISBN):
	book_list = Book.objects.all()
	for book in book_list:
		if book.ISBN==bookISBN:
			return render_to_response('change.html',{'book':book})
	#book_list=Book.objects.all()
	# for book in book_list:
		# if book.ISBN==bookISBN:
			
			# Book.objects.filter(ISBN=bookISBN).update(ISBN=request.GET['I'])
			# Book.objects.filter(ISBN=bookISBN).update(Title=request.GET['T'])
			# Book.objects.filter(ISBN=bookISBN).update(AuthorID=request.GET['ID'])
			# Book.objects.filter(ISBN=bookISBN).update(Publisher=request.GET['Per'])
			# Book.objects.filter(ISBN=bookISBN).update(PublishDate=request.GET['PD'])
			# Book.objects.filter(ISBN=bookISBN).update(Price=request.GET['Price'])
			#return render_to_response('search_form.html')
def update(request,bookISBN):
	book_list = Book.objects.all()
	for p in book_list:
		if p.ISBN==bookISBN:
			p.ISBN = request.GET.get('I','')
			p.Title = request.GET.get('T','')
			p.AuthorID = request.GET.get('ID','')
			p.Publisher = request.GET.get('Per','')
			p.PublishDate = request.GET.get('PD','')
			p.Price = request.GET.get('Price','')
			p.save()
			return  render_to_response('changeresult.html')
	
def addauthor(request):
	return  render_to_response('adauthor.html')
	
def addbook(request):
	return  render_to_response('adbook.html')
def adb(request):
	p = Book()
	p.ISBN = request.GET.get('I','')
	p.Title = request.GET.get('T','')
	p.AuthorID = request.GET.get('ID','')
	p.Publisher = request.GET.get('Per','')
	p.PublishDate = request.GET.get('PD','')
	p.Price = request.GET.get('Price','')
	Author_list = Author.objects.all()
	for i in Author_list:
		if i.AuthorID == p.AuthorID:
			p.save()
			return  render_to_response('adbresult.html')
	p.save()
	return 	render_to_response('adauthor.html',{'ID':p.AuthorID})
	
def ada(request):
	q = Author()
	q.AuthorID = request.GET.get('I','')
	q.Name = request.GET.get('N','')
	q.Age = request.GET.get('A','')
	q.Country = request.GET.get('C','')
	q.save()
	return  render_to_response('adaresult.html')
	
def showauthor(request):
	Author_list = Author.objects.all()
	return render_to_response('showauthor.html',{'Author_list':Author_list})
	
def showbook(request):
	book_list = Book.objects.all()
	return render_to_response('showbook.html',{'book_list':book_list})
	