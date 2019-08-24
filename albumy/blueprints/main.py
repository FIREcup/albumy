import os

from flask import render_template, current_app, request, Blueprint, send_from_directory
from flask_login import login_required, current_user

from ..decorators import permission_required, confirm_required
from ..extensions import db
from ..models import Photo
from ..utils import rename_image, resize_image
from flask_dropzone import random_filename


main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('main/index.html')

@main_bp.route('/upload', methods=['GET', 'POST'])
@login_required
@confirm_required
@permission_required('UPLOAD')
def upload():
    if request.method == 'POST' and 'file' in request.files:
        f = request.files.get('file')
        filename = random_filename(f.filename)
        f.save(os.path.join(current_app.config['ALBUMY_UPLOAD_PATH'], filename))
        filename_s = resize_image(f, filename, crrent_app.config['ALBUMY_PHOTO_SIZE']['small'])
        filename_m = resize_image(f, filename, crrent_app.config['ALBUMY_PHOTO_SIZE']['medium'])
        photo = Photo(
                filename = filename,
                filename_s = filename_s,
                filename_m = filename_m,
                author = current_user._get_current_object()
        )
        db.session.add(photo)
        db.session.commit()
    return render_template('main/upload.html')

@main_bp.route('/avatars/<path:filename>')
def get_avatar(filename):
    return send_from_directory(current_app.config['AVATARS_SAVE_PATH'], filename)
