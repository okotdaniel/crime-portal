from admindashboard.models import crimes

class crimeManagement():
    def view_crimes(self, id, crime_name):
        pending_crimes = crimes.objects.exclude(status="pending")

        if( pending_crimes == False and start_date <  ):
            view_crimes = crimes.objects.all().order_by('name')
            