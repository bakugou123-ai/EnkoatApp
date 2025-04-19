from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Quote
from .serializers import QuoteSerializer
from django.template.loader import render_to_string
from django.http import HttpResponse


#Home view to render the home page
def home_view(request):
    return render(request,'quotes/home.html')

# Handle POST request to submit a new roofing quote
@api_view(['POST'])
def submit_quote(request):
    serializer = QuoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save() # Save the quote to the database
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Handle GET request to retrieve quotes by filters
@api_view(['GET'])
def get_quotes(request):
    state = request.GET.get('state')
    roof_type = request.GET.get('roof_type')

    quotes = Quote.objects.all() #Start with all records
    if state:
        quotes = quotes.filter(state=state) #filter by state
    if roof_type:
        quotes = quotes.filter(roof_type=roof_type) #filter by root type

    serializer = QuoteSerializer(quotes, many=True)
    return Response(serializer.data) #return the response 

def quote_form_view(request):
    return render(request, 'quotes/form.html')


from django.shortcuts import render
from bokeh.embed import server_document

#View for dashbord
def dashboard_view(request):
    script = server_document('http://localhost:5006/bokeh_dashboard') #Use the local server 
    return render(request, 'quotes/dashboard.html', {'bokeh_script': script}) #Render the dashboard page on local server



