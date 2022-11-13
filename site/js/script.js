var listinha = document.getElementById('listinha');

// select all the radio buttons
var radios = listinha.querySelectorAll('input[type="radio"]');

console.log(radios);

for (var i = 0; i < listinha.length; i++) {
    // get radios[i] value

    console.log(listinha[i].textContent);
    listinha[i].textContent = "sjaisjaisi";
    console.log(listinha[i].textContent);
}