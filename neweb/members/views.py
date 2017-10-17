# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from django.template import RequestContext
from neweb.views import *
import MySQLdb
import abc, six



###############################################################
################### Strategy Pattern ##########################
###############################################################
###############################################################
class Context:

    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self, request, search_id):
        return self._strategy.searchMem(request, search_id)

###############################################################
@six.add_metaclass(abc.ABCMeta)
class SearchClass():


    @abc.abstractmethod
    def searchMem(self, request, search_id):
        pass
###############################################################

class SearchWithName(SearchClass):


    def searchMem(self, request, search_id):
        conn = dbase()
        cursor = conn.getCursor()
        args = [search_id,]
        s = cursor.callproc("searchMemWithName", args)
        return cursor.fetchall() 

###############################################################
class SearchWithID(SearchClass):

     def searchMem(self, request, search_id):
        conn = dbase()
        cursor = conn.getCursor()
        args = [search_id,]
        s = cursor.callproc("searchMemWithID", args)
        return cursor.fetchall() 

###############################################################
class SearchAll(SearchClass):

     def searchMem(self, request, search_id):
        conn = dbase()
        cursor = conn.getCursor()
        s = cursor.callproc("searchMemAll")
        return cursor.fetchall() 

################################################################
class Member:
    counter=0
    def __init__(self, id, name):
        self.name = name
        self.id = id
        Member.counter += 1
########################################################################################################
def search(request):
    memberList = []
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        if not search_id:
            context = Context(SearchAll())
        elif search_id[0] <= '9' and search_id[0] >= '0':
            context = Context(SearchWithID())
        else:
            context = Context(SearchWithName())
        
        row = context.context_interface(request, search_id)
        for i in row:
            memberList.append(Member(i[0],i[1]))
        return render(request, "members/searchResults.html",context={'member':memberList})    
################################################################################################        
def memberHome(request):
    return render(request, "members/members.html")
################################################################
###############################################################
###############################################################
def addMember(request):
    name = request.POST.get('username', None)
    if not name:
        return render(request, "members/memberForm.html", context={'warning': "Please enter the name of the member"})
    mail = request.POST.get('usermail', None)
    if not mail:
        return render(request, "members/memberForm.html", context={'warning': "Please enter the E-mail address of the member"})
    cell_no = request.POST.get('contactno', None)
    if not cell_no:
        return render(request, "members/memberForm.html", context={'warning': "Please enter the Contact No. of the member"})
    present_ad = request.POST.get('userprad', None)
    permanent_ad = request.POST.get('userpmad', None)
    dept = request.POST.get('userdept', None)
    if not dept:
        return render(request, "members/memberForm.html", context={'warning': "Please enter the name of the Department of the member"})
    designation = request.POST.get('userdesignation', None)
    if not designation:
        return render(request, "members/memberForm.html", context={'warning': "Please enter the Designation of the member"})
    status = request.POST.get('userstat', None)
    member_type = request.POST.get('usertype', None)
    if not member_type:
        return render(request, "members/memberForm.html", context={'warning': "Please enter the type of the member"})
    conn = dbase()
    cursor = conn.getCursor() 
    args = [name,cell_no,present_ad,permanent_ad,designation,dept,status,mail,member_type,]
    s = cursor.callproc("addMember", args)
    conn.commit()    
    cursor.close()
    return render(request, "members/memberSuccess.html", context = {'name': name, 'mail':mail, 'cell_no':cell_no,'present_ad':present_ad,'permanent_ad':permanent_ad,'dept':dept,'designation':designation, 'status': status,'member_type':member_type})
###############################################################
def addMem(request):
    return render(request, "members/memberForm.html", context={'warning': ""})

####################################################################
def deleteMemberPage(request):
    return render(request, "members/deleteMember.html", context={'warning':""})
####################################################################
def updateMemberPage(request):
    return render(request, "members/updateForm.html", context={'warning':""})
####################################################################
def deleteMember(request):
    memberid = request.POST.get('memberid', None)
    if not memberid:
        return render(request, "members/deleteMember.html", context={'warning': "Please enter the id of the member"})
 
    conn = dbase()
    cursor = conn.getCursor()
    cursor.execute ("select * from Accounts where memberID = "+memberid)
    if cursor.rowcount == 0:
        return render(request, "members/deleteMember.html", context={'warning': "Please enter a valid ID"})
    else:
        row = cursor.fetchone()
        return render(request, "members/confirmDelete.html", context = {'name': row[1], 'memberid':row[0],'designation':row[5],'dept':row[6]})
##########################################################
def deleteMem(request):
    memberid = request.POST.get('memberid', None)
    if not memberid:
        return render(request, "members/deleteMember.html", context={'warning': "Please enter the id of the member"})
    conn = dbase()
    cursor = conn.getCursor()
    args = [memberid,]
    s = cursor.callproc("deleteMember", args)
    conn.commit()    
    cursor.close()
    return render(request, "members/deleteSuccess.html")
###################################################################
def updateMember(request):
    memberid = request.POST.get('memberid', None)
    if not memberid:
        return render(request, "members/updateForm.html", context={'warning': "Please enter the id of the member"})
    conn = dbase()
    cursor = conn.getCursor()
    cursor.execute ("select * from Accounts where memberID = "+memberid)
    if cursor.rowcount == 0:
        return render(request, "members/updateForm.html", context={'warning': "Please enter a valid ID"})
    row = cursor.fetchone()
    name = request.POST.get('username', None)
    if not name:
        name = row[1]
    mail = request.POST.get('usermail', None)
    if not mail:
        mail = row[8]
    cell_no = request.POST.get('contactno', None)
    if not cell_no:
        cell_no = row[2]
    present_ad = request.POST.get('userprad', None)
    if not present_ad:
	    present_ad = row[3]
    permanent_ad = request.POST.get('userpmad', None)
    if not permanent_ad:
	    permanent_ad = row[4]
    dept = request.POST.get('userdept', None)
    if not dept:
        dept = row[6]
    designation = request.POST.get('userdesignation', None)
    if not designation:
        designation = row[5]
    status = request.POST.get('userstat', None)
    if not status:
        status = row[7]
    member_type = request.POST.get('usertype', None)
    if not member_type:
        member_type = row[10]
    args = [memberid,name,cell_no,present_ad,permanent_ad,designation,dept,status,mail,member_type,]
    s = cursor.callproc("updateMember", args)
    conn.commit()    
    cursor.close()
    return render(request, "members/updateSuccess.html", context = {'name': name, 'mail':mail, 'cell_no':cell_no,'present_ad':present_ad,'permanent_ad':permanent_ad,'dept':dept,'designation':designation, 'status': status,'member_type':member_type})
