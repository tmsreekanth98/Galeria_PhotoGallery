from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import Photo
from photogallery.forms import ImportForm
from django.core.files.storage import FileSystemStorage



def index_page(request):
	public_photos = Photo.objects.filter(is_public=True)
	return render(request,'photogallery/index.html',{'public_photos':public_photos})


def register(request):

	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']

			user = authenticate(username=username,password=password)
			login(request,user)

			return redirect('/accounts/profile')

	else:
		form = UserCreationForm()


	return render(request,'photogallery/register.html',{'form':form})


@login_required
def profile(request):
	photos = Photo.objects.filter(username=request.user.username).order_by('date_added')
	photos=photos.reverse()
	
	return render(request,'photogallery/profile.html',{'photos':photos})


@login_required
def delete_photo(request,photo_id):
	photo_obj = Photo.objects.get(id=photo_id)
	if photo_obj.username==request.user.username:
		photo_obj.delete()
	return redirect('../../')

@login_required
def favorite_photo(request,photo_id):
	photo_obj = Photo.objects.get(id=photo_id)
	if photo_obj.is_favorite:
		photo_obj.is_favorite = False
		photo_obj.save()
	else:
		photo_obj.is_favorite = True
		photo_obj.save()
	return redirect('../../')



@login_required
def view_favorite_photo(request,photo_id):
	photo_obj = Photo.objects.get(id=photo_id)
	if photo_obj.is_favorite:
		photo_obj.is_favorite = False
		photo_obj.save()
	else:
		photo_obj.is_favorite = True
		photo_obj.save()
	return redirect('../')



@login_required
def import_photo(request):
	if request.method=='POST':
		import_form = ImportForm(request.POST,request.FILES)
		if import_form.is_valid():
			photo_obj = Photo()

			#getting form data
			title = import_form.cleaned_data['title']
			photo = request.FILES['photo']

			fs = FileSystemStorage()
			filename = fs.save(photo.name,photo)
			file_url = fs.url(filename)
			
			photo_obj.file_format = photo.name.split(".")[1]
			photo_obj.title = title
			photo_obj.url = file_url
			photo_obj.username = request.user.username;
			photo_obj.original_uploader = request.user.username;

			if import_form.cleaned_data['favorite']:
				photo_obj.is_favorite = True
			else:
				photo_obj.is_favorite = False

			if import_form.cleaned_data['public']:
				photo_obj.is_public = True
			else:
				photo_obj.is_public = False

			photo_obj.save()

			return redirect('../')

	else:
		import_form = ImportForm()

	return render(request,'photogallery/import.html',{'import_form':import_form})


@login_required
def archive(request):
	public_photos = Photo.objects.filter(is_public=True).exclude(username=request.user.username)
	return render(request,'photogallery/archive.html',{'public_photos':public_photos})


@ login_required
def view_photo(request,photo_id):

	try:
		photo = Photo.objects.get(id=photo_id)
		error=""
		errorcode=""
		if request.user.username != photo.username and (photo.is_public==False):
			error="403 Error! Access Denied!"
			errorcode = "403"
	except:
		error = "404 Error! Image does not Exist!"
		errorcode="404"
		photo = ""
	return render(request,'photogallery/view.html',{'photo':photo,'error':error,'errorcode':errorcode})


@login_required
def add_photo(request,photo_id):
	photo = Photo.objects.get(id=photo_id)
	newphoto = Photo()
	error = ""
	if photo.is_public:
		newphoto.title = photo.title
		newphoto.url = photo.url
		newphoto.is_favorite = photo.is_favorite
		newphoto.file_format = photo.file_format
		newphoto.date_added = photo.date_added
		newphoto.is_public = photo.is_public
		newphoto.original_uploader = photo.original_uploader

		newphoto.username = request.user.username
		newphoto.is_public = False
		newphoto.save()
	else:
		error = "Photo is already Private!"
	return redirect('/accounts/profile/')