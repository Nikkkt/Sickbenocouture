import base64
import random

from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from io import BytesIO
from PIL import Image 

app = Flask(__name__, template_folder="../templates", static_folder="../static")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///item.db'
app.config['SQLALCHEMY_BINDS'] = {'order': 'sqlite:///order.db'}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Item(db.Model):
    __tablename__ = 'clothes'
    
    id = db.Column(db.Integer, primary_key=True)
    itemID = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    price_USD = db.Column(db.Integer, nullable=False)
    price_UAH = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    description_en = db.Column(db.String(1000), nullable=False)
    additional_info = db.Column(db.String(1000))
    additional_info_en = db.Column(db.String(1000))
    amountNumber = db.Column(db.Integer, nullable=False)
    slug = db.Column(db.String(100), index=True)
    size_S = db.Column(db.String(10))
    size_M = db.Column(db.String(10))
    size_L = db.Column(db.String(10))
    size_XL = db.Column(db.String(10))
    size_XXL = db.Column(db.String(10))
    image = db.Column(db.String(100000))
    image_original = db.Column(db.String(100000))
    
class Order(db.Model):
    __bind_key__ = 'order'
    __tablename__ = 'order'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String(15), nullable=False)
    user_name = db.Column(db.String(110), nullable=False)
    lastname = db.Column(db.String(70), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    messenger = db.Column(db.String(15), nullable=False)
    phone_or_nickname = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(75), nullable=False)
    post_office_details = db.Column(db.String(200), nullable=False)
    post_index = db.Column(db.Integer, nullable=False)
    additional_comment = db.Column(db.String(1000))
    order_title = db.Column(db.String(10000), nullable=False)
    hidden_total__usd = db.Column(db.String(7), nullable=False)
    hidden_total__uah = db.Column(db.String(7), nullable=False)


@app.route('/')
def default():
    return redirect('/en')


@app.route('/<lang>/', methods=['POST', 'GET'])
def index(lang):
    if lang != 'en' and lang != 'ua': 
        return redirect('/en')
    
    items = Item.query.order_by(Item.id).all()
    activeLang=lang

    if request.method == "POST":
        order_id = "SB" + str(random.randint(1000000, 10000000))
        user_name = request.form['user_name']
        lastname = request.form['lastname']
        email = request.form['email']
        messenger = request.form['messenger']
        phone_or_nickname = request.form['telegram_nickname']
        country = request.form['country']
        city = request.form['city']
        address = request.form['address']
        post_index = request.form['post_index']
        post_office_details = request.form['post_office__details']
        additional_comment = request.form['additional_comment']
        order_title = request.form['order_title']
        hidden_total__usd = request.form['hidden_total__usd']
        hidden_total__uah = request.form['hidden_total__uah']
        
        order = Order(
                    order_id=order_id,
                    user_name=user_name,
                    lastname=lastname,
                    email=email,
                    messenger=messenger,
                    phone_or_nickname=phone_or_nickname,
                    country=country,
                    city=city,
                    address=address,
                    post_index=post_index,
                    post_office_details=post_office_details,
                    additional_comment=additional_comment,
                    order_title=order_title,
                    hidden_total__usd=hidden_total__usd,
                    hidden_total__uah=hidden_total__uah,
                    )
        
        try:
            db.session.add(order)
            db.session.commit()

            return redirect(f'/thank_you/{order_id}')
            
        except Exception as e:
            return str(e)

    else:
        return render_template('index.html', data=items, language=activeLang)


@app.route('/<lang>/about', methods=['POST', 'GET'])
def about(lang):
    if lang != 'en' and lang != 'ua': 
        return redirect('/en')

    activeLang=lang

    if request.method == "POST":
        order_id = "SB" + str(random.randint(1000000, 10000000))
        user_name = request.form['user_name']
        lastname = request.form['lastname']
        email = request.form['email']
        messenger = request.form['messenger']
        phone_or_nickname = request.form['telegram_nickname']
        country = request.form['country']
        city = request.form['city']
        address = request.form['address']
        post_index = request.form['post_index']
        post_office_details = request.form['post_office__details']
        additional_comment = request.form['additional_comment']
        order_title = request.form['order_title']
        hidden_total__usd = request.form['hidden_total__usd']
        hidden_total__uah = request.form['hidden_total__uah']
        
        order = Order(
                    order_id=order_id,
                    user_name=user_name,
                    lastname=lastname,
                    email=email,
                    messenger=messenger,
                    phone_or_nickname=phone_or_nickname,
                    country=country,
                    city=city,
                    address=address,
                    post_index=post_index,
                    post_office_details=post_office_details,
                    additional_comment=additional_comment,
                    order_title=order_title,
                    hidden_total__usd=hidden_total__usd,
                    hidden_total__uah=hidden_total__uah,
                    )
        
        try:
            db.session.add(order)
            db.session.commit()

            return redirect(f'/thank_you/{order_id}')
        
        except Exception as e:
            return str(e)

    else:
        return render_template('about.html', language=activeLang)


