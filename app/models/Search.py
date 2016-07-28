from system.core.model import Model

class Search(Model):
    def __init__(self):
        super(Search, self).__init__()

    # Appended by_id due to method naming conflicts
    def get_favourites_by_user_id(self, session):
        print 'Session is - ', session,'\n'
        data_all_fav = {'id': session['id']}
        query_all_fav = 'SELECT * FROM search_favs WHERE users_user_id = :id'

        return self.db.query_db(query_all_fav, data_all_fav)

    def add_favourite(self, form):
        print "Search_add_favourite",'\n'
        query_new_fav = 'INSERT INTO search_favs (fav_name, fav_description, search_url, created_at, updated_at, users_user_id) VALUES (:fav_name, :fav_description, :current_url_search, NOW(), NOW(), 2);'
        print "Form data is ", form, '\n'
        new_fav_data = {
            'fav_name': form['fav_name'],
            'fav_description': form['fav_description'],
            'current_url_search': form['current_url_search']
        }

        return self.db.query_db(query_new_fav, new_fav_data)

    def get_fav_by_user(self, user_id, fav_id):
        print 'Search_get_fav_by_user'
        data_fav_by_user = {
                        'user_id': user_id,
                        'fav_id': fav_id
                        }
        query_fav_by_user = 'SELECT search_url FROM search_favs WHERE users_user_id=:user_id AND fav_id=:fav_id'
        search_url = self.db.query_db(query_fav_by_user, data_fav_by_user)
        print 'Search URL is ', search_url,'\n'
        return search_url[0]['search_url']


    #
    # # NOTE: Requests are already validated from Controller
    # def get_user(self, request):
    #     query = 'SELECT * FROM users WHERE email=:email'
    #     values = {
    #         'email': request.form['email']
    #     }
    #
    #     user = self.db.get_one(query, values)
    #
    #     # Result is empty, no user found.
    #     if not user:
    #         return False
    #
    #     if not self.bcrypt.check_password_hash(user['pw_hash'], request.form['pw']):
    #         return False
    #
    #     # Return id to store in session
    #     return user['id']
