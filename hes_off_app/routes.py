# Import packages
import os
import hes_off
import importlib_resources

from flask import render_template, request
from werkzeug.utils import secure_filename

from . import app
from .forms import *
from .forms import HesOffForm
from .utilities import *


# Create directory to store configuration files
UPLOAD_DIR = "hes_off_app/uploads/"
app.config["UPLOAD_FOLDER"] = UPLOAD_DIR
app.config["UPLOAD_EXTENSIONS"] = ["cfg"]

if not os.path.isdir(UPLOAD_DIR):
    os.mkdir(UPLOAD_DIR)


# Create app main page
@app.route("/", methods=["GET", "POST"])
@app.route("/gui", methods=["GET", "POST"])
def gui():

    # Instantiate WTForm object
    form = HesOffForm(request.form)

    # Initialize output dicts (to be updated after computations)
    data_dict = initialize_data_dict()
    plot_dict = initialize_plot_dict()

    # Load default configuration file and update fields
    if request.method == "POST" and form.DEFAULT.data:
        filename = importlib_resources.files("hes_off.data_files").joinpath("default.cfg")
        field_dict = hes_off.read_configuration_file(filename)
        form = update_form_from_dict(form, field_dict)

    # Load user-defined configuration file and update fields
    if request.method == "POST" and form.UPLOAD.data:
        file = request.files[form.INPUT_FILE.name]
        if file_allowed(file.filename, app.config["UPLOAD_EXTENSIONS"]):
            filename = os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(file.filename))
            file.save(filename)
            field_dict = hes_off.read_configuration_file(filename)
            form = update_form_from_dict(form, field_dict)

    # Get the data stored in the form and perform computations
    if request.method == "POST" and (form.COMPUTE.data or form.PLOTS.data) and form.validate():
        field_dict = create_dict_from_form(form)
        EnergySystem = hes_off.IntegratedModel(field_dict)
        EnergySystem.evaluate_process_model()
        data_dict = create_data_dict(EnergySystem)
        if form.PLOTS.data:
            plot_dict = create_plot_dict(EnergySystem)

    return render_template("gui.html", form=form, data_dict=data_dict, plot_dict=plot_dict)


# Create app docs page
@app.route("/docs", methods=["GET", "POST"])
def docs():
    return render_template("docs.html")


# Create app about page
@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html")
