// Form
const adminName = document.querySelector('.name');
const adminSlug = document.querySelector('.slug');

adminName.addEventListener('input', (e) => {
  e.preventDefault();
  adminSlug.value = e.target.value.toLowerCase().replaceAll(/\W/g, '-').replaceAll(/-+/g, '-').replace(/^-/, '').replace(/-$/, '');
})

const sizeS = document.querySelector('.size_input_S'),
      sizeM = document.querySelector('.size_input_M'),
      sizeL = document.querySelector('.size_input_L'),
      sizeXL = document.querySelector('.size_input_XL'),
      sizeXXL = document.querySelector('.size_input_XXL');

const hidden_S = document.querySelector('.hidden_size_S'),
      hidden_M = document.querySelector('.hidden_size_M'),
      hidden_L = document.querySelector('.hidden_size_L'),
      hidden_XL = document.querySelector('.hidden_size_XL'),
      hidden_XXL = document.querySelector('.hidden_size_XXL');


sizeS.addEventListener('input', (e) => {
  e.preventDefault();
  let itm = e.target;
  if (itm.checked == 1) {
    hidden_S.value = itm.checked;
  } else {
    hidden_S.value = itm.checked;
  }
})

sizeM.addEventListener('input', (e) => {
  e.preventDefault();
  let itm = e.target;
  if (itm.checked == 1) {
    hidden_M.value = itm.checked;
  } else {
    hidden_M.value = itm.checked;
  }
})

sizeL.addEventListener('input', (e) => {
  e.preventDefault();
  let itm = e.target;
  if (itm.checked == 1) {
    hidden_L.value = itm.checked;
  } else {
    hidden_L.value = itm.checked;
  }
})

sizeXL.addEventListener('input', (e) => {
  e.preventDefault();
  let itm = e.target;
  if (itm.checked == 1) {
    hidden_XL.value = itm.checked;
  } else {
    hidden_XL.value = itm.checked;
  }
})

sizeXXL.addEventListener('input', (e) => {
  e.preventDefault();
  let itm = e.target;
  if (itm.checked == 1) {
    hidden_XXL.value = itm.checked;
  } else {
    hidden_XXL.value = itm.checked;
  }
})

// let amountSizeS = document.querySelector('.size_S__amount'), 
//     amountSizeM = document.querySelector('.size_M__amount'),
//     amountSizeL = document.querySelector('.size_L__amount'),
//     amountSizeXL = document.querySelector('.size_XL__amount'),
//     amountSizeXXL = document.querySelector('.size_XXL__amount');

// sizeS.addEventListener('input', (e) => {
//   e.preventDefault();
//   if (e.target.checked == true) {
//     amountSizeS.classList.remove('d-none');
//   } else {
//     amountSizeS.classList.add('d-none');
//   }
// })

// sizeM.addEventListener('input', (e) => {
//   e.preventDefault();
//   if (e.target.checked == true) {
//     amountSizeM.classList.remove('d-none');
//   } else {
//     amountSizeM.classList.add('d-none');
//   }
// })

// sizeL.addEventListener('input', (e) => {
//   e.preventDefault();
//   if (e.target.checked == true) {
//     amountSizeL.classList.remove('d-none');
//   } else {
//     amountSizeL.classList.add('d-none');
//   }
// })

// sizeXL.addEventListener('input', (e) => {
//   e.preventDefault();
//   if (e.target.checked == true) {
//     amountSizeXL.classList.remove('d-none');
//   } else {
//     amountSizeXL.classList.add('d-none');
//   }
// })

// sizeXXL.addEventListener('input', (e) => {
//   e.preventDefault();
//   if (e.target.checked == true) {
//     amountSizeXXL.classList.remove('d-none');
//   } else {
//     amountSizeXXL.classList.add('d-none');
//   }
// })



// let mainAmount = document.querySelector('.main_amount');
// let secondaryAmounts = document.querySelectorAll('.secondary_amount')
// let sizeCheckboxes = document.querySelectorAll('.size_checkboxes');

// secondaryAmounts.forEach(item => {
//   item.addEventListener('input', (e) => {
//     e.preventDefault();
//     let tempAmountSum = 0;
//     secondaryAmounts.forEach(elem => {
//       if (!elem.classList.contains('d-none') && elem.value !== '') {
//         tempAmountSum += parseInt(elem.value);
//       } else if (elem.classList.contains('d-none') == true) {
//         elem.value = '';
//         tempAmountSum += 0;
//       }
//     })
//     sizeCheckboxes.forEach(item => {
//       item.addEventListener('input', (ev) => {
//         ev.preventDefault();
//         if (item.checked == false) {
//           mainAmount.value -= item.parentElement.parentElement.lastElementChild.value; 
//           item.parentElement.parentElement.lastElementChild.value = 0;  
//         }
//       })
//     })
//     mainAmount.value = tempAmountSum;
//   })
// })