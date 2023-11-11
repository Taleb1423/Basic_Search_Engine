from django.shortcuts import render, redirect
from django.conf import settings
import os


# Create your views here.

def success_page(request):
    return render(request, 'success_page.html')

def main(request):

   if request.method == 'POST':

      if 'uploadButton' in request.POST:

         uploaded_file = request.FILES['fileInput']
         # Define the destination folder
         destination_folder = os.path.join(settings.MEDIA_ROOT, 'uploads')

         # Ensure the folder exists, create if not
         os.makedirs(destination_folder, exist_ok=True)

         # Save the file to the destination folder
         destination_path = os.path.join(destination_folder, uploaded_file.name)
         with open(destination_path, 'wb') as destination_file:
            for chunk in uploaded_file.chunks():
               destination_file.write(chunk)
         return redirect('success_page')
   

      elif 'searchButton' in request.POST:
         pass

       

   return render (request, 'engine.html')
