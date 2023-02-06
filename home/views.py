from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect,redirect)
from django.http import HttpResponse
from pytube import YouTube 
def home(request):
	if request.method=='POST':
		url_link=request.POST['links']
		youtubeObject = YouTube(url_link)
		youtubeObject = youtubeObject.streams.get_highest_resolution()
		try:
			result=youtubeObject.download()
		except:
			print("An error has occurred")
		print("Download is completed successfully")
		return HttpResponse("Download is completed successfully In Given Path")

	return render(request,'home/home.html')