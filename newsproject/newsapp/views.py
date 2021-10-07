from django.shortcuts import render
import requests

def index(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=c872e0c51dc9d031f3acd036392c22b1&countries=es')
    res = r.json()
    print("THIS IS MEEEE")
    print(res)

    data = res['data']
    title=[]
    description=[]
    image=[]
    url=[]
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])

    news = zip(title, description, image, url)
    return render(request, 'newsapp/index.html', {'news':news})
