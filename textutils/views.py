from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  return render(request, 'index.html')

def analyze(request):
  # Get Text
  data = request.POST.get('text', 'default')

  # Check Checkbox values
  removepunc = request.POST.get('removepunc', 'off')
  fullcaps = request.POST.get('fullcaps', 'off')
  newlineremover = request.POST.get('newlineremover', 'off')
  extraspaceremover = request.POST.get('extraspaceremover', 'off')
  numberremover = request.POST.get('numberremover', 'off')

  # Check which checkbox is on
  if removepunc == 'on':
    analyzed = ''
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' 
    for ele in data:
      if ele not in punc:
        analyzed = analyzed + ele

    params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
    data = analyzed
  
  if (fullcaps == 'on'):
    analyzed = '' 
    for ele in data:
      analyzed = analyzed + ele.upper()

    params = {'purpose': 'Change To Upper Case', 'analyzed_text': analyzed}
    data = analyzed
  
  if (newlineremover == 'on'):
    analyzed = ''
    for ele in data:
      if ele != '\n' and ele != '\r':
        analyzed= analyzed + ele
      
  
    params = {'purpose': 'Remove Newlines', 'analyzed_text': analyzed}

  if (extraspaceremover == 'on'):
    analyzed = ''
    for index, ele in enumerate(data):
      if ele == data[index-1]:
        if not (data[index] == ' '):
          analyzed = analyzed + ele
      
      elif not(data[index] == ' ' and data[index+1] == ' '):
        analyzed = analyzed + ele

    params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
    data = analyzed
  
  if (numberremover == 'on'):
    analyzed = ''
    numbers = '0123456789'
    for ele in data:
      if ele not in numbers:
        analyzed = analyzed + ele

    params = {'purpose': 'Remove Numbers', 'analyzed_text': analyzed}

  if (removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and numberremover != 'on'):
    return HttpResponse('Pleae select the option and try again.')
 
  return render(request, 'analyze.html', params)  

