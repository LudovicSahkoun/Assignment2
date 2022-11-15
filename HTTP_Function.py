import logging
from math import *

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    
    lower=req.route_params.get("lower")
    upper=req.route_params.get("upper")

    
    lower_value=0
    upper_value=0

    try:
        lower_value=float(lower)
        upper_value=float(upper)
    except ValueError:
        return func.HttpResponse(
            "Incorrect parameters",
            status_code=400
        )

    

    def numerical_integration(lower : float, upper : float) -> list:
       
        result=[]
        
        N=[10, 100, 100, 1000, 10000, 100000, 1000000]
            
        for num in N:
            x=lower
            total=0
            dx = abs(upper-lower)/num
            
            while x <= upper:
                total+=abs(math.sin(x))*dx
                x=x+dx
            result.append(total)
        
        return result
           


    # Build HTML response
    body="<h1>%s</h1>"%str(numerical_integration(float(lower),float(upper)))

    return func.HttpResponse(
        body,
        status_code=200,
        mimetype="text/html"
    )
