from datetime import datetime , timedelta

class Currentdate:

    def currentdate(days):

        return(datetime.now() + timedelta(days=days)).strftime("%Y-%d-%m")
    
