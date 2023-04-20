function addProduct(id, name, size, priceUAH, priceUSD) {
    if (size === 'S') {
        cartLS.add({id: id, name: `${name}`, size: `${size}`, price: priceUAH, priceTwo: priceUSD })
    } else if (size === 'M') {
        cartLS.add({id: parseInt(id) + 1, name: `${name}`, size: `${size}`, price: priceUAH, priceTwo: priceUSD })
    } else if (size === 'L') {
        cartLS.add({id: parseInt(id) + 2, name: `${name}`, size: `${size}`, price: priceUAH, priceTwo: priceUSD })
    } else if (size === 'XL') {
        cartLS.add({id: parseInt(id) + 3, name: `${name}`, size: `${size}`, price: priceUAH, priceTwo: priceUSD })
    } else if (size === 'XXL') {
        cartLS.add({id: parseInt(id) + 4, name: `${name}`, size: `${size}`, price: priceUAH, priceTwo: priceUSD })
    } else if (size === 'One Size') {
        cartLS.add({id: parseInt(id) + 4, name: `${name}`, size: `${size}`, price: priceUAH, priceTwo: priceUSD });
    }
}

function showNotification(name, selector, size) {
    let placeToShow = document.querySelector(selector);
    if  (size !== 'Select' && size !== '') {
        placeToShow.innerHTML += `
        <div class="cart_message__single_box">
            <p class="text-white" style="margin-bottom: 0 !important">${localStorage.getItem("LANG") == "EN" ? `Product ${name} added to cart` : `Продукт ${name} додано до кошику`} </p><i class="fa-solid fa-xmark notification_cross"></i>
        </div>
        `;
        let notificationCross = document.querySelectorAll('.notification_cross');
        notificationCross.forEach(item => {
            item.addEventListener('click', (e) => {
                e.preventDefault();
                let crossParent = item.closest('.cart_message__single_box');
                crossParent.style.opacity = '0';
                setTimeout(() => {
                    crossParent.style.display = 'none';
                    crossParent.remove()
                }, 450)
            })
        })
        setTimeout(() => {
            let crossParent = document.querySelectorAll('.cart_message__single_box');
            crossParent.forEach(el => {
                el.style.opacity = '0'
                setTimeout(() => {
                    el.style.display = 'none';
                    el.remove();
                }, 450)
            })
        }, 2200)
    }
}

let boxToAdd = document.querySelector('.item_to_buy');
let script = document.createElement('script');
script.setAttribute('async', '');
script.text = `let currSize = ''; 
              document.querySelector('.input_select__size').addEventListener('change', (e) => {
                e.preventDefault(); 
                currSize = e.target.value;
              })`
window.onload = () => {
  document.querySelector('.sizeScript').appendChild(script);
}

let arrOfImgs = [];
function getArrOfImages(tempArrOfImgs) {
    arrOfImgs = tempArrOfImgs.split(',');
}
getArrOfImages(image_original);
function ifGenerateGalleryCol(array) {
    if (array.length > 1) {
        function imagesLoop() {
            let htmlArch = ``;
            array.forEach(img => {
                let imgArch = `
                <a class="item_side__imgs_url" data-fancybox="gallery" data-src="data:image/jpeg;base64,${img}"  style="margin-bottom: 15px; height: fit-content;">
                    <img class="item_side__imgs" src="data:image/jpeg;base64,${img}" style="max-width: 100%" />
                </a>
                `;
                htmlArch += imgArch;
            });
            return htmlArch;
        }
        return `
        <div class="row item_all__images_row"">
          <div class="img_box col-12 col-md-10 col-lg-12" id="main_image_container">
            <img src="data:image/jpg;base64,${image.split(',')[0]}" class="item_toBuy_img item_main__img" style="max-width: 100%"; />
          </div>

          <div class="col-12 col-md-3 d-flex item_media_div">
            ${imagesLoop()}
          </div>
        </div>
        `
    } else {
        return `
        <div class="w-100 img_box" style="margin-bottom: 15px" id="main_single_image_container">
            <img src="data:image/jpg;base64,${image.split(',')[0]}" class="item_toBuy_img item_main__img" style="max-width: 100%"; />
        </div>
        `;
    }
}

