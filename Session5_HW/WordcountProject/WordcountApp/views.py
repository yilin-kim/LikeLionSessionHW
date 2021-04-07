from django.shortcuts import render

# Create your views here.


def input(request):
    return render(request, 'input.html')


def result(request):
    text = request.POST['text']
    total_len = len(text)
    no_blank_len = len(text.replace(' ', ''))
    word_len = len(text.split(' '))

    return render(request, 'result.html',
                  {'text': text, 'total_len': total_len, 'no_blank_len': no_blank_len, 'word_len': word_len})
