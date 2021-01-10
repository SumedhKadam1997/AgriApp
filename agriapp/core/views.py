from flask import render_template,request,Blueprint,redirect,url_for
from flask_login import login_user, current_user, logout_user, login_required
from agriapp.models import Users, Crops, Fertilizers, WaterSolubleFertilizers, Contactmsg
from agriapp.core.forms import ContactForm, SearchForm
from agriapp import db

core = Blueprint('core',__name__)

@core.route('/')
def index():
    page = request.args.get('page',1,type=int)
    users = Users.query.all()
    crops = Crops.query.order_by(Crops.date_planted.desc()).paginate(page=page,per_page=5)
    return render_template('index.html',crops=crops, users = users)

@core.route('/about')
def about():
    return render_template('about.html')

@core.route('/contact',methods = ['GET','POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        contact = Contactmsg(user_id=current_user.id,
                            email=form.email.data,
                            subject = form.subject.data,
                            message = form.message.data)
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('core.index'))
    return render_template('contact.html',form = form)

@core.route('/search',methods = ['GET','POST'])
def search():
    form1 = SearchForm()

    if form1.validate_on_submit():
        pass
    return render_template('search.html',form1=form1)