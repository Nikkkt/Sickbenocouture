let sizeCheckBox = document.querySelectorAll('.size_checkboxes');
sizeCheckBox.forEach(item => {
  if (item.previousElementSibling.value == 'true') {
    item.setAttribute('checked', 'true')
  }
})

let btnUpdateCheckOut = document.querySelector('#btn_check_update');
let checkIfUpdateHiddenInput = document.querySelector('.hidden_if_update');

btnUpdateCheckOut.addEventListener('click', (e) => {
  checkIfUpdateHiddenInput.value = 'Update';
})

let btnImagesCheckOut = document.querySelector('#btn_check_images');
let checkIfImagesHiddenInput = document.querySelector('.hidden_if_delete_all_images');

btnImagesCheckOut.addEventListener('click', (e) => {
  e.preventDefault();
  checkIfImagesHiddenInput.value = 'Clear';
})