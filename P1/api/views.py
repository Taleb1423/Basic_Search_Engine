from django.shortcuts import render, redirect
from django.conf import settings
import os

from api.mymodule.elastic import client
from api.mymodule.Pre_processing import index_doc

from api.mymodule.function import func

# Create your views here.

def success_page(request):
    #return render(request, 'success_page.html')

    result = func()
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

         index_doc(uploaded_file.name)

         return redirect('success_page')
   

      elif 'searchButton' in request.POST:
         
         query = request.POST.get('search_term')

         #index_doc("document.txt")

         q= { "query_string" : {"query": query}}


         hits = client.search(index='courses',query=q)

         #print(hits)

         # search_results = []
         

         # for hit in hits['hits']['hits']:
         #    title = hit['_source'].get('Title', '')
         #    objective = hit['_source'].get('Objective', '')
         #    framework = hit['_source'].get('Framework', '')
         #    search_results.append({'title': title, 'objective': objective, 'framework': framework})


         i = 1
         outdoc = []
         scorelist = []
         

         for hit in hits['hits']['hits']:
             score = hit['_score']
             print(score)
             scorelist.append(score)
             print("doc"+str(i)+":\n")
             outfield = []
             for f in hit['_source']:
                 outfield.append(f +": "+ str(hit['_source'][f]))
             i = i + 1
             outdoc.append(outfield)
         i=1     
         outdoc =zip(outdoc,scorelist)
        

         
         
            #  print("Title:", title)
            #  print("Objective:", objective)
            #  print("Framework:", framework)
         

         

         #for key, value in res.items():
         #  print(f'{key}: {value}')
       
         return render(request, 'engine.html', {'outdoc': outdoc})
      


      elif 'searchdocButton' in request.POST:

         docid = ''

         uploaded_file = request.FILES['docin']
         # Define the destination folder
         destination_folder = os.path.join(settings.MEDIA_ROOT, 'uploads')

         # Ensure the folder exists, create if not
         os.makedirs(destination_folder, exist_ok=True)

         # Save the file to the destination folder
         destination_path = os.path.join(destination_folder, uploaded_file.name)
         with open(destination_path, 'wb') as destination_file:
            for chunk in uploaded_file.chunks():
               destination_file.write(chunk)
         
         docid = index_doc(uploaded_file.name)




         qfile= { "more_like_this": {
      "fields": [ "*" ],
      "like": [
        {
          "_index": "courses",
          "_id": docid
        }],
    "min_term_freq": 1,
    "max_query_terms": 12
    }
}
         

         hits = client.search(index='courses',query=qfile)
         i = 1
         outdoc = []
         scorelist = []
         

         for hit in hits['hits']['hits']:
             score = hit['_score']
             print(score)
             scorelist.append(score)
             print("doc"+str(i)+":\n")
             outfield = []
             for f in hit['_source']:
                 outfield.append(f +": "+ hit['_source'][f])
             i = i + 1
             outdoc.append(outfield)
         i=1     

         outdoc =zip(outdoc,scorelist)

         
         
            #  print("Title:", title)
            #  print("Objective:", objective)
            #  print("Framework:", framework)
         

         

         #for key, value in res.items():
         #  print(f'{key}: {value}')
       
         return render(request, 'engine.html', {'outdoc': outdoc})
      

         
   return render (request, 'engine.html')
