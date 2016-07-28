from system.core.model import Model

class Search(Model):
    def __init__(self):
        super(Search, self).__init__()

    # Appended by_id due to method naming conflicts
    def get_favourites_by_user_id(self, id):
        query_all_fav = 'SELECT * FROM searches'

        return self.db.query_db(query_all_fav)

    def add_favourite(self, form):
        query_new_fav = 'INSERT INTO searches (search_name, search_url, created_at, updated_at) VALUES (:faveourite_name, :current_url_search, NOW(), NOW() )'
        new_fav_data = {
            'faveourite_name': form['faveourite_name'],
            'current_url_search': form['current_url_search'],
        }
        return self.db.query_db(query_new_fav, new_fav_data)


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