@app.route('/<lang>/contact', methods=['POST', 'GET'])
def contact(lang):
    if lang != 'en' and lang != 'ua': 
        return redirect('/en')
    
    activeLang=lang
    
    if request.method == "POST":
        order_id = "SB" + str(random.randint(1000000, 10000000))
        user_name = request.form['user_name']
        lastname = request.form['lastname']
        email = request.form['email']
        messenger = request.form['messenger']
        phone_or_nickname = request.form['telegram_nickname']
        country = request.form['country']
        city = request.form['city']
        address = request.form['address']
        post_index = request.form['post_index']
        post_office_details = request.form['post_office__details']
        additional_comment = request.form['additional_comment']
        order_title = request.form['order_title']
        hidden_total__usd = request.form['hidden_total__usd']
        hidden_total__uah = request.form['hidden_total__uah']
        
        order = Order(
                    order_id=order_id,
                    user_name=user_name,
                    lastname=lastname,
                    email=email,
                    messenger=messenger,
                    phone_or_nickname=phone_or_nickname,
                    country=country,
                    city=city,
                    address=address,
                    post_index=post_index,
                    post_office_details=post_office_details,
                    additional_comment=additional_comment,
                    order_title=order_title,
                    hidden_total__usd=hidden_total__usd,
                    hidden_total__uah=hidden_total__uah,
                    )
        
        try:
            db.session.add(order)
            db.session.commit()

            return redirect(f'/thank_you/{order_id}')
        
        except Exception as e:
            return str(e)

    else:
        return render_template('contact.html', language=activeLang) 


@app.route('/z8d6Ta3H49iJb3S9AR6XtTpb', methods=['POST', 'GET'])
def adminpage():
    if request.method == "POST":
        name = request.form['name']
        itemID = str(random.randint(1000000, 10000000))
        price_USD = request.form['price_USD']
        price_UAH = request.form['price_UAH']
        description = request.form['description']
        description_en = request.form['description_en']
        amountNumber = request.form['amountNumber']
        slug = request.form['slug']
        size_S = request.form['size_S']
        size_M = request.form['size_M']
        size_L = request.form['size_L']
        size_XL = request.form['size_XL']
        size_XXL = request.form['size_XXL']
        additional_info = request.form['additional_info']
        additional_info_en = request.form['additional_info_en']
        image = request.files.getlist('image')
        
        imageArr_original = []
        imageArr = []
        for item in image: 
            imageArr_original.append(base64.b64encode(item.read()).decode('ascii'))
            im = Image.open(item)
            width, height = im.size
            tmp1 = 400 - width / 10
            tmp2 = 400 - height / 10
            if tmp1 < 0 and tmp2 < 0: 
                im = im.convert("RGB")
                im.thumbnail([int(width / 10), int(height / 10)])
                buffered = BytesIO()
                im.save(buffered, format="JPEG", quality=100)
                imageArr.append(base64.b64encode(buffered.getvalue()).decode('ascii'))
            else: 
                im = im.convert("RGB")
                im.thumbnail([int((width / 10) + tmp1), int((height / 10)) + tmp2])
                buffered = BytesIO()
                im.save(buffered, format="JPEG", quality=100)
                imageArr.append(base64.b64encode(buffered.getvalue()).decode('ascii'))
            
        item = Item(
                    name=name, 
                    itemID=itemID,
                    price_USD=price_USD, 
                    price_UAH=price_UAH, 
                    description=description, 
                    description_en=description_en, 
                    amountNumber=amountNumber, 
                    slug=slug,
                    size_S=size_S,
                    size_M=size_M,
                    size_L=size_L,
                    size_XL=size_XL,
                    size_XXL=size_XXL,
                    additional_info=additional_info,
                    additional_info_en=additional_info_en,
                    image=",".join(imageArr),
                    image_original=",".join(imageArr_original)
                    )
        
        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/z8d6Ta3H49iJb3S9AR6XtTpb')
        except Exception as e:
            return str(e)

    else:
        return render_template('admin.html')


