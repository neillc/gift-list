# GiftList.py - a flask application to help organise buying gifts
#    Copyright (C) 2015  Neill Cox
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
import os

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, login_required
from flask.ext.social import Social
from flask.ext.social.datastore import SQLAlchemyConnectionDatastore
from flask_mail import Mail # TOBLOG - need to add this before register + confirmable will work
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
mail = Mail(app)    # TOBLOG

db = SQLAlchemy(app)
security = None
user_datastore = None
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@app.route('/')
@login_required
def hello_world():
    return render_template('index.html')


# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)


# Create a user to test with
def main():
    from app.models.users import User, Role, Connection

    global security, user_datastore, social

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)

    if app.config['CONFIG_SOCIAL']:
        social = Social(app, SQLAlchemyConnectionDatastore(db, Connection))

    admin = Admin(app, name='GiftList', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Role, db.session))
    admin.add_view(ModelView(Connection, db.session))

    manager.run()
