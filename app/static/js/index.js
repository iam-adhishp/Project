function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
 }

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
 }


const searchInput = document.querySelector('input[name="q"]');
searchInput.addEventListener('input', function () {
    const query = this.value;
    fetch('/search/?q=${query}')
       .then(response => response.text())
       .then(data => {
          document.querySelector('#results').innerHTML = data;
       });
 });

document.querySelector('input[name="q"]').addEventListener('input', function () {
    const query = this.value;
    fetch('/autocomplete/?q=${query}')
       .then(response => response.json())
       .then(data => {
          const suggestions = data.map(item => '<option value="${item.name}">');
          document.querySelector('#suggestions').innerHTML = suggestions.join('');
       });
 });