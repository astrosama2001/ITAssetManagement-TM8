
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from .models import Asset
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return redirect(url_for('auth.login'))

@main.route('/dashboard')
@login_required
def dashboard():
    assets = Asset.query.all()
    return render_template('dashboard.html', assets=assets)

@main.route('/add_asset', methods=['POST'])
@login_required
def add_asset():
    new_asset = Asset(
        name=request.form.get('name'),
        category=request.form.get('category'),
        serial_number=request.form.get('serial_number'),
        assigned_to=request.form.get('assigned_to'),
        maintenance_date=request.form.get('maintenance_date')
    )
    db.session.add(new_asset)
    db.session.commit()
    return redirect(url_for('main.dashboard'))