function checkSizeAmount(ifsize, size) { 
    if (ifsize == 'true') {
        return `<option value="${size}">${size}</option>`;
    } else if (ifsize == 'false') {
        return '';
    }
}

function checkIfAnySizeChosen(arr) {
    let res = 0;
    for (let val of arr) {
        if (val == 'false') {
            continue;
        } else {
            res += 1;
        }
    }
    if (res == 0 && amountNumber != 0) {
        return `<option value="One Size">One Size</option>`;
    } else if (res == 0 && amountNumber == 0) {
        console.log('meow2')
        return `<option value="One Size" disabled>One Size</option>`;
    } else if (res >= 1) {
        return '';
    }
}

let innerClothes = `
  <div class="row justify-content-between item_to_buy" style="margin-bottom: 40px">
      <div class="col-lg-5 col-12 item_img__box">
          ${ifGenerateGalleryCol(arrOfImgs)}
          <p class="amount__stock ${ amountNumber <= 0 ? 'amount_out__of_stack' : ''}" style="margin-bottom: 0">${ amountNumber > 0 ? `${localStorage.getItem("LANG") == "EN" ? 'In Stock' : 'В наявності'}` : `${localStorage.getItem("LANG") == "EN" ? 'Soldout' : 'Soldout'}`}</p>
      </div>

      <div class="col-lg-5 col-12 d-flex flex-column justify-content-center">
          <div class="d-flex flex-column align-items-start">
              <h3 class="item_title_on_item_page">${name}</h3>
              <div class="prizes">
                  <p style="font-size: 22px; margin-bottom: 0;">${localStorage.getItem("LANG") == "EN" ? 'Price' : 'Ціна'}</p>
                  <p style="font-size: 22px; margin-bottom: 0;"><span class="item_to_buy_uah">${price_UAH}</span>₴ / <span class="item_to_buy_usd">${price_USD}</span>$</p>
              </div>
              <div class="select_size__box w-100">
                  <p style="font-size: 22px; margin-bottom: 0;">${localStorage.getItem("LANG") == "EN" ? 'Size' : 'Розміри'}</p>
                  <select name="sizeSelect" class="input_select__size"  id="validationDefault03">
                      <option value="Select" selected>${localStorage.getItem("LANG") == "EN" ? 'Select' : 'Обрати'}</option>
                      ${checkSizeAmount(size_S, 'S')}
                      ${checkSizeAmount(size_M, 'M')}
                      ${checkSizeAmount(size_L, 'L')}
                      ${checkSizeAmount(size_XL, 'XL')}
                      ${checkSizeAmount(size_XXL, 'XXL')}
                      ${checkIfAnySizeChosen([size_S, size_M, size_L, size_XL, size_XXL])}
                  </select>
              </div>
              <div class="sizeScript" style="display: none;">
                ${script}
              </div>
              <div class="add_to__cart_btn__box w-100">
                  <button class="add_to__cart_btn" onClick="addProduct(${id}, '${name}', currSize, ${price_UAH}, ${price_USD}); showNotification('${name}', '.cart_message__block', currSize)">${localStorage.getItem("LANG") == "EN" ? 'Add to cart' : 'Додати до кошика'}</button>
              </div> 
          </div>
      </div>
  </div>
  <div class="row justify-content-center">
      <div class="col-12" style="margin-bottom: 30px">
          <div class="d-flex flex-column justify-content-evenly align-items-start" style="margin-bottom: 20x;">
              <h4 style="font-size: 27px">${localStorage.getItem("LANG") == "EN" ? 'Description' : 'Опис'}</h4>
              <p class="description_par">${localStorage.getItem("LANG") == "EN" ? description_en : description}</p>    
          </div>
          ${additional_info !== `` ? `<div class="d-flex flex-column justify-content-evenly align-items-start" style="margin-bottom: 20x;"><h4 style="font-size: 27px">${localStorage.getItem("LANG") == "EN" ? 'Additional Information' : 'Додаткова інформація'}</h4><p class="addinf_par">${localStorage.getItem("LANG") == "EN" ? additional_info_en : additional_info}</p></div>` : ''}
      </div>
  </div>`;
boxToAdd.innerHTML += innerClothes;