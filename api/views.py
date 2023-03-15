from django.http import HttpRequest, JsonResponse
import json

# import models
from .models import Contact, Address, Student


def add_contact(request: HttpRequest) -> JsonResponse:
    """add contact view"""
    if request.method == "POST":
        # get data from request
        decoded_data = request.body.decode()
        data = json.loads(decoded_data)

        # insert data
        contact = Contact.objects.create(
            phone=data.get('phone', 0),
            email=data.get('email', 0),
        )

        return JsonResponse({
            'id': contact.id,
            'phone': contact.phone,
            'email': contact.email,
        })
    return JsonResponse({'status': 'method not allawed'})