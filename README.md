<p align="center">
    <h1 align="center">Internet shop of brand custom clothes</h1>
</p>

<p align="center">
    <img src="App\static\images\mandems_logo_white.png" style="width: 30%">
</p>

<p align="center"><h2 align="center">Using <a href="https://github.com/Nikkkt/Sickbenocouture/blob/main/App/venv/main.py">Python</a> framework Flask and SQLAlchemy for Backend:</h2></p>

```python
from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="../templates", static_folder="../static")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///item.db'
app.config['SQLALCHEMY_BINDS'] = {'order': 'sqlite:///order.db'}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

...

if request.method == "POST":
        user_name = request.form['user_name']
        lastname = request.form['lastname']
        phone = request.form['phone']
        email = request.form['email']
        country = request.form['country']
        city = request.form['city']
        address = request.form['address']
        post_index = request.form['post_index']
        additional_comment = request.form['additional_comment']
        order_title = request.form['order_title']
        hidden_total__usd = request.form['hidden_total__usd']
        hidden_total__uah = request.form['hidden_total__uah']
        check_currency = request.form['check_currency']
        
        order = Order(user_name=user_name,
                    lastname=lastname,
                    phone=phone,
                    email=email,
                    country=country,
                    city=city,
                    address=address,
                    post_index=post_index,
                    additional_comment=additional_comment,
                    order_title=order_title,
                    hidden_total__usd=hidden_total__usd,
                    hidden_total__uah=hidden_total__uah,
                    check_currency=check_currency)
        
        try:
            db.session.add(order)
            db.session.commit()
            ...
        except Exception as e:
            return str(e)
            
...

if __name__ == "__main__":
    with app.app_context():         
        db.create_all()
    app.run(host='0.0.0.0', port=port, debug=False)
```

<p align="center"><h2 align="center">and <a href="https://github.com/Nikkkt/Sickbenocouture/tree/main/App/templates">HTML</a>, <a href="https://github.com/Nikkkt/Sickbenocouture/tree/main/App/static/css">CSS</a>, <a href="https://github.com/Nikkkt/Sickbenocouture/tree/main/App/static/js">JavaScript</a> for Frontend:</h2></p>

```javascript
const LANGTITLE = document.querySelector('.langtitle_par');
LANGTITLE.textContent = localStorage.getItem('LANG');
let langBtn = document.querySelector('.change_lang_button');
langBtn.addEventListener('click', (e) => {
  e.preventDefault();
  if (localStorage.getItem('LANG') == "EN") {
    localStorage.setItem('LANG', "UA");
    langBtn.value = localStorage.getItem('LANG');
    langBtn.querySelector('.langtitle_par').textContent = localStorage.getItem('LANG');
    window.location.href = `/ua/` + url.split('/').slice(4).join('/');
  } else if(localStorage.getItem('LANG') != "EN") {
    localStorage.setItem('LANG', "EN");
    langBtn.value = localStorage.getItem('LANG');
    langBtn.querySelector('.langtitle_par').textContent = localStorage.getItem('LANG');
    window.location.href = `/en/` + url.split('/').slice(4).join('/');
  }
})
```

```html
<main>
    <section class="shop_items__section">
      <div class="container">
        <div class="row shop_items__box" style="flex-wrap: wrap;">
          <script>
            const mainBox = document.querySelector('.shop_items__box');
            let arrayOfClothes = [];
            {% for item in data %}
            arrayOfClothes.push({
              "id": parseInt("{{ item.itemID }}"),
              "name": "{{ item.name }}",
              "image": "{{ item.image }}",
              "description": `{{ item.description }}`,
              "slug": "{{ item.slug }}",
            })
            {% endfor %}
            console.log(arrayOfClothes);
            arrayOfClothes.forEach((item) => {
              mainBox.innerHTML += `
                            <div class="col-lg-3 col-md-4 col-sm-6 col-10 offset-1 offset-sm-0  item_box">
                                <div class="item_logo__box">
                                    <a href="/{{ language }}/clothes/${item.slug}" class="nremgomf"><img style="object-fit: cover; aspect-ratio: 1 / 1; width: 100%;" src="data:image/jpeg;base64,${item.image.split(',')[0]}" alt="item_logo" class="item_logo" /></a>
                                </div>
                                <a href="/{{ language }}/clothes/${item.slug}" style="color: #000 !important"><h3 class="item_title limit-2-line-text">${item.name}</h3></a>
                            </div>
                            `;
            })
          </script>
        </div>
      </div>
    </section>
  </main>
```

```css
body {padding: 0;}
a {text-decoration: none !important; color: #fff !important}

.hidden_overflow {overflow-y: hidden;}
.shown_overflow {overflow-y: scroll;}
label {color: #000 !important}

.scroll-top-arrow { background: #fff; font-size: 17px; line-height: 34px; box-shadow: 0 0 25px rgba(23,23,23,.25); height: 34px; width: 34px; padding: 0; position: fixed; right: 45px; text-align: center; text-decoration: none; bottom: 45px; z-index: 1029; border-radius: 100%; }
.change_lang_button { background: #fff; font-size: 17px; line-height: 34px; box-shadow: 0 0 25px rgba(23,23,23,.25); height: 34px; width: 34px; padding: 0; position: fixed; right: 45px; text-align: center; text-decoration: none; top: 70px; z-index: 1029; border-radius: 100%; }
@media (max-width: 767.98px) {
	.change_lang_button {right: 25px;}
	.scroll-top-arrow {right: 25px;}
	.nav-container {max-width: 100% !important;}
}
@media (max-width: 575.98px) {
	.change_lang_button {right: 7px;}
	.scroll-top-arrow {right: 7px;}
}
```



<p align="center"><h2 align="center">For deploy was used Cloud Application Platform <a href="https://www.heroku.com"><i><b>Heroku</b></i></a>, and you can see result on this website:</p>
<p align="center"><a href="https://sickbenocouture.herokuapp.com"><b>sickbenocouture.herokuapp.com</b></a></p>
	
<br>
	
<p align="center"><h3 align="center"><i>Programmers</i></h3></p>

<p align="center"><a href="https://github.com/fow1078"><i>Kolisnyk Vladyslav</i></a>: Frontend<br><a href="https://github.com/Nikkkt"><i>Terpilovskyi Nikita</i></a>: Backend</p>
