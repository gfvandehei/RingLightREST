from flask import Blueprint, request, current_app, render_template
from RingLightAPI.services.light_store import LightStore
import logging
import json

log = logging.getLogger(__name__)

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=["GET"])
def get():
    return render_template('index.html')