function changeColor(getColor) {
    let bg = document.querySelector('.bg');
    let selectColor = getColor.value;
    bg.style.background = selectColor;
    let text = getColor.options[getColor.selectedIndex].text;
    bg.innerHTML = text;
}
