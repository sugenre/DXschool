from django.http import HttpResponse
from django.shortcuts import render
from web0726.models import Item


def index(request):
	#전체 데이터 가져오기
	data = Item.objects.all()
	print(data)
	return render(request, 'index.html', {'data':data})

#url 뒤에 붙은 파라미터는 2번째 매개변수를 이용해서 가져옴
def detail(request, itemid):
	item = Item.objects.get(itemid = itemid)
	print(item)
	return render(request, 'detail.html', {'item':item})












# Create your views here.

#def index(request):
#	print(dir(request))
#	return HttpResponse("<p>Hi Django</p>")

#def display(request):
#	return render(request, "display.html")

#def template(request):
#	msg = "Hello Template"
#	person = {"name":"adam", "age":53}
	#HTML에 데이터를 전송하고자 하면
	#세번째 매개변수에 디셔너리를만들어서
	#데이터 이름과 데이터를 기재
#	return render(request, "template.html", {"msg":msg, "person":person})


#def template(request):
#	age = 54

#	date = ["Stack", "queue"]
	#HTML에 데이터를 전송하고자 하면
	#세번째 매개변수에 디셔너리를만들어서
	#데이터 이름과 데이터를 기재
#	return render(request, "template.html",
#		{"age":age, "data": date})


