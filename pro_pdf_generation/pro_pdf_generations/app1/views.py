from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm
from django.views import View
from fpdf import FPDF
from django.http import FileResponse

# Create your views here.
def index(request):
    template_name = 'app1/index.html'
    context={}
    return render(request,template_name,context)

def report(request,id):
    obj = Employee.objects.get(id=id)
    sales = [
        {"Employee": "EMPLOYEE ID", "Details": obj.eid},
        {"Employee": "NAME", "Details": obj.name},
        {"Employee": "SALARY", "Details":  obj.salary},
        {"Employee": "E-MAIL", "Details":  obj.mail},
        {"Employee": "CITY", "Details":  obj.city}
      
    ]
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('courier', 'B', 16)
    pdf.cell(40, 10, f'THIS IS THE DETAILS OF EMPLOYEEE : {obj.name}',0,1)
    pdf.cell(40, 10, '',0,1)
    pdf.set_font('courier', '', 12)
    pdf.cell(200, 8, f"{'Employee'.ljust(30)} {'Details'.rjust(20)}", 0, 1)
    pdf.line(10, 30, 150, 30)
    pdf.line(10, 38, 150, 38)
    for line in sales:
        pdf.cell(200, 8, f"{line['Employee'].ljust(30)} {line['Details']}", 0, 1)
    pdf.output('report.pdf', 'F')
    return FileResponse(open('report.pdf', 'rb'), as_attachment=True, content_type='application/pdf')
 
class AddEmployee(View):
    template_name ='app1/addemp.html'
    form  =EmployeeForm
    def get(self,request):
        form = self.form()
        context = {'form':form}
        return render(request,self.template_name,context)
    def post(self,request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
        context={'form':'form'}
        return render(request,self.template_name,context)
    
class ShowEWmployee(View):
    template_name = 'app1/showemp.html'
    def get(self,request):
        obj = Employee.objects.all()
        context={'obj':obj}
        return render(request,self.template_name,context)
    
class UpdateEmployee(View):
    template_name ='app1/addemp.html'
    form  =EmployeeForm
    def get(self,request,id):
        obj = Employee.objects.get(id=id)
        form = self.form(instance=obj)
        context = {'form':form}
        return render(request,self.template_name,context)
    def post(self,request,id):
        obj = Employee.objects.get(id=id)
        form = self.form(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
        context={'form':'form'}
        return render(request,self.template_name,context)
    
class DeleteEmployee(View):
    template_name = 'app1/deleteemp.html'
    def get(self,request,id):
        obj = Employee.objects.get(id=id)
        context ={'obj':obj}
        return render(request,self.template_name,context)
    def post(self,request,id):
        obj = Employee.objects.get(id=id)
        obj.delete()
        return redirect("show_url")
        context ={'obj':obj}
        return render(request,self.template_name,context)
    

        
        
        
    
    
    
        
        