@app.route('/z8d6Ta3H49iJb3S9AR6XtTpb/statistics')
def adminpagestatistics():
    order = Order.query.order_by(Order.id).all()
    return render_template('adminstatistic.html', order=order)


@app.route("/z8d6Ta3H49iJb3S9AR6XtTpb/statistics/delete/<id>")
def delete(id):
    order = Order.query.filter_by(id=id).first()
    db.session.delete(order)
    i = 0
    order_edit = Order.query.all()
    for el in order_edit:
        i += 1
        el.id = i
    db.session.commit()
    return redirect('/z8d6Ta3H49iJb3S9AR6XtTpb/statistics')


@app.route("/z8d6Ta3H49iJb3S9AR6XtTpb/statistics/reset")
def reset():
    order = Order.query.all()
    for el in order:
        db.session.delete(el)
    db.session.commit()
    return redirect('/z8d6Ta3H49iJb3S9AR6XtTpb/statistics')


@app.route('/z8d6Ta3H49iJb3S9AR6XtTpb/edit')
def adminpageedit():
    item = Item.query.order_by(Item.id).all()
    return render_template('adminedit.html', item=item)


@app.route('/z8d6Ta3H49iJb3S9AR6XtTpb/edit/<id>', methods=['POST', 'GET'])
def editItem(id):
    item = db.session.query(Item).filter_by(id=id).first()
    
    if request.method == "POST":
        check = request.form['check_action']
        
        if check == 'Update':
            item.name = request.form['name']
            item.price_USD = request.form['price_USD']
            item.price_UAH = request.form['price_UAH']
            item.description = request.form['description']
            item.description_en = request.form['description_en']
            item.amountNumber = request.form['amountNumber']
            item.slug = request.form['slug']
            item.size_S = request.form['size_S']
            item.size_M = request.form['size_M']
            item.size_L = request.form['size_L']
            item.size_XL = request.form['size_XL']
            item.size_XXL = request.form['size_XXL']
            item.additional_info = request.form['additional_info']
            item.additional_info_en = request.form['additional_info_en']
            image = request.files.getlist('image')
            
            if request.form['check_delete_all_images'] == 'Clear':
                item.image = ""
                item.image_original = ""
                
                imageArr = []
                imageArr_original = []
                
                for el in image:
                    imageArr_original.append(base64.b64encode(el.read()).decode('ascii'))
                    
                    im = Image.open(el)
                    width, height = im.size
                    tmp1 = 400 - width / 10
                    tmp2 = 400 - height / 10
                    
                    if tmp1 < 0 and tmp2 < 0: 
                        im = im.convert("RGB")
                        im.thumbnail([int(width / 10), int(height / 10)])
                        buffered = BytesIO()
                        im.save(buffered, format="JPEG", quality=100)
                        imageArr.append(base64.b64encode(buffered.getvalue()).decode('ascii'))
                        
                    else: 
                        im = im.convert("RGB")
                        im.thumbnail([int((width / 10) + tmp1), int((height / 10)) + tmp2])
                        buffered = BytesIO()
                        im.save(buffered, format="JPEG", quality=100)
                        imageArr.append(base64.b64encode(buffered.getvalue()).decode('ascii'))
                        
                arr = item.image.split(",") + imageArr
                arr2 = item.image_original.split(",") + imageArr_original
                
                for el in arr:
                    if el == '':
                        arr.remove(el)
                        
                for el in arr2:
                    if el == '':
                        arr.remove(el)

                item.image = ",".join(arr)
                item.image_original = ",".join(arr2)

            else:
                imageArr = []
                imageArr_original = []
                
                for el in image:
                    imageArr_original.append(base64.b64encode(el.read()).decode('ascii'))
                    
                    im = Image.open(el)
                    width, height = im.size
                    tmp1 = 400 - width / 10
                    tmp2 = 400 - height / 10
                    
                    if tmp1 < 0 and tmp2 < 0: 
                        im = im.convert("RGB")
                        im.thumbnail([int(width / 10), int(height / 10)])
                        buffered = BytesIO()
                        im.save(buffered, format="JPEG", quality=100)
                        imageArr.append(base64.b64encode(buffered.getvalue()).decode('ascii'))
                        
                    else: 
                        im = im.convert("RGB")
                        im.thumbnail([int((width / 10) + tmp1), int((height / 10)) + tmp2])
                        buffered = BytesIO()
                        im.save(buffered, format="JPEG", quality=100)
                        imageArr.append(base64.b64encode(buffered.getvalue()).decode('ascii'))
                        
                arr = item.image.split(",") + imageArr
                arr2 = item.image_original.split(",") + imageArr_original
                
                for el in arr:
                    if el == '':
                        arr.remove(el)
                        
                for el in arr2:
                    if el == '':
                        arr.remove(el)

                item.image = ",".join(arr)
                item.image_original = ",".join(arr2)

            db.session.commit()
            return redirect("/z8d6Ta3H49iJb3S9AR6XtTpb/edit")

        else:
            item = Item.query.filter_by(id=id).first()
            db.session.delete(item)
            i = 0
            item_id_update = item.query.all()
            for el in item_id_update:
                i += 1
                el.id = i
            db.session.commit()
            return redirect("/z8d6Ta3H49iJb3S9AR6XtTpb/edit")

    return render_template('edititem.html', item=item) 


