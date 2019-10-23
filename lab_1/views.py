from django.shortcuts import render
from datetime import datetime, date
# Enter your name here
mhs_name = 'Mohammad Fatoni' # TODO Implement this
curr_year = int(datetime.now().strftime("%Y"))
curr_mont = int(datetime.now().strftime("%m"))
curr_day = int(datetime.now().strftime("%d"))
birth_date = date(1999,7,9) #TODO Implement this, format (Year, Month, Date)
birth_year=int(birth_date.strftime("%Y"))
birth_mont=int(birth_date.strftime("%m"))
birth_day=int(birth_date.strftime("%d"))
npm = 53417687 # TODO Implement this
# Create your views here.
def index(request):
    response = {'name': mhs_name, 'age': calculate_age(birth_date.year), 'npm': npm}
    return render(request, 'index_lab1.html', response)

def calculate_age(birth_year):
    age=curr_year - birth_year
    if birth_year >= curr_year :
        #masih bayi
        return 0
    else:
        if birth_mont > curr_mont:
            #belum ultah bos
            return age-1
        else:
            if birth_day> curr_day:
                #harinya belum sampai
                return age-1
            else :
                #happy birthday!!
                age=curr_year - birth_year
                return age
    # return curr_year - birth_year if birth_year <= curr_year else 0

def portofolio(request):
    return render(request, 'portofolio.html', {})
