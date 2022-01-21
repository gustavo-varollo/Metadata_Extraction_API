from flask import redirect, request, Blueprint
from werkzeug.utils import secure_filename
import pathlib
import os
from uuid import uuid4
from . metadata_handler import extract_metadata

uploader = Blueprint('uploader', __name__)


def make_unique(string):
    ident = uuid4().__str__()
    return f"{ident}-{string}"


def check_filetype_for_dir(file):
    """
    Check for file extension
    """
    return ''.join(pathlib.Path(file).suffixes)


def check_dir(uploads_dir, name):
    """
    Verify the directory for the possible existence of a sub-directory
    for the extension if none existente it makes a one
    """
    if not os.path.isdir(uploads_dir + name):
        os.makedirs(uploads_dir + name)


@uploader.route('/', methods=['GET', 'POST'])
def upload_file():
    """
    it Handles uploads o for the system
    """
    if request.method == 'POST' and request.files:
        file = request.files['file']
        if file.filename == '':
            return redirect('')
        elif file and file.filename:
            original_filename = secure_filename(file.filename)
            unique_filename = make_unique(original_filename)
            files_path = './Metadata_Extraction_API/static/uploads/'
            check_dir(files_path, check_filetype_for_dir(file.filename))
            if check_filetype_for_dir(file.filename) == '':
                file.save(files_path + 'None' + '/' + unique_filename)
                extract_metadata(unique_filename.replace('-' + file.filename, ''), file.filename,
                                 files_path + 'None')
            else:
                file.save(files_path + check_filetype_for_dir(file.filename) + '/' + unique_filename)
                extract_metadata(unique_filename.replace('-' + file.filename, ''), file.filename,
                                 files_path + check_filetype_for_dir(file.filename))
        return redirect(request.url)
    return redirect(request.url)
