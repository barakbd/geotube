from system.core.controller import *
import re
import json
import os

KEY = os.environ['ACCESS_SECRET']
TOKEN = os.environ['ACCESS_TOKEN']
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class Searches(Controller):
    def __init__(self, action):
        super(Searches, self).__init__(action)
        self.load_model('Search')

    def index(self):
        # if 'id' in session:
        #     return redirect('/')
        return self.load_view('search.html')

    def all_fav(self):
        all_fav=self.models['Search'].get_favourites_by_user_id()
        return

    def add_favourite(self):
        print 'Searches_add_favourite'
        print 'data received - ', request.form, '\n'
        new_fav_id=self.models['Search'].add_favourite(request.form)
        print 'New fav ID - ', new_fav_id
        return new_fav_id
