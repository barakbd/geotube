from system.core.model import Model

class Search(Model):
    def __init__(self):
        super(Search, self).__init__()

    def add_favourite(self, request):
        query = 'INSERT INTO users (name, alias, email, pw_hash, created_at) VALUES (:name, :alias, :email, :pw_hash, NOW())'
        values = {
            'name': request.form['name'],
            'alias': request.form['alias'],
            'email': request.form['email'],
            'pw_hash': self.bcrypt.generate_password_hash(request.form['pw'])
        }

        return self.db.query_db(query, values)

    # Appended by_id due to method naming conflicts
    def get_favourites_by_user_id(self, id):
        query = 'SELECT * FROM users WHERE id=:id'
        values = {
            'id': id
        }

        return self.db.get_one(query, values)

    # NOTE: Requests are already validated from Controller
    def get_user(self, request):
        query = 'SELECT * FROM users WHERE email=:email'
        values = {
            'email': request.form['email']
        }

        user = self.db.get_one(query, values)

        # Result is empty, no user found.
        if not user:
            return False

        if not self.bcrypt.check_password_hash(user['pw_hash'], request.form['pw']):
            return False

        # Return id to store in session
        return user['id']