@app.route('/<lang>/clothes/<slug>', methods=['POST', 'GET'])
def itempage(lang, slug):
    if lang != 'en' and lang != 'ua': 
        return redirect('/en')

    activeLang=lang
    item = db.session.query(Item).filter_by(slug = slug).first()

    if request.method == "POST":
        order_id = "SB" + str(random.randint(1000000, 10000000))
        user_name = request.form['user_name']
        lastname = request.form['lastname']
        email = request.form['email']
        messenger = request.form['messenger']
        phone_or_nickname = request.form['telegram_nickname']
        country = request.form['country']
        city = request.form['city']
        address = request.form['address']
        post_index = request.form['post_index']
        post_office_details = request.form['post_office__details']
        additional_comment = request.form['additional_comment']
        order_title = request.form['order_title']
        hidden_total__usd = request.form['hidden_total__usd']
        hidden_total__uah = request.form['hidden_total__uah']
        
        order = Order(
                    order_id=order_id,
                    user_name=user_name,
                    lastname=lastname,
                    email=email,
                    messenger=messenger,
                    phone_or_nickname=phone_or_nickname,
                    country=country,
                    city=city,
                    address=address,
                    post_index=post_index,
                    post_office_details=post_office_details,
                    additional_comment=additional_comment,
                    order_title=order_title,
                    hidden_total__usd=hidden_total__usd,
                    hidden_total__uah=hidden_total__uah,
                    )
        
        try:
            db.session.add(order)
            db.session.commit()

            return redirect(f'/thank_you/{order_id}')
        
        except Exception as e:
            return str(e)

    else:
        return render_template("item.html", item=item, language=activeLang)
    
    
@app.route('/<lang>/oferta', methods=['POST', 'GET'])
def oferta(lang):
    if lang != 'en' and lang != 'ua': 
        return redirect('/en')

    activeLang=lang

    if request.method == "POST":
        order_id = "SB" + str(random.randint(1000000, 10000000))
        user_name = request.form['user_name']
        lastname = request.form['lastname']
        email = request.form['email']
        messenger = request.form['messenger']
        phone_or_nickname = request.form['telegram_nickname']
        country = request.form['country']
        city = request.form['city']
        address = request.form['address']
        post_index = request.form['post_index']
        post_office_details = request.form['post_office__details']
        additional_comment = request.form['additional_comment']
        order_title = request.form['order_title']
        hidden_total__usd = request.form['hidden_total__usd']
        hidden_total__uah = request.form['hidden_total__uah']
        
        order = Order(
                    order_id=order_id,
                    user_name=user_name,
                    lastname=lastname,
                    email=email,
                    messenger=messenger,
                    phone_or_nickname=phone_or_nickname,
                    country=country,
                    city=city,
                    address=address,
                    post_index=post_index,
                    post_office_details=post_office_details,
                    additional_comment=additional_comment,
                    order_title=order_title,
                    hidden_total__usd=hidden_total__usd,
                    hidden_total__uah=hidden_total__uah,
                    )
        
        try:
            db.session.add(order)
            db.session.commit()

            return redirect(f'/thank_you/{order_id}')
        
        except Exception as e:
            return str(e)

    else:
        return render_template('oferta.html', language=activeLang) 


