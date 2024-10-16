from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.models import Employee
from myapp.forms import Employeeform


class EmployeeListView(View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        return render(request,"employee.html",{"data":qs})
    
class EmployeeCreateView(View):
    def get(self,request,*args,**kwargs):
        form_instance=Employeeform()
        return render(request,"employee_add.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        form_instance=Employeeform(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            
            Employee.objects.create(**data)
            return redirect("employee-list")
        else:
            return render(request,"employee_add.html",{"form":form_instance})

class EmployeeDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employee.objects.get(id=id)
        return render(request,"employee_detail.html",{"data":qs})
    
class EmployeeDeleteView(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Employee.objects.get(id=id).delete()
        return redirect("employee-list")

class EmployeeUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        employee_object=Employee.objects.get(id=id)
        dist={
            "name":employee_object.name,
            "department":employee_object.department,
            "salary":employee_object.salary,
            "location":employee_object.location,
            "email":employee_object.email,
            "address":employee_object.address
    
        }
        form_instance=Employeeform(initial=dist)
        return render(request,"employee_edit.html",{"form":form_instance})
    

    def post(self,request,*args,**kwargs):
        form_instance=Employeeform(request.POST)
        id=kwargs.get("pk")
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            Employee.objects.filter(id=id).update(**data)
            return redirect("employee-list")
        else:
            return render(request,"employee_edit.html",{"form":form_instance})

 
 
    


    

        
    