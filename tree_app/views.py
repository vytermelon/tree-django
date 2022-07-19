from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CreateBook,CreateNode
from .models import Book_id, Book_page
import re
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.core.management import call_command
from django.db import models
from django.urls import clear_url_caches
from django.utils.module_loading import import_module
from importlib import reload
from django.apps import apps
from django.contrib import admin
html_tree = ""
level = 0



def home(request):
    db_books = Book_id.objects.all()
    return render(request,'home.html',{
        'books' : db_books
    })

def tree(request,book_id):
    global html_tree,level
    db_user = Book_id.objects.filter(book_id=book_id)
    db_book= Book_page.objects.filter(book_id=book_id)
    html_tree = ""
    level = 0
    render_tree(book_id)
    return render(request,'tree.html',{
        'db_user' : db_user,
        'db_book' : db_book,
        'html' : html_tree
    })
def write_tree(request,node_id, book_id):
    path = get_path_from_node_id(book_id, node_id)
    if request.method == 'POST':
        form = CreateNode(request.POST)
        if form.is_valid():
            node_content = form['node_content'].value()
            branch_content = form['branch_content'].value()
            level = Book_page.objects.filter(book_id=book_id).filter(path=path)
            node_id = Book_page.objects.filter(book_id=book_id).count() + 1
            node_id = "%s:%s" % (book_id,node_id)
            for l in level.values('level'):
                level = l['level']

            next_path = get_next_path(book_id, path, level)
            new_book_page_obj = Book_page.objects.create(username=request.user, content=node_content, path=next_path,
                                                               level=level+1,book_id=book_id, branch_name=branch_content, node_id=node_id)
            return HttpResponseRedirect('/tree/%s' % book_id)
    else:
        form = CreateNode()
    return render(request, 'write_tree.html', {
                            'form': form,
                            'node_id':node_id,
                            'book_id':book_id,
                            }
                  )

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def read_tree(request,node_id, book_id):
    node_id_check = re.compile(r'^\d*:\d*$')
    if not node_id_check.search(node_id):
        node_id = "%s:1" % node_id
    path = get_path_from_node_id(book_id, node_id)
    db_user = Book_id.objects.filter(book_id=book_id)
    db_node= Book_page.objects.filter(book_id=book_id).filter(path=path)
    regex_str = r'^%s-\d*$' % path
    db_node_children = Book_page.objects.filter(book_id=book_id).filter(path__iregex=regex_str)
    return render(request,'read_tree.html',{
        'db_user' : db_user,
        'db_node' : db_node,
        'db_node_children' : db_node_children,
        'room_name': "%s/%i" % (node_id, book_id)
    })
def create(request):
    if request.method == 'POST':
        form = CreateBook(request.POST)
        if form.is_valid():
            #bookname = request.POST.get('book_name')
            bookname = form['book_name'].value()
            node_content = form['node_content'].value()
            book_id = len(Book_id.objects.all())+1
            new_book = Book_id.objects.create(username=request.user, bookname=bookname, book_id=book_id)
            new_book_table_obj = Book_page.objects.create(username=request.user, content=node_content, path=1,
                                                               level=1,book_id=book_id, branch_name='Start',node_id='%s:1' % book_id)
            return HttpResponseRedirect('/')
    else:
        form = CreateBook()
    return render(request, 'create.html', {'form': form})

def get_next_path(book_id, path, level):
    if path.count("-") + 1 == level:
        regex_str = r'^%s-\d*$' % path
        next_path = Book_page.objects.filter(book_id=book_id).filter(path__iregex=regex_str).count() + 1
        return path + "-%s" % next_path
    else:
        return 100

def render_tree(book_id, path='1'):
    global html_tree, level
    cur_branch_name,cur_level = get_cur_branch_level(book_id, path)
    node_id = get_node_id_from_path(book_id, path)
    onclick = "onclick=\"location.href='/write_tree/%s/%i'\"" % (node_id,book_id)
    html_tree += "<li><code><button %s>%s</button></code>\n" % (onclick, cur_branch_name)
    db_node_children = get_node_children(book_id, path)
    if db_node_children.count() == 0:
        html_tree += "\n</li>"
    else:
        html_tree += "\n<ul>"
        for l in db_node_children.values('path'):
            render_tree(book_id, l['path'])
        html_tree += "\n</ul>"

def get_cur_branch_level(book_id, path):
    cur_branch_level = Book_page.objects.filter(book_id=book_id).filter(path=path)
    cur_branch = [l['branch_name'] for l in cur_branch_level.values('branch_name')]
    cur_level = [l['level'] for l in cur_branch_level.values('level')]
    return cur_branch[0], cur_level[0]

def get_node_children(book_id, path):
    regex_str = r'^%s-\d*$' % path
    return Book_page.objects.filter(book_id=book_id).filter(path__iregex=regex_str).order_by('level','path')

def get_path_from_node_id(book_id,node_id):
    cur_node_id = Book_page.objects.filter(book_id=book_id).filter(node_id=node_id)
    cur_path = [l['path'] for l in cur_node_id.values('path')]
    return cur_path[0]

def get_node_id_from_path(book_id,path):
    cur_path = Book_page.objects.filter(book_id=book_id).filter(path=path)
    cur_node_id = [l['node_id'] for l in cur_path.values('node_id')]
    return cur_node_id[0]
