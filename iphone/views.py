from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views import generic
from .models import Iphone
from .forms import IphoneForm






class Iphone_update_view(generic.UpdateView):
    template_name = 'iphone/update_phone.html'
    form_class = IphoneForm
    success_url = '/list_view/'

    def get_object(self, **kwargs):
        iphone_id = self.kwargs.get('id')
        return get_object_or_404(Iphone, id=iphone_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(Iphone_update_view, self).form_valid(form=form)


# def update_phone_view(request, id):
#     phone = get_object_or_404(Iphone, id=id)
#     if request.method == 'POST':
#         form = IphoneForm(request.POST, instance=phone)
#         if form.is_valid():
#             form.save()
#             return redirect('list_view')
#     else:
#         form = IphoneForm(instance=phone)
#     return render(request, 'iphone/update_phone.html', {'form':form})



class Iphone_delete_view(generic.DeleteView):
    template_name = 'iphone/delete_iphone.html'
    success_url = '/list_view/'

    def get_object(self, **kwargs):
        iphone_id = self.kwargs.get('id')
        return get_object_or_404(Iphone, id=iphone_id)


# def delete_phone_view(request, id):
#     phone = get_object_or_404(Iphone, id=id)
#     phone.delete()
#     return redirect('xc')



class Iphone_create_view(generic.CreateView):
    template_name = 'iphone/create_phone.html'
    form_class = IphoneForm
    success_url = '/list_view/'

    def form_valid(self, form):
        form.save()
        return super(Iphone_create_view, self).form_valid(form=form)

# def creare_phone_view(request):
#     if request.method == 'POST':
#         form = IphoneForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('list_view')
#     else:
#         form = IphoneForm()
#     return render(request, 'iphone/create_phone.html', {'form': form})


class Iphone_detail_view(generic.DetailView):
    template_name = 'iphone/iphone_details.html'
    context_object_name = 'iphone_id'

    def get_object(self, **kwargs):
        iphone_id = self.kwargs.get('id')
        return get_object_or_404(Iphone, id=iphone_id)


# def details_view(request, id):
#     if request.method == 'GET':
#         iphone_id = get_object_or_404(Iphone, id=id)
#         return render(request, 'iphone/iphone_details.html', {'iphone_id': iphone_id})


class Iphone_list_view(generic.ListView):
    template_name = 'iphone/iphone_list.html'
    context_object_name = 'iphones'
    model = Iphone

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')



# def list_view(request):
#     if request.method == 'GET':
#         iphones = Iphone.objects.filter().order_by('-id')
#         return render(request, 'iphone/iphone_list.html', {'iphones': iphones})

def index(request):
    if request.method == 'GET':
        return HttpResponse("Hello, World!")


