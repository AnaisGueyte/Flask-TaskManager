from flask import Blueprint, render_template

profile = Blueprint('profile', __name__, template_folder='templates',
                    static_folder='static', url_prefix='/avc')

@profile.route('/profile')
def main():
    # Do some stuff
    return render_template('profile.html')