@app.route('/<lang>/exchange', methods=['POST', 'GET'])
def exchange(lang):
    if lang != 'en' and lang != 'ua': 
        return redirect('/en')

    activeLang=lang

    if request.method == "POST":
        order_id = "SB" + str(random.randint(1000000, 10000000))
        user_name = request.form['user_name']
        lastname = request.form['lastname']
        email = request.form['email']
        messenger = request.form['messenger']
        phone_or_nickname = request.form['telegram_nickname']
        country = request.form['country']
        city = request.form['city']
        address = request.form['address']
        post_index = request.form['post_index']
        post_office_details = request.form['post_office__details']
        additional_comment = request.form['additional_comment']
        order_title = request.form['order_title']
        hidden_total__usd = request.form['hidden_total__usd']
        hidden_total__uah = request.form['hidden_total__uah']
        
        order = Order(
                    order_id=order_id,
                    user_name=user_name,
                    lastname=lastname,
                    email=email,
                    messenger=messenger,
                    phone_or_nickname=phone_or_nickname,
                    country=country,
                    city=city,
                    address=address,
                    post_index=post_index,
                    post_office_details=post_office_details,
                    additional_comment=additional_comment,
                    order_title=order_title,
                    hidden_total__usd=hidden_total__usd,
                    hidden_total__uah=hidden_total__uah,
                    )
        
        try:
            db.session.add(order)
            db.session.commit()

            return redirect(f'/thank_you/{order_id}')

        except Exception as e:
            return str(e)

    else:
        return render_template('exchange.html', language=activeLang) 


@app.route('/<lang>/payment', methods=['POST', 'GET'])
def payment(lang):
    if lang != 'en' and lang != 'ua': 
        return redirect('/en')
    
    activeLang=lang
    
    if request.method == "POST":
        order_id = "SB" + str(random.randint(1000000, 10000000))
        user_name = request.form['user_name']
        lastname = request.form['lastname']
        email = request.form['email']
        messenger = request.form['messenger']
        phone_or_nickname = request.form['telegram_nickname']
        country = request.form['country']
        city = request.form['city']
        address = request.form['address']
        post_index = request.form['post_index']
        post_office_details = request.form['post_office__details']
        additional_comment = request.form['additional_comment']
        order_title = request.form['order_title']
        hidden_total__usd = request.form['hidden_total__usd']
        hidden_total__uah = request.form['hidden_total__uah']
        
        order = Order(
                    order_id=order_id,
                    user_name=user_name,
                    lastname=lastname,
                    email=email,
                    messenger=messenger,
                    phone_or_nickname=phone_or_nickname,
                    country=country,
                    city=city,
                    address=address,
                    post_index=post_index,
                    post_office_details=post_office_details,
                    additional_comment=additional_comment,
                    order_title=order_title,
                    hidden_total__usd=hidden_total__usd,
                    hidden_total__uah=hidden_total__uah,
                    )
        
        try:
            db.session.add(order)
            db.session.commit()

            return redirect(f'/thank_you/{order_id}')
        
        except Exception as e:
            return str(e)

    else:
        return render_template('payment.html', language=activeLang)


@app.route('/<lang>/privacy-policy', methods=['POST', 'GET'])
def policy(lang):
    if lang != 'en' and lang != 'ua': 
        return redirect('/en')
    
    activeLang=lang
    
    if request.method == "POST":
        order_id = "SB" + str(random.randint(1000000, 10000000))
        user_name = request.form['user_name']
        lastname = request.form['lastname']
        email = request.form['email']
        messenger = request.form['messenger']
        phone_or_nickname = request.form['telegram_nickname']
        country = request.form['country']
        city = request.form['city']
        address = request.form['address']
        post_index = request.form['post_index']
        post_office_details = request.form['post_office__details']
        additional_comment = request.form['additional_comment']
        order_title = request.form['order_title']
        hidden_total__usd = request.form['hidden_total__usd']
        hidden_total__uah = request.form['hidden_total__uah']
        
        order = Order(
                    order_id=order_id,
                    user_name=user_name,
                    lastname=lastname,
                    email=email,
                    messenger=messenger,
                    phone_or_nickname=phone_or_nickname,
                    country=country,
                    city=city,
                    address=address,
                    post_index=post_index,
                    post_office_details=post_office_details,
                    additional_comment=additional_comment,
                    order_title=order_title,
                    hidden_total__usd=hidden_total__usd,
                    hidden_total__uah=hidden_total__uah,
                    )
        
        try:
            db.session.add(order)
            db.session.commit()

            return redirect(f'/thank_you/{order_id}')
        
        except Exception as e:
            return str(e)

    else:
        return render_template('privacypolicy.html', language=activeLang)


@app.route('/thank_you/<order_id>',  methods=['POST', 'GET'])
def thank_you(order_id):
    return render_template('finishpaymentpage.html', order_id=order_id)
