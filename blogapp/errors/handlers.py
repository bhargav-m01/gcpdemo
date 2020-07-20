from flask import Blueprint, render_template

errors = Blueprint('errors',__name__)

# We also has another method called errorhandler instead of app_errorhandler but that is active for this blue print.
#  this app_errorhandler will work across  the application

@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404


@errors.app_errorhandler(403)
def error_404(error):
    return render_template('errors/403.html'), 403


@errors.app_errorhandler(500)
def error_404(error):
    return render_template('errors/500.html'), 500
