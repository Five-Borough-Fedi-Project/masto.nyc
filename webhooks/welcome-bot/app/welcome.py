import os

from mastodon import Mastodon
from fastapi import FastAPI
from pydantic import BaseModel

# This was shamelessly stolen from from https://medium.com/@jaxzin/creating-a-mastodon-welcome-bot-9fe94a818506

class Account(BaseModel):
    # see AccountSerializer for the full list of properties: 
    #   https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/admin/account_serializer.rb
    username: str


class AccountCreatedEvent(BaseModel):
    event: str
    created_at: str
    object: Account


app = FastAPI()


@app.post("/")
def root(event: AccountCreatedEvent):
    #   Set up Mastodon
    mastodon = Mastodon(
        access_token=os.environ.get("WELCOMEACCESSTOKEN", ""),
        api_base_url='https://masto.nyc/'
    )

    account_id = f"@{event.object.username}"
    # For the love of god don't delete that first newline
    message = account_id + \
        " \n" \
        " Welcome to masto.nyc! \n" \
        "We hope you emjoy your stay here! \n" \
        "If you are new to Mastodon, we've put together a brief packet with some tips and pointers: \n" \
        "https://docs.google.com/document/d/1wSD4W_hcuChgiNjZLxRBafcSeOLFRFeBt0Q0e7hDk2U"

    mastodon.status_post(message, visibility='direct')

    return {"message": f"Sent welcome message to {account_id}."}