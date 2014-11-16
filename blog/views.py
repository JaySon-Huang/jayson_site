#coding=utf-8
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.http import Http404

from models import BlogPost, BlogCatalogue
from mysite.views import render_default

from markdown import markdown

# Create your views here.
def blog(request, blog_id):
	global profile_list

	cata_list = BlogCatalogue.objects.all()

	if blog_id is not None:
		try :
			record = BlogPost.objects.get(id=blog_id)
			record.body = markdown(unicode(record.body))
			record.page_view += 1
			BlogPost.objects.filter(id=record.id).update(page_view=record.page_view)
			for tag in record.tags.all():
				print "Tag:",tag
		except BlogPost.DoesNotExist :
			raise Http404
	else :
		raise Http404

	return render_default(
		'blog.html',
		{
		'blog'      : record,
		'cata_list' : cata_list,
		},
		request
	)
