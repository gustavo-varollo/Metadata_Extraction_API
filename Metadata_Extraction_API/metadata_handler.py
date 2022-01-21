from flask import current_app as app
from .models import db, Metadata
from flask import send_file
import mimetypes
import time
import pathlib
import os


def extract_metadata(key: str, name: str, file: str) -> dict:
    """
    Meta data extraction function
    """
    return query_metadata_for_db({
        'key': key,
        'name': name,
        'path': file,
        'created': time.strftime('%d/%m/%Y', time.localtime(os.path.getctime(file))),
        'modified': time.strftime('%d/%m/%Y', time.localtime(os.path.getctime(file))),
        'mime_type': mimetypes.MimeTypes().guess_type(file)[0],
        'extension': ''.join(pathlib.Path(name).suffixes)
    })


@app.route('/', methods=['GET'])
def query_metadata_for_db(metadata_extracted: dict):
    """
    Query and save the metadata in to database
    """
    new_register = Metadata(
        key=metadata_extracted['key'],
        name=metadata_extracted['name'],
        path=metadata_extracted['path'],
        created=metadata_extracted['created'],
        modified=metadata_extracted['modified'],
        mime_type=metadata_extracted['mime_type'],
        extension=metadata_extracted['extension']
    )
    db.session.add(new_register)
    db.session.commit()


@app.route("/search<search_key>", methods=['GET'])
def get_metadata(search_key) -> str:
    """
    Return the metadata stored on the database
    """
    search = Metadata.query.filter_by(key=search_key).first()
    return str(search.__dict__)


@app.route("/retrieve<search_key>")
def query_metadata(search_key):
    """
    Return all the contents of a specific key
    """
    search = Metadata.query.filter_by(key=search_key).first()
    search_dir = 'static/uploads/' \
                 + str(search.extension) + '/' + str(search_key) + '-' + str(search.name)
    return send_file(search_dir)
