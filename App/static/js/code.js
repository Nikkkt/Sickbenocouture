// Scroll to top
function scrollToTop() {
  window.scrollTo(0, 0);
}
let url = window.location.href;

let langPars = document.querySelector('.langtitle_par');
langPars.textContent = langPars.textContent.toUpperCase();
const LANGTITLE = document.querySelector('.langtitle_par');
let langBtn = document.querySelector('.change_lang_button');
langBtn.addEventListener('click', (e) => {
  e.preventDefault();
  if (localStorage.getItem('LANG') == "EN") {
    localStorage.setItem('LANG', "UA");
    langBtn.value = localStorage.getItem('LANG');
    window.location.href = `/ua/` + url.split('/').slice(4).join('/');
  } else if(localStorage.getItem('LANG') != "EN") {
    localStorage.setItem('LANG', "EN");
    langBtn.value = localStorage.getItem('LANG');
    window.location.href = `/en/` + url.split('/').slice(4).join('/');
  }
})

// Nav Bar
let menuToggler = document.getElementById('menuToggler')
let menuTogglerLabel = document.getElementById('menuTogglerLabel');
let sidebar = document.getElementById('sidebar');
let menuItems = document.getElementsByClassName('menu__link');

menuToggler.addEventListener('change', function() {
if(menuToggler.checked) {
  menuTogglerLabel.setAttribute('aria-pressed', 'true');
  sidebar.setAttribute('aria-hidden', 'false');    
} else {
  menuTogglerLabel.setAttribute('aria-pressed', 'false');
  sidebar.setAttribute('aria-hidden', 'true');
}

for(let menuItem of menuItems) {
  if(menuToggler.checked) {
    menuItem.setAttribute('tabindex', '0');
  } else {
    menuItem.setAttribute('tabindex', '-1');
  }
}  
});

let numberOfCartItems = document.querySelector('.number_of__itemsincart'); 


// Cart Modal
let cartIcon = document.querySelector('.cart_click');
const modalTrigger = document.querySelectorAll('[data-modal]'),
     modal = document.querySelector('.modal'),
    modalCloseBtn = document.querySelector('[data-close]');

modalTrigger.forEach(btn => {
  btn.addEventListener('click', function() {
      modal.classList.add('show');
      modal.classList.remove('hide');
      document.body.style.overflow = 'hidden';
  });
});

function closeModal() {
  modal.classList.add('hide');
  modal.classList.remove('show');
  document.body.style.overflow = '';
}

modalCloseBtn.addEventListener('click', closeModal);

modal.addEventListener('click', (e) => {
  if (e.target === modal) {
      closeModal();
  }
});

document.addEventListener('keydown', (e) => {
  if (e.code === "Escape" && modal.classList.contains('show')) { 
      closeModal();
  }
});

// New Cart
var fadeTime = 300;
/* Assign actions */
$('.product-quantity input').change( function() {
  updateQuantity(this);
});

$('.product-removal button').click( function() {
  removeItem(this);
});



/* Recalculate cart */
function recalculateCart()
{
  var subtotal = 0;
  
  /* Sum up row totals */
  $('.product').each(function () {
    subtotal += parseFloat($(this).children('.product-line-price').text());
  });
  
  /* Calculate totals */

  var total = subtotal;
  
  /* Update totals display */
  $('.totals-value').fadeOut(fadeTime, function() {
    $('#cart-subtotal').html(subtotal.toFixed(2));
    $('#cart-total').html(total.toFixed(2));
    $('.totals-value').fadeIn(fadeTime);
  });
}


/* Update quantity */
function updateQuantity(quantityInput) {
  /* Calculate line price */
  var productRow = $(quantityInput).parent().parent();
  var price = parseFloat(productRow.children('.product-price').text());
  var quantity = $(quantityInput).val();
  var linePrice = price * quantity;

  console.log(quantity);

  /* Update line price display and recalc cart totals */
  productRow.children('.product-line-price').each(function () {
      $(this).fadeOut(fadeTime, function() {
      $(this).text(linePrice.toFixed(2));
      recalculateCart();
      $(this).fadeIn(fadeTime);
      });
  });  
}


/* Remove item from cart */
function removeItem(removeButton) {
/* Remove row from DOM and recalc cart total */
var productRow = $(removeButton).parent().parent();
productRow.slideUp(fadeTime, function() {
  productRow.remove();
  recalculateCart();
});
}

let btnUAHCheckOut = document.querySelector('#btn_checkout_uah');
let checkIfUAHHiddenInput = document.querySelector('.hidden_if_UAH');

btnUAHCheckOut.addEventListener('click', (e) => {
  checkIfUAHHiddenInput.value = 'UAH';
})