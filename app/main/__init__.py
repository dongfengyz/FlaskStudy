# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import Blueprint

main = Blueprint('main', __name__)

from . import errors, views
