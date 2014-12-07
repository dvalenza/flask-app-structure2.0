import os
from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask.ext.login import login_required, current_user
from werkzeug import secure_filename

from ..database import db_session
from ..models import Item

from forms import CreateNewItemForm

mod = Blueprint('items', __name__,
                template_folder='templates',
                static_folder='static')

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@mod.route('/newitem', methods=['GET','POST'])
def newItem():
    form = CreateNewItemForm()
    if request.method == 'POST':
      if form.validate_on_submit():
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
            newItem = Item(str(current_user()), form.name.data, form.description.data,form.quantity.data,filename)
    return render_template('items/newitem.html', form=form)